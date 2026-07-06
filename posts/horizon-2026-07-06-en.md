# Horizon Daily - 2026-07-06

> From 30 items, 1 important content pieces were selected

---

1. [Competence Gate: Gating Tool-Use on Internal Confidence Signals](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Competence Gate: Gating Tool-Use on Internal Confidence Signals](https://www.reddit.com/r/MachineLearning/comments/1unw5un/competence_gate_gating_tooluse_on_a_small_models/) ⭐️ 8.0/10

A 10MB LoRA adapter for Qwen3.5-4B gates tool use on internal model confidence signals instead of verbalized confidence, improving error detection (d′ improvement of 0.46) and reducing private query leakage to public search from 22% to 10%. This approach addresses a fundamental limitation of small language models—their inability to accurately verbalize uncertainty—by directly reading internal activations, making tool-use more reliable and privacy-preserving for local deployments. The gate uses a LoRA probe trained on internal activations to decide per query whether to answer directly, search the web, or retrieve from local documents; it runs locally on Apple Silicon (MLX) and via GGUF for llama.cpp/Ollama, with a conservative bias in GGUF mode.

reddit · r/MachineLearning · /u/Synthium- · Jul 5, 07:49

**Background**: Small language models often struggle to express their own uncertainty, tending to appear confident even when wrong. LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning method that adds small trainable matrices to a frozen base model. Internal confidence signals—hidden states within the model—have been shown to encode information about answer correctness that is not reflected in verbal outputs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2106.09685">[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2604.22271">[2604.22271] How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals</a></li>
<li><a href="https://medium.com/@georgekar91/measuring-confidence-in-llm-responses-e7df525c283f">Measuring Confidence in LLM responses | by George Karapetyan | Medium</a></li>

</ul>
</details>

**Tags**: `#confidence estimation`, `#tool use`, `#LoRA`, `#small language models`, `#open source`

---

