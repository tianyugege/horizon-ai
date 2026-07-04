# Horizon Daily - 2026-07-04

> From 53 items, 13 important content pieces were selected

---

1. [EU Parliament Spy Probe Member Hacked with Pegasus](#item-1) ⭐️ 9.0/10
2. [Anthropic Accuses Alibaba of Massive Distillation Attack on Claude](#item-2) ⭐️ 9.0/10
3. [Jamesob's Guide to Running SOTA LLMs Locally](#item-3) ⭐️ 8.0/10
4. [Wordgard: New Rich-Text Editor from ProseMirror Creator](#item-4) ⭐️ 8.0/10
5. [Ubicloud on PostgreSQL and Strict Memory Overcommit](#item-5) ⭐️ 8.0/10
6. [Open Source AI Gap Map v0.1 Launched](#item-6) ⭐️ 8.0/10
7. [CDD recovers finetuning data from LLM logits without weights](#item-7) ⭐️ 8.0/10
8. [Claude Fable 5 Relaunch Disappoints with Aggressive Safety Filters](#item-8) ⭐️ 8.0/10
9. [Huawei Launches Atlas 350 Accelerator with Ascend 950PR, 2.87x H20 Performance](#item-9) ⭐️ 8.0/10
10. [China Proposes 6-Month Inactive Account Deactivation Rule](#item-10) ⭐️ 8.0/10
11. [Geekerwan Review: Mate 80 Pro Gaming Efficiency Beats Snapdragon 8 Gen3](#item-11) ⭐️ 8.0/10
12. [NASA Launches Rescue Satellite to Save Falling Space Telescope](#item-12) ⭐️ 8.0/10
13. [Tencent Xuanwu Lab's Atuin AI beats Mythos in CyberGym test](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [EU Parliament Spy Probe Member Hacked with Pegasus](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 9.0/10

Citizen Lab confirmed with high confidence that Stelios Kouloglou, a European Parliament member investigating spyware, had his iPhone infected with Pegasus spyware on October 21, 2022, and again on March 6-7, 2023. This marks the first confirmed case of a sitting European Parliament member being hacked with Pegasus, exposing a sophisticated cross-border espionage campaign that threatens EU democratic institutions and raises urgent questions about state-sponsored surveillance within the bloc. The first infection overlapped with a previously identified Pegasus campaign targeting Russian and Belarusian-speaking exiled journalists in Europe, suggesting a single Pegasus customer with authorization to spy across multiple EU countries was responsible.

hackernews · ledoge · Jul 3, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48779683)

**Background**: Pegasus is spyware developed by Israeli firm NSO Group, marketed for fighting crime and terrorism but widely used by governments to surveil journalists, activists, and dissidents. Citizen Lab, based at the University of Toronto, is a leading research lab that investigates digital threats and has published numerous reports on Pegasus infections. The European Parliament has been investigating the use of spyware like Pegasus across member states.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the Pegasus scandal in Greece, where many politicians were hacked, was never fully resolved and may have been orchestrated by the prime minister's office. Others pointed out that some European countries have abused Pegasus so extensively that Israeli firms cut ties with them, highlighting the irony of an EU parliament member being spied on by the same tools used against journalists.

**Tags**: `#cybersecurity`, `#spyware`, `#Pegasus`, `#surveillance`, `#European Parliament`

---

<a id="item-2"></a>
## [Anthropic Accuses Alibaba of Massive Distillation Attack on Claude](https://t.me/zaihuapd/42327) ⭐️ 9.0/10

Anthropic has accused Alibaba of orchestrating the largest known distillation attack against its Claude AI model, using approximately 25,000 fraudulent accounts to generate 28.8 million interactions between April 22 and June 5, 2026. In response, Alibaba ordered all employees to uninstall Anthropic products, including Claude Sonnet, Opus, and Fable, effective July 10, 2026. This accusation highlights a new frontier in AI intellectual property theft, where model distillation attacks can replicate expensive proprietary models at a fraction of the cost. The involvement of a major Chinese tech firm and the unprecedented scale of the attack could escalate geopolitical tensions and reshape how AI companies secure their APIs. Anthropic stated that the attack exhibited hallmarks of distillation: massive volume concentrated in a few areas, highly repetitive structures, and content directly valuable for training an AI model. Alibaba's internal memo cited the need to protect its own AI development and banned employee use of Anthropic's models and agent products like Claude Code.

telegram · zaihuapd · Jul 3, 06:21

**Background**: Model distillation is a machine learning technique where a smaller 'student' model learns to replicate the outputs of a larger 'teacher' model, often by training on the teacher's responses. When used without authorization at scale, it becomes a distillation attack — a form of intellectual property theft that undermines the massive R&D investment required to build advanced AI models. Anthropic had previously tightened its security policies after detecting the suspicious activity.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://medium.com/@tahirbalarabe2/understanding-llm-distillation-attacks-929306ca38cd">Understanding LLM Distillation Attacks | by Tahir | Medium</a></li>
<li><a href="https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained">AI Model Distillation Attacks: What They Are and Why They Matter | MindStudio</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#model distillation`, `#Anthropic`, `#Alibaba`, `#geopolitics`

---

<a id="item-3"></a>
## [Jamesob's Guide to Running SOTA LLMs Locally](https://github.com/jamesob/local-llm) ⭐️ 8.0/10

Jamesob published a comprehensive guide on GitHub detailing how to run state-of-the-art large language models locally, including hardware recommendations and cost estimates. The guide sparked extensive community debate about the practicality and expense of local inference. This guide highlights the growing interest in local AI inference as an alternative to cloud subscriptions, but the community discussion reveals that running SOTA models locally remains prohibitively expensive for most users. The cost of a high-end local setup (around $50,000) can equal over 16 years of cloud subscription fees, challenging the value proposition. The guide's recommended high-end build costs approximately $50,000, including four $12,000 GPUs, and relies on quantization and pruning techniques to fit models into available VRAM. Community members note that even with such hardware, models like GLM-5.2 may require 8x H200 GPUs (closer to $400,000) for comfortable inference, and quantized models can suffer from quality degradation and reasoning loops.

hackernews · livestyle · Jul 3, 15:03 · [Discussion](https://news.ycombinator.com/item?id=48775921)

**Background**: Running large language models locally requires significant GPU memory (VRAM) to hold the model weights and perform inference. Quantization reduces model precision (e.g., from 16-bit to 4-bit) to shrink memory requirements, but can degrade output quality. Cloud APIs like Claude Opus or GPT-5 offer access to full-precision models for a monthly subscription fee, eliminating upfront hardware costs.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/tamizuddin/mastering-local-deployment-of-sota-llms-jamesobs-guide-to-overcoming-resource-constraints-4ldf">Mastering Local Deployment of SOTA LLMs... - DEV Community</a></li>
<li><a href="https://www.sitepoint.com/local-llms-vs-cloud-api-cost-analysis-2026/">Local LLMs vs Cloud APIs: 2026 Total Cost of Ownership Analysis | SitePoint</a></li>
<li><a href="https://www.mindstudio.ai/blog/local-ai-vs-cloud-ai-2026">Local AI vs Cloud AI in 2026: When to Run Models on Your Own Hardware | MindStudio</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: some users warn that local setups are wildly expensive and lower quality than cloud APIs, while others point to mid-range options like 128GB unified memory systems running DeepSeek V4 flash as a reasonable compromise. A key concern is that quantized models often perform worse in practice than benchmarks suggest, with issues like reasoning loops in Qwen3.6.

**Tags**: `#LLM`, `#local inference`, `#hardware`, `#cost analysis`, `#open source`

---

<a id="item-4"></a>
## [Wordgard: New Rich-Text Editor from ProseMirror Creator](https://wordgard.net/) ⭐️ 8.0/10

Marijn Haverbeke, the creator of ProseMirror, has released Wordgard, a new in-browser rich-text editor that offers a refined approach to WYSIWYG editing. The project is available at wordgard.net and includes detailed documentation comparing it to ProseMirror. This release is significant because it comes from a highly respected author in the web development community, and it addresses long-standing challenges in building robust WYSIWYG editors. It could influence the next generation of rich-text editing frameworks and impact projects like Tiptap that currently rely on ProseMirror. Wordgard shares many concepts with ProseMirror but does not provide an upgrade path, meaning switching requires significant rework. The editor features a clean, tasteful design by artist Kamila Stankiewicz, and the community has noted its strong technical depth and validation.

hackernews · indy · Jul 3, 08:50 · [Discussion](https://news.ycombinator.com/item?id=48772573)

**Background**: ProseMirror is a battle-tested core foundation for many rich-text editors, including Tiptap, known for its lightweight core and steep learning curve. WYSIWYG editors aim to produce clean, semantically meaningful documents while remaining user-friendly, a challenge that has persisted for over two decades without a standard web implementation.

<details><summary>References</summary>
<ul>
<li><a href="https://prosemirror.net/">ProseMirror</a></li>

</ul>
</details>

**Discussion**: The community discussion is highly engaged, with users expressing excitement about Wordgard's design and technical approach, while also raising practical concerns about migration difficulty from ProseMirror. Some users noted the lack of a static type system for document schemas as a pain point in ProseMirror, which Wordgard may address.

**Tags**: `#rich-text editor`, `#ProseMirror`, `#web development`, `#open source`, `#WYSIWYG`

---

<a id="item-5"></a>
## [Ubicloud on PostgreSQL and Strict Memory Overcommit](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit) ⭐️ 8.0/10

Ubicloud published a technical blog post explaining why they use strict memory overcommit (vm.overcommit_memory=2) for PostgreSQL to prevent the Linux OOM killer from terminating the database process. The article details the trade-offs between the default heuristic overcommit mode and the strict mode. This matters because PostgreSQL is sensitive to memory pressure and the OOM killer can cause catastrophic database downtime. The discussion highlights a critical configuration decision for database administrators running PostgreSQL on Linux, especially in production environments. The strict mode (mode 2) prevents memory overcommit but can cause fork() failures if the system runs out of memory, which may affect application startup. The article warns that adjusting overcommit ratios without careful testing can lead to instability, and recommends thorough QA testing before production deployment.

hackernews · furkansahin · Jul 3, 13:00 · [Discussion](https://news.ycombinator.com/item?id=48774509)

**Background**: Linux uses memory overcommit by default, allowing processes to allocate more virtual memory than physical RAM plus swap. The OOM killer is a kernel mechanism that terminates processes when the system runs out of memory. PostgreSQL, being a memory-intensive database, is a frequent target of the OOM killer under memory pressure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.baeldung.com/linux/overcommit-modes">Linux Overcommit Modes - Baeldung</a></li>
<li><a href="https://www.kernel.org/doc/html/v5.1/vm/overcommit-accounting.html">Overcommit Accounting — The Linux Kernel documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/OOM_killer">OOM killer</a></li>

</ul>
</details>

**Discussion**: Community comments reveal mixed experiences: some users report that Linux default memory management is problematic in 2026, while others caution that strict overcommit can break applications that rely on fork(). The author acknowledges the blog post's title was too strong and notes that strict mode has unanticipated side-effects in many scenarios.

**Tags**: `#PostgreSQL`, `#Linux`, `#memory management`, `#OOM killer`, `#database administration`

---

<a id="item-6"></a>
## [Open Source AI Gap Map v0.1 Launched](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI, a well-funded non-profit, launched the Open Source AI Gap Map v0.1, a detailed index of 421 open source AI products across models, tools, datasets, and hardware. The underlying data, including 1,184 YAML files and 16,185 tracked GitHub repos, is released under an MIT license. This map provides a structured, comprehensive view of the open source AI ecosystem, helping researchers, developers, and strategists identify gaps and opportunities. It addresses a critical need for landscape mapping in a rapidly evolving field, backed by a credible non-profit with $400 million in committed capital. The Gap Map v0.1 details 421 products: 266 software tools and libraries, 85 models, 50 datasets, and 20 hardware projects from 228 organizations. The data is available on GitHub under an MIT license, and can be explored via Datasette Lite using a CSV of 16,185 repos.

rss · Simon Willison · Jul 3, 22:04

**Background**: Current AI is a global non-profit partnership founded at the AI Action Summit in Paris in February 2025, with over $400 million committed and a goal to mobilize $2.5 billion over five years. The Gap Map builds on work from the Columbia Convening, MOF, Hugging Face, and others, evaluating over 24,626 projects across openness, capability, and adoption.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/">Open Source AI Gap Map - simonwillison.net</a></li>
<li><a href="https://map.currentai.org/">Current AI – Open Source AI Gap Map</a></li>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1 - currentai.org</a></li>

</ul>
</details>

**Tags**: `#open source`, `#AI`, `#ecosystem mapping`, `#non-profit`, `#landscape analysis`

---

<a id="item-7"></a>
## [CDD recovers finetuning data from LLM logits without weights](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

Contrastive Decoding Diffing (CDD) recovers verbatim finetuning data from large language models using only grey-box logit access, without requiring model weights, activations, or a probe corpus. It achieves a verbatim recovery score of 4+ out of 5 on 19 out of 20 organism-model pairs across four model families (1B to 32B parameters) on the SDF benchmark, significantly outperforming the prior Activation Difference Lens (ADL) method which never exceeds 3/5 despite needing full weight access. This research exposes a significant privacy and security vulnerability in LLM fine-tuning pipelines, showing that sensitive training data can be extracted with minimal access. It also demonstrates that synthetic data generated by LLMs can leave unintended fingerprints—such as the recurring fictional persona "Dr. Elena Rodriguez"—which CDD can recover, raising concerns about data leakage and model transparency. CDD works by contrasting the logits of the base and finetuned models directly, using a single default configuration with no per-organism calibration or layer selection. An unplanned finding revealed that the name "Dr. Elena Rodriguez" appeared across four semantically unrelated finetuning domains because Claude Sonnet 3.6 disproportionately favors this name when generating fictional scientists for synthetic data, causing it to be baked into every finetune that used LLM-generated training data.

reddit · r/MachineLearning · /u/CebulkaZapiekana · Jul 3, 19:01

**Background**: Model diffing is a technique for comparing a base model with its finetuned counterpart to understand what changed during fine-tuning. Prior work, such as the Activation Difference Lens (ADL), required white-box access (full weights and activations) and could only recover vague domain-level descriptions. Grey-box methods like CDD operate only on model outputs (logits), making them more practical for real-world scenarios where internal model access is restricted. The SDF benchmark is a standard evaluation for measuring how well a method can recover verbatim fine-tuning data.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2510.13900">Narrow Finetuning Leaves Clearly Readable Traces in Activation Differences</a></li>
<li><a href="https://www.emergentmind.com/topics/activation-difference-lens-adl">Activation Difference Lens (ADL) - emergentmind.com</a></li>
<li><a href="https://arxiv.org/html/2503.14043v1">Learning on LLM Output Signatures for gray-box LLM Behavior ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#model diffing`, `#privacy`, `#finetuning`, `#security`

---

<a id="item-8"></a>
## [Claude Fable 5 Relaunch Disappoints with Aggressive Safety Filters](https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-relaunch-disappoints-users-with-nerfed-performance/) ⭐️ 8.0/10

After US export controls were lifted, Anthropic relaunched Claude Fable 5, but users report severe performance degradation due to overly aggressive safety filters that trigger false positives on low-level code and keywords like "vulnerability" or "hook." Additionally, subscription users face usage caps (50% weekly quota until July 7, after which the model shifts to pay-per-use), and the model automatically downgrades to Opus 4.8 when safety thresholds are triggered. This regression undermines developer trust in Anthropic's flagship model, especially for low-level coding tasks where safety over-filtering directly blocks legitimate workflows. The shift from subscription to pay-per-use also alters the cost structure for developers, potentially driving them to competing models. Media reports confirm the model's core capabilities are unchanged; the issue is solely due to excessive safety guardrails. The API and pay-per-use enterprise tier still provide full access to Fable 5, but Anthropic has not yet announced a fix for the false positive problem.

telegram · zaihuapd · Jul 3, 07:20

**Background**: Claude Fable 5 is Anthropic's highest-scoring model on FrontierBench, a frontier coding evaluation, and is designed for long-horizon reasoning and autonomous software engineering. Anthropic has a strong focus on AI safety, and its Acceptable Use Policy classifiers have historically caused false positives in developer workflows, as seen with Opus 4.7. The model was previously unavailable due to US export controls and has now been relaunched.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://letsdatascience.com/news/anthropic-tightens-opus-47-acceptable-use-filters-b397e1fb">Anthropic Tightens Opus 4.7 Acceptable Use Filters</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Claude`, `#Anthropic`, `#safety`, `#developer experience`

---

<a id="item-9"></a>
## [Huawei Launches Atlas 350 Accelerator with Ascend 950PR, 2.87x H20 Performance](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

At the Huawei China Partner Conference 2026, Huawei officially launched and released the Atlas 350 AI accelerator card powered by the new Ascend 950PR processor. The card claims 2.87 times the compute power of NVIDIA's H20 and is the only domestic accelerator supporting FP4 low-precision inference. This announcement is significant because it demonstrates Huawei's continued progress in AI hardware amid ongoing export restrictions on advanced NVIDIA chips to China. The Atlas 350's claimed performance leap could reshape the competitive landscape for AI inference in the Chinese market and reduce dependence on foreign GPU suppliers. The Atlas 350 features 112 GB of HBM memory and can load a 70B-parameter model on a single card. It delivers 1.56 petaflops of FP4 compute power, and the Ascend 950PR processor includes significant improvements in vector compute, interconnect bandwidth, and self-developed HBM compared to its predecessor.

telegram · zaihuapd · Jul 3, 08:35

**Background**: FP4 (4-bit floating point) precision is a low-precision format that can significantly reduce memory usage and accelerate inference for large language models, often achieving up to 8x model size reduction compared to full precision. The Ascend 950PR is Huawei's latest AI chip, designed to compete with NVIDIA's offerings in the Chinese market where export controls limit access to high-end NVIDIA GPUs like the H100. The Atlas 350 is positioned as a direct competitor to NVIDIA's H20, which was specifically designed to comply with US export restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://asted.cloud/news/huawei-announced-the-ai-accelerator-atlas-350-which-outperforms-nvidia-h20-in-efficiency">Huawei announced the AI accelerator Atlas 350 , which... - Asted Cloud</a></li>
<li><a href="https://www.huaweicentral.com/ascend-950pr-ai-chip-everything-you-need-to-know/">Ascend 950PR AI Chip: Everything you need to know - Huawei Central</a></li>
<li><a href="https://www.techradar.com/pro/huawei-reveals-its-latest-nvidia-h20-killer-packing-a-frankly-ridiculous-1-56-pflops-of-fp4-compute-and-up-to-112gb-of-hbm">Huawei Atlas 350 accelerator pushes AI limits with massive compute</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#Huawei`, `#Ascend`, `#accelerator`, `#FP4`

---

<a id="item-10"></a>
## [China Proposes 6-Month Inactive Account Deactivation Rule](https://mp.weixin.qq.com/s/TfYZaC8ULPvu9JeTqYGkKg) ⭐️ 8.0/10

On July 3, 2026, China's Cyberspace Administration released a revised draft of the Internet Information Service Management Measures for public comment, proposing that platforms may deactivate accounts inactive for over 6 months and must support unbinding when phone numbers change hands. The draft also mandates AI content labeling, prohibits forced use of intelligent services, requires an opt-out option for personalized recommendations, and bans manipulation of rankings and fake trends. This regulation significantly impacts how internet platforms in China manage user accounts, AI-generated content, and algorithmic recommendations, affecting billions of users and major tech companies. It represents a major step in China's ongoing effort to strengthen data privacy, AI governance, and online content integrity, potentially setting a global precedent for similar policies. The draft requires large internet platforms to handle complaints about illegal or harmful content within 24 hours. It also builds on earlier AI-specific regulations, such as the Measures for the Identification of AI-Generated Synthetic Content adopted in March 2025, which take effect on September 1, 2025.

telegram · zaihuapd · Jul 3, 11:29

**Background**: China has been progressively tightening its internet governance framework under three overarching laws: the Cybersecurity Law, the Personal Information Protection Law (PIPL), and the Data Security Law. The Cyberspace Administration of China (CAC) is the primary regulator for algorithms, generative AI, content labeling, and deepfakes, having issued multiple AI-specific rules since 2022. The new draft updates the existing Internet Information Service Management Measures to address emerging issues like account lifecycle management and AI content transparency.

<details><summary>References</summary>
<ul>
<li><a href="https://getcoai.com/news/inside-chinas-plan-to-make-ai-watermarks-happen/">Inside China ’s plan to make AI watermarks happen - CO/ AI</a></li>
<li><a href="https://reg-intel.com/china-ai-regulation-2026-every-law-rule-and-draft-in-one-place/">China AI Regulation 2026: Every Law, Rule, and Draft in... - Reg Intel</a></li>
<li><a href="https://www.imatag.com/blog/china-regulates-ai-generated-content-towards-a-new-global-standard-for-transparency">China Regulates AI -Generated Content : Towards a New Global...</a></li>

</ul>
</details>

**Tags**: `#regulation`, `#China`, `#data privacy`, `#AI governance`, `#internet policy`

---

<a id="item-11"></a>
## [Geekerwan Review: Mate 80 Pro Gaming Efficiency Beats Snapdragon 8 Gen3](https://www.bilibili.com/video/BV1F7T46wEyT) ⭐️ 8.0/10

Geekerwan's review of the Huawei Mate 80 Pro series shows that the Kirin 9030 chip, despite lower theoretical performance, achieves better gaming power efficiency than the Snapdragon 8 Gen3 thanks to native HarmonyOS optimizations. This demonstrates that deep software-hardware integration can overcome raw hardware disadvantages, potentially shifting the mobile industry's focus from pure specs to ecosystem optimization. The Mate 80 Pro Max runs Genshin Impact at 60fps with only 4.9W total power consumption, and Honor of Kings at 120fps with about 3W, both outperforming Snapdragon 8 Gen3 in efficiency.

telegram · zaihuapd · Jul 3, 13:27

**Background**: Huawei's Kirin 9030 Pro is a 9-core chipset announced in November 2025, manufactured on a 5nm or 7nm process. HarmonyOS NEXT removes Android AOSP code, allowing native apps to run directly on the HarmonyOS kernel for better performance.

<details><summary>References</summary>
<ul>
<li><a href="https://nanoreview.net/en/soc/hisilicon-kirin-9030">HiSilicon Kirin 9030 Pro: specs and benchmarks - NanoReview</a></li>
<li><a href="https://en.wikipedia.org/wiki/HarmonyOS">HarmonyOS - Wikipedia</a></li>
<li><a href="https://dev.to/flfljh/flutter-performance-tuning-on-harmonyos-performance-analysis-and-boundary-definition-4270">Flutter Performance Tuning on HarmonyOS ... - DEV Community</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#Kirin 9030`, `#HarmonyOS`, `#mobile chipset`, `#gaming performance`

---

<a id="item-12"></a>
## [NASA Launches Rescue Satellite to Save Falling Space Telescope](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 8.0/10

On July 3, 2026, NASA launched the LINK spacecraft, built by startup Katalyst Space Technologies, to capture and boost the aging Swift space telescope to a higher orbit. This marks the first private attempt to grab a U.S. government satellite in orbit. This mission could extend the life of a valuable scientific instrument and demonstrate a new paradigm for on-orbit satellite servicing, reducing orbital debris and saving taxpayer money. Success would validate public-private partnerships in space operations and encourage broader commercial servicing of government satellites. The LINK spacecraft will use a robotic arm to grab Swift, then fire thrusters to raise its orbit by about 240 kilometers. If successful, Swift could resume science observations as early as September 2026.

telegram · zaihuapd · Jul 3, 15:43

**Background**: The Neil Gehrels Swift Observatory, launched in 2004, detects gamma-ray bursts, X-rays, and ultraviolet light from cosmic explosions. Its orbit has been decaying faster than expected due to increased solar activity, threatening to burn up in Earth's atmosphere as early as October 2026. On-orbit satellite servicing—refueling, repairing, or boosting satellites—has long been a goal but rarely attempted, especially by private companies.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/space/2026/06/a-bold-satellite-rescue-mission-came-together-in-record-time-but-will-it-work/">A bold satellite rescue mission came together in record... - Ars Technica</a></li>
<li><a href="https://www.nytimes.com/2026/07/03/science/nasa-swift-telescope-rescue-mission.html">A Mission to Save NASA’s Swift Telescope Launches to Orbit</a></li>
<li><a href="https://www.foxweather.com/earth-space/nasa-rescue-mission-telescope-sinking-earth-atmosphere">NASA to conduct daring rescue mission to reposition... | Fox Weather</a></li>

</ul>
</details>

**Tags**: `#space`, `#satellite servicing`, `#NASA`, `#orbital debris`, `#private space`

---

<a id="item-13"></a>
## [Tencent Xuanwu Lab's Atuin AI beats Mythos in CyberGym test](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 8.0/10

Tencent Xuanwu Lab announced that its Atuin AI, built on the open-source GLM-5.1 model, scored 84.0% on the UC Berkeley-led CyberGym cybersecurity benchmark, surpassing Anthropic's Claude Mythos Preview while using less than 0.1% of the budget. Atuin also discovered multiple high-severity logic vulnerabilities in projects like curl, OpenSSL, and Python cryptography that Mythos missed. This demonstrates that a locally deployable open-source model can outperform a major proprietary competitor in AI-driven vulnerability detection at a fraction of the cost, potentially democratizing advanced cybersecurity capabilities. The discovery of critical vulnerabilities in widely-used open-source projects highlights the practical impact and could reshape how organizations approach automated security testing. Atuin AI achieved the highest severity ranking (1st) on the Berkeley BVI real-world vulnerability list, and 5th in total number of vulnerabilities found. The tool is based on GLM-5.1, an open-source model designed for long-horizon agentic tasks that can work autonomously for up to 8 hours.

telegram · zaihuapd · Jul 3, 16:12

**Background**: CyberGym is a benchmark from UC Berkeley that evaluates AI agents on end-to-end cybersecurity tasks, including vulnerability detection, proof-of-concept generation, and patching. GLM-5.1 is Z.AI's latest flagship open-source model, optimized for autonomous coding and engineering tasks, with performance comparable to Claude Opus 4.6. The 'Glass Wing Project' (玻璃翼计划) is Anthropic's initiative behind Claude Mythos, which typically requires substantial computational resources.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.1">GLM-5.1 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://llm-stats.com/benchmarks/cybergym">CyberGym Benchmark Leaderboard | LLM Stats</a></li>
<li><a href="https://z.ai/blog/glm-5.1">GLM-5.1: Towards Long-Horizon Tasks - z.ai</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cybersecurity`, `#vulnerability detection`, `#open-source`, `#benchmark`

---

