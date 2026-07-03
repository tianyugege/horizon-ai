from __future__ import annotations

from src.models import (
    AIConfig,
    AIProvider,
    Config,
    FilteringConfig,
    GDELTConfig,
    GitHubSourceConfig,
    GoogleNewsConfig,
    HackerNewsConfig,
    OSSInsightConfig,
    RSSSourceConfig,
    RedditConfig,
    SourcesConfig,
    TelegramChannelConfig,
    TelegramConfig,
    TwitterConfig,
)
from src.setup import wizard


def test_configure_ai_allows_ollama_without_api_key(monkeypatch):
    answers = iter(
        [
            "ollama",
            "llama3.2",
            "http://nas.local:11434",
            "",
            "zh,en",
        ]
    )

    monkeypatch.setattr(wizard.Prompt, "ask", lambda *args, **kwargs: next(answers))
    monkeypatch.setattr(wizard.console, "print", lambda *args, **kwargs: None)

    config = wizard.configure_ai()

    assert config == AIConfig(
        provider=AIProvider.OLLAMA,
        model="llama3.2",
        base_url="http://nas.local:11434",
        api_key_env="",
        temperature=0.3,
        max_tokens=8192,
        languages=["zh", "en"],
    )


def test_ai_recommendations_available_for_ollama_without_api_key():
    config = AIConfig(
        provider=AIProvider.OLLAMA,
        model="llama3.1",
        api_key_env="",
    )

    assert wizard._ai_recommendations_available(config) is True


def test_ai_recommendations_require_api_key_for_cloud_provider(monkeypatch):
    config = AIConfig(
        provider=AIProvider.OPENAI,
        model="gpt-4",
        api_key_env="OPENAI_API_KEY",
    )
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    assert wizard._ai_recommendations_available(config) is False

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    assert wizard._ai_recommendations_available(config) is True


def test_build_config_supports_query_based_sources():
    ai_config = AIConfig(
        provider=AIProvider.OPENAI,
        model="gpt-4",
        api_key_env="OPENAI_API_KEY",
    )
    selected_sources = [
        {
            "type": "ossinsight",
            "config": {
                "period": "past_24_hours",
                "languages": ["All", "Python"],
                "keywords": ["llm"],
                "min_stars": 20,
                "max_items": 10,
            },
        },
        {
            "type": "gdelt",
            "config": {
                "query": "cybersecurity",
                "mode": "ArtList",
                "max_records": 40,
                "language": "english",
                "category": "security-news",
            },
        },
        {
            "type": "google_news",
            "config": {
                "query": "react",
                "language": "en",
                "country": "US",
                "max_results": 25,
                "category": "web-news",
            },
        },
    ]

    config = wizard.build_config(ai_config, selected_sources)

    assert config.sources.ossinsight.enabled is True
    assert config.sources.ossinsight.keywords == ["llm"]
    assert config.sources.gdelt == GDELTConfig(
        enabled=True,
        query="cybersecurity",
        mode="ArtList",
        max_records=40,
        language="english",
        category="security-news",
    )
    assert config.sources.google_news == GoogleNewsConfig(
        enabled=True,
        query="react",
        language="en",
        country="US",
        max_results=25,
        category="web-news",
    )


def test_merge_configs_preserves_existing_optional_sources():
    new_config = Config(
        ai=AIConfig(provider=AIProvider.OPENAI, model="gpt-4", api_key_env="OPENAI_API_KEY"),
        filtering=FilteringConfig(),
        sources=SourcesConfig(
            github=[GitHubSourceConfig(type="repo_releases", owner="rust-lang", repo="rust")],
            hackernews=HackerNewsConfig(enabled=True),
            rss=[RSSSourceConfig(name="Test", url="https://example.com/feed.xml")],
            reddit=RedditConfig(),
            telegram=TelegramConfig(),
        ),
    )
    existing_config = Config(
        ai=AIConfig(provider=AIProvider.OPENAI, model="gpt-4", api_key_env="OPENAI_API_KEY"),
        filtering=FilteringConfig(),
        sources=SourcesConfig(
            github=[],
            hackernews=HackerNewsConfig(enabled=True),
            rss=[],
            reddit=RedditConfig(),
            telegram=TelegramConfig(
                enabled=True,
                channels=[TelegramChannelConfig(channel="horizon_news")],
            ),
            twitter=TwitterConfig(enabled=True, users=["karpathy"]),
            ossinsight=OSSInsightConfig(enabled=True, keywords=["agent"]),
            gdelt=GDELTConfig(enabled=True, query="ai policy"),
            google_news=GoogleNewsConfig(enabled=True, query="open source"),
        ),
    )

    merged = wizard.merge_configs(new_config, existing_config)

    assert merged.sources.telegram.enabled is True
    assert [channel.channel for channel in merged.sources.telegram.channels] == ["horizon_news"]
    assert merged.sources.twitter is not None
    assert merged.sources.twitter.users == ["karpathy"]
    assert merged.sources.ossinsight.enabled is True
    assert merged.sources.ossinsight.keywords == ["agent"]
    assert merged.sources.gdelt is not None
    assert merged.sources.gdelt.query == "ai policy"
    assert merged.sources.google_news is not None
    assert merged.sources.google_news.query == "open source"
