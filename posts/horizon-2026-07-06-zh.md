# Horizon 每日速递 - 2026-07-06

> 从 30 条内容中筛选出 1 条重要资讯。

---

1. [能力门控：基于内部置信信号控制工具使用](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [能力门控：基于内部置信信号控制工具使用](https://www.reddit.com/r/MachineLearning/comments/1unw5un/competence_gate_gating_tooluse_on_a_small_models/) ⭐️ 8.0/10

一个针对 Qwen3.5-4B 的 10MB LoRA 适配器，基于模型内部置信信号而非口头表达的置信度来控制工具使用，将错误检测的 d′提升了 0.46，并将私密查询泄露到公共搜索的比例从 22%降低到 10%。 该方法通过直接读取内部激活状态，解决了小型语言模型无法准确表达不确定性的根本局限，使工具使用更可靠，并在本地部署中更好地保护隐私。 该门控使用一个在内部激活上训练的 LoRA 探针，针对每个查询决定是直接回答、搜索网络还是从本地文档检索；它可在 Apple Silicon（MLX）上本地运行，并通过 GGUF 支持 llama.cpp/Ollama，在 GGUF 模式下具有保守偏差。

reddit · r/MachineLearning · /u/Synthium- · 7月5日 07:49

**背景**: 小型语言模型通常难以表达自身的不确定性，即使出错也倾向于表现出自信。LoRA（低秩适配）是一种参数高效的微调方法，它在冻结的基础模型上添加小型可训练矩阵。内部置信信号——模型内部的隐藏状态——已被证明编码了关于答案正确性的信息，而这些信息并未反映在口头输出中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2106.09685">[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2604.22271">[2604.22271] How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals</a></li>
<li><a href="https://medium.com/@georgekar91/measuring-confidence-in-llm-responses-e7df525c283f">Measuring Confidence in LLM responses | by George Karapetyan | Medium</a></li>

</ul>
</details>

**标签**: `#confidence estimation`, `#tool use`, `#LoRA`, `#small language models`, `#open source`

---

