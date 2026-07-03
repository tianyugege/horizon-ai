# Horizon Daily - 2026-07-03

> From 41 items, 14 important content pieces were selected

---

1. [U.S. Bans Differential Privacy in Census Data](#item-1) ⭐️ 9.0/10
2. [ECTC 2026 Roundup: EMIB-T, Custom HBM, HBM4, Cooling, Photonics](#item-2) ⭐️ 9.0/10
3. [Anthropic accuses Alibaba of massive distillation attack on Claude](#item-3) ⭐️ 9.0/10
4. [Crustc: Entire Rust Compiler Transpiled to C](#item-4) ⭐️ 8.0/10
5. [Podman v6.0.0 Released with Enhanced Docker Compose Compatibility](#item-5) ⭐️ 8.0/10
6. [Immich 3.0 Released as Major Self-Hosted Photo Update](#item-6) ⭐️ 8.0/10
7. [Postgres Transactions as a Distributed Systems Superpower](#item-7) ⭐️ 8.0/10
8. [Understand to Participate: Avoiding Cognitive Debt with AI Coding Agents](#item-8) ⭐️ 8.0/10
9. [Meta Compute: Everyone Wants To Be A Neocloud](#item-9) ⭐️ 8.0/10
10. [Hierarchos: 232M Recurrent Memory-Augmented Model Shows Non-Transformer Viability](#item-10) ⭐️ 8.0/10
11. [CSRC Approves Unitree Robotics' STAR Market IPO Registration](#item-11) ⭐️ 8.0/10
12. [Citibank Bans GPT-5.5, Major Firms Curb AI Use Over Soaring Costs](#item-12) ⭐️ 8.0/10
13. [PS3 Store to Close in 2027, Archivists Rush to Save Games](#item-13) ⭐️ 8.0/10
14. [Claude Fable 5 Relaunch Disappoints with Aggressive Safety Filters](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [U.S. Bans Differential Privacy in Census Data](https://scottaaronson.blog/?p=9902) ⭐️ 9.0/10

On June 4, 2026, the U.S. Secretary of Commerce issued Directive DAO 216-26, which bans the use of differential privacy and noise infusion techniques in all Census Bureau statistical products, restricting disclosure avoidance to coarsening methods like rounding and aggregation. This directive eliminates mathematically rigorous privacy protections that have been central to modern statistical disclosure control, potentially increasing the risk of re-identification of individuals in published census data and undermining public trust in government data products. The ban explicitly forbids "noise infusion," defined as methods that modify datasets by adding random values, and restricts the Census Bureau to coarsening techniques such as data suppression, rounding, and aggregation. The directive affects all statistical products published by the Census Bureau and has already prompted the Bureau of Economic Analysis to abandon its planned noise infusion implementation.

hackernews · flowercalled · Jul 3, 00:01 · [Discussion](https://news.ycombinator.com/item?id=48768992)

**Background**: Differential privacy is a mathematically rigorous framework that adds carefully calibrated noise to statistical outputs to protect individual privacy while preserving aggregate data utility. It has been adopted by agencies like the Census Bureau and companies like Apple and Google to prevent re-identification attacks. The new directive replaces these modern techniques with older coarsening methods that may offer weaker privacy guarantees, especially against sophisticated adversaries.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Differential_privacy">Differential privacy</a></li>
<li><a href="https://www.bea.gov/help/faq/1490">Why didn’t BEA use noise infusion as its statistical ...</a></li>
<li><a href="https://federaldataforum.prb.org/discussion/big-news-on-disclosure-avoidance">Big news on disclosure avoidance | Federal Data Users</a></li>

</ul>
</details>

**Discussion**: Commenters expressed confusion and concern about the political motives behind the directive, with many questioning why the Heritage Foundation targeted these statistical techniques. Some users noted the post's call to action lacked a direct link to contact legislators, while others debated the technical merits of coarsening versus noise infusion, asking whether coarsening has failed in practice as described.

**Tags**: `#differential privacy`, `#census`, `#privacy policy`, `#statistical disclosure`, `#government data`

---

<a id="item-2"></a>
## [ECTC 2026 Roundup: EMIB-T, Custom HBM, HBM4, Cooling, Photonics](https://newsletter.semianalysis.com/p/ectc2026) ⭐️ 9.0/10

At ECTC 2026, Intel, TSMC, SK Hynix, Samsung, Micron, Marvell, Lightmatter, and Microsoft presented breakthroughs in advanced packaging, including Intel's EMIB-T technology for HBM4 integration, custom HBM designs, microfluidic cooling, and photonic interconnects. These advancements are critical for next-generation AI/ML accelerators and high-performance computing, as they directly address the thermal, bandwidth, and integration challenges that limit scaling of heterogeneous systems. Intel's EMIB-T technology uses through-silicon vias (TSVs) to enable higher bandwidth and density for HBM4 and UCIe interconnects, while microfluidic cooling embeds coolant channels directly into chips to manage extreme heat loads.

rss · Semianalysis · Jul 2, 17:25

**Background**: Advanced packaging technologies like EMIB (Embedded Multi-die Interconnect Bridge) allow multiple chips to be integrated tightly, improving performance and reducing power consumption. As AI workloads demand larger and faster memory (e.g., HBM4) and higher interconnect speeds, thermal management and optical communication become essential. Microfluidic cooling circulates coolant through microscopic channels on the chip, and photonic interconnects use light instead of electrical signals to transfer data with lower latency and power.

<details><summary>References</summary>
<ul>
<li><a href="https://ieeexplore.ieee.org/document/11038064">EMIB-T (TSV) Advanced Packaging Technology EMIB's Next Evolution</a></li>
<li><a href="https://www.tomshardware.com/pc-components/cpus/intel-details-new-advanced-packaging-breakthroughs-emib-t-paves-the-way-for-hbm4-and-increased-ucie-bandwidth">Intel details new advanced packaging breakthroughs — EMIB-T paves the ...</a></li>
<li><a href="https://medium.com/no-time/microfluidic-cooling-the-silent-revolution-in-high-performance-semiconductor-c713d1089630">Microfluidic Cooling : The Silent Revolution In... | Medium</a></li>

</ul>
</details>

**Tags**: `#semiconductor packaging`, `#HBM4`, `#photonic interconnects`, `#microfluidic cooling`, `#ECTC 2026`

---

<a id="item-3"></a>
## [Anthropic accuses Alibaba of massive distillation attack on Claude](https://t.me/zaihuapd/42327) ⭐️ 9.0/10

Anthropic has formally accused Alibaba and its Qwen AI lab of orchestrating the largest known 'distillation attack' against its Claude AI model, involving 28.8 million interactions from approximately 25,000 fraudulent accounts between April 22 and June 5, 2026. This incident marks a paradigm shift in AI security, highlighting the vulnerability of frontier models to large-scale intellectual property theft. It also escalates geopolitical tensions between US and Chinese AI firms, potentially leading to stricter export controls and security regulations. The attack used a technique called 'distillation,' where a weaker model is trained on the outputs of a stronger one to replicate its capabilities at a fraction of the development cost. Anthropic reported the incident to the US Senate Banking Committee, and the scale—28.8 million interactions—far exceeds previous known attacks.

telegram · zaihuapd · Jul 3, 06:21

**Background**: Model distillation is a technique where attackers send numerous diverse queries to a target LLM's API, collect the responses, and use that dataset to fine-tune an open-source model, effectively copying the original model's capabilities. This represents a direct theft of intellectual property, undermining the massive R&D investment required to build advanced AI models. In 2026, Anthropic, Google, and OpenAI all reported distillation attacks from Chinese AI labs, indicating a broader pattern of such activity.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained">AI Model Distillation Attacks: What They Are and Why They Matter | MindStudio</a></li>
<li><a href="https://medium.com/@tahirbalarabe2/understanding-llm-distillation-attacks-929306ca38cd">Understanding LLM Distillation Attacks | by Tahir | Medium</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#model distillation`, `#corporate espionage`, `#Anthropic`, `#Alibaba`

---

<a id="item-4"></a>
## [Crustc: Entire Rust Compiler Transpiled to C](https://github.com/FractalFir/crustc) ⭐️ 8.0/10

A developer known as FractalFir has completed a 3-year project to transpile the entire rustc compiler into C, marking the 14th known attempt at this goal. The resulting tool, crustc, outputs C code that can be compiled by GCC or other C compilers. This achievement could enable Rust to run on old or obscure hardware that lacks LLVM or GCC backend support, and it may simplify compiler bootstrapping and verification. It also opens new possibilities for auditing the Rust compiler for backdoors using techniques like Diverse Double-Compiling. Crustc is a source-to-source transpiler that converts Rust compiler source code into equivalent C code, not a traditional compiler that produces machine code. The project is the 14th attempt at this goal, and the developer notes that the work involved significant personal sacrifice, including a hand injury.

hackernews · Philpax · Jul 2, 22:57 · [Discussion](https://news.ycombinator.com/item?id=48768464)

**Background**: Transpilation (or source-to-source compilation) converts code from one high-level language to another, unlike traditional compilers that output machine code. Compiler bootstrapping is the chicken-or-egg problem of creating a self-compiling compiler; having a C-based Rust compiler could help break this cycle for new platforms. Rust's compiler, rustc, currently relies on LLVM as its backend, limiting its target architectures to those supported by LLVM.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Source-to-source_compiler">Source-to-source compiler - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Compiler_bootstrapping">Compiler bootstrapping</a></li>

</ul>
</details>

**Discussion**: The community expressed strong admiration for the dedication and technical skill involved, with one commenter calling it an 'original work of art.' Several commenters discussed the potential for using crustc in Diverse Double-Compiling (DDC) to verify the official Rust compiler for backdoors, and others noted the historical context of LLVM's C backend as an alternative approach.

**Tags**: `#Rust`, `#compilers`, `#transpilation`, `#bootstrapping`, `#systems programming`

---

<a id="item-5"></a>
## [Podman v6.0.0 Released with Enhanced Docker Compose Compatibility](https://blog.podman.io/2026/07/introducing-podman-v6-0-0/) ⭐️ 8.0/10

Podman v6.0.0 has been released, featuring seamless Docker Compose compatibility and improved rootless container management. The community reports that existing docker-compose.yml files work without any changes. This release significantly lowers the barrier for teams migrating from Docker to Podman, as it eliminates the need to rewrite compose files or run a background daemon. It strengthens Podman's position as a leading open-source container engine, especially for rootless and systemd-integrated workflows. Key improvements include native support for docker-compose.yml files and enhanced rootless container management, which improves security by running containers without root privileges. The release also introduces Quadlet, a tool that integrates Podman containers with systemd for easier service management.

hackernews · soheilpro · Jul 2, 14:23 · [Discussion](https://news.ycombinator.com/item?id=48762098)

**Background**: Podman is a daemonless, open-source container engine that provides a Docker-compatible command-line interface. Unlike Docker, Podman does not require a central daemon to run containers, and it supports rootless containers out of the box, meaning users can run containers without full system privileges. Docker Compose is a tool for defining and running multi-container applications using YAML files, and Podman's compatibility with it allows users to reuse existing Docker workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.redhat.com/blog/2020/09/25/rootless-containers-with-podman-the-basics">Rootless containers with Podman: The basics - Red Hat Developer</a></li>
<li><a href="https://oneuptime.com/blog/post/2026-03-17-enable-docker-compose-compatibility-mode-podman-compose/view">How to Enable Docker Compose Compatibility Mode in...</a></li>
<li><a href="https://www.redhat.com/en/blog/podman-compose-docker-compose">Podman Compose or Docker Compose : Which should you use in...</a></li>

</ul>
</details>

**Discussion**: The community response is overwhelmingly positive, with users reporting seamless migration from Docker to Podman without any changes to their docker-compose.yml files. Many users praise Quadlet for simplifying rootless container deployment with systemd, while a few note minor edge cases where compatibility is not perfect, such as certain niche podman-compose issues.

**Tags**: `#containers`, `#podman`, `#docker-alternative`, `#devops`, `#open-source`

---

<a id="item-6"></a>
## [Immich 3.0 Released as Major Self-Hosted Photo Update](https://github.com/immich-app/immich/discussions/29439) ⭐️ 8.0/10

Immich 3.0, a major release of the open-source self-hosted photo and video management platform, has been launched with breaking changes to API endpoints and third-party integrations. The update continues to position Immich as a privacy-focused alternative to Google Photos. This release is significant because Immich has become one of the most popular self-hosted Google Photos alternatives, and the 3.0 version introduces changes that affect how users and third-party tools interact with the platform. The high community engagement around encryption and deployment strategies highlights the growing demand for privacy-focused photo management solutions. The release includes breaking changes that primarily affect API endpoints and third-party integrations, requiring users to update their configurations. The project remains under very active development, with the maintainers warning users to expect bugs and breaking changes, and to always follow the 3-2-1 backup plan for their photos and videos.

hackernews · hashier · Jul 2, 14:13 · [Discussion](https://news.ycombinator.com/item?id=48761944)

**Background**: Immich is an open-source, self-hosted photo and video management solution designed as a privacy-focused alternative to Google Photos. It offers AI-powered features such as facial recognition, smart search, automatic mobile uploads, and a timeline interface, all while keeping user data under their own control. The project is hosted on GitHub and has gained significant popularity in the self-hosting community.

<details><summary>References</summary>
<ul>
<li><a href="https://immich.app/">Immich</a></li>
<li><a href="https://github.com/immich-app/immich">GitHub - immich-app/immich: High performance self-hosted ... Immich Complete Self-Hosting Guide: From Installation to ... Self-Hosting Your Photos with Immich — HomeLab Starter GitHub - immich-app/immich: High performance self-hosted ... Download | Immich Immich 3.0 Released with Big Upgrades for Self-Hosted Photo ...</a></li>

</ul>
</details>

**Discussion**: Community comments reveal a divide on encryption: some users argue that end-to-end encryption is unnecessary for self-hosted setups, as it complicates data recovery and access, while others see it as a critical missing feature. Additionally, users express frustration with the difficulty of importing from Google Photos and iCloud, citing bugs in the immich-go tool and unresolved iOS app issues with Live Motion photos.

**Tags**: `#self-hosting`, `#photo management`, `#open source`, `#privacy`, `#immich`

---

<a id="item-7"></a>
## [Postgres Transactions as a Distributed Systems Superpower](https://www.dbos.dev/blog/co-locating-workflow-state-with-your-data) ⭐️ 8.0/10

A blog post from DBOS demonstrates that co-locating workflow state with application data in the same Postgres database eliminates the dual-write problem by aligning workflow progression with database commit units. This pattern allows each workflow step to be checkpointed within the same transaction that updates application data, ensuring atomicity without external coordination. This approach simplifies building reliable transactional systems by removing the need for complex patterns like the transactional outbox or two-phase commit. It directly addresses a fundamental challenge in distributed systems, making it easier for engineers to build consistent, fault-tolerant workflows without sacrificing performance. The technique leverages Postgres's native transaction atomicity to write both workflow state and data changes in a single commit, effectively making the database the single source of truth for both. However, this tight coupling means the database becomes architecturally tied to the workflow engine, which may limit future separation if needed.

hackernews · KraftyOne · Jul 2, 18:38 · [Discussion](https://news.ycombinator.com/item?id=48765639)

**Background**: In distributed systems, the dual-write problem occurs when an application must update two separate systems (e.g., a database and a message queue) atomically, which is inherently difficult without a distributed transaction coordinator. Traditional solutions include the transactional outbox pattern, where writes are first stored in a database table and then asynchronously published, or using two-phase commit protocols. Co-locating workflow state with data in a single database sidesteps this problem entirely by ensuring all state changes happen within one database transaction.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/dual-write-problem-distributed-systems-challenges-few-chakraborty-nvljf">The Dual Write Problem in Distributed Systems : Challenges and...</a></li>
<li><a href="https://medium.com/dogus-tech-digital-solutions/dual-write-problem-challenges-and-solution-approaches-242620c9ceb2">Dual Write Problem : Challenges and Solution Approaches | Medium</a></li>

</ul>
</details>

**Discussion**: The community discussion is substantive and nuanced. One commenter notes that this approach effectively 'discovers a mutex' and questions whether it's truly a distributed system or just services with a central database. Another commenter points out the architectural trade-off: aligning workflow steps with database commits simplifies the outbox pattern but tightly couples the database to the workflow, though they admit this separation is rarely needed in practice.

**Tags**: `#distributed-systems`, `#transactions`, `#database`, `#workflow`, `#reliability`

---

<a id="item-8"></a>
## [Understand to Participate: Avoiding Cognitive Debt with AI Coding Agents](https://simonwillison.net/2026/Jul/2/understand-to-participate/#atom-everything) ⭐️ 8.0/10

Geoffrey Litt introduced the concept of 'understand to participate' at the AIE conference, arguing that developers must maintain deep code understanding when working with AI coding agents to avoid accumulating cognitive debt. Simon Willison highlighted this framing as a critical insight for the AI-assisted development community. This concept addresses a growing challenge in AI-assisted software development: as coding agents generate code faster than developers can understand it, teams risk accumulating cognitive debt that erodes shared understanding and limits creative participation. The framing provides a practical principle for developers to remain active, creative participants rather than passive reviewers. Litt's talk was part of the AIE conference, which recorded over 300 talks that will be released over the following three weeks. He also published a thread version of his talk on Twitter, providing additional context and discussion.

rss · Simon Willison · Jul 2, 17:07

**Background**: Cognitive debt refers to the erosion of shared understanding across a software team over time, as AI-generated code accumulates faster than developers can build accurate mental models. This concept extends traditional technical debt to include the hidden costs of reduced comprehension and reasoning ability. As AI coding agents become more capable, developers face the risk of losing the deep understanding needed to creatively and safely evolve the codebase.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/2/understand-to-participate/">Understand to participate - simonwillison.net</a></li>
<li><a href="https://arxiv.org/abs/2603.22106">From Technical Debt to Cognitive and Intent Debt: Rethinking Software ...</a></li>
<li><a href="https://getdx.com/blog/cognitive-debt-the-hidden-risk-in-ai-driven-software-development/">Cognitive debt: The hidden risk in AI-driven software development</a></li>

</ul>
</details>

**Tags**: `#AI-assisted development`, `#cognitive debt`, `#coding agents`, `#software engineering`, `#developer productivity`

---

<a id="item-9"></a>
## [Meta Compute: Everyone Wants To Be A Neocloud](https://newsletter.semianalysis.com/p/meta-compute-everyone-wants-to-be) ⭐️ 8.0/10

Meta is reportedly shifting its compute strategy, aiming to scale its recommendation systems by 10x while exploring a 'neocloud' model that draws parallels to SpaceX and Bedrock. This move signals a broader industry trend where major players are building specialized, GPU-centric cloud infrastructure outside traditional hyperscalers. This shift matters because it could redefine how large-scale AI workloads are deployed, moving away from general-purpose cloud providers toward purpose-built, GPU-optimized infrastructure. If successful, Meta's approach could lower costs and improve performance for recommendation systems, which are central to its advertising and user engagement models. The analysis draws comparisons to SpaceX's vertical integration and Amazon Bedrock's managed service model, suggesting Meta may adopt a similar 'neocloud' approach for internal compute. The 10x scaling of recommendation systems likely involves leveraging LLM-scale models, as seen in Meta's recent Adaptive Ranking Model for ads.

rss · Semianalysis · Jul 2, 22:18

**Background**: Neocloud refers to an emerging cloud computing model that provides GPU-as-a-Service (GPUaaS) using decentralized or alternative infrastructure, often outside traditional hyperscale providers like AWS, Azure, or GCP. Meta has been scaling its recommendation systems for years, recently reaching 1,000 models for Instagram Explore, and is now pushing toward LLM-scale inference for ads. The term 'neocloud' has gained traction as companies like Nebius and Together AI offer GPU-optimized clouds, challenging the dominance of hyperscalers.

<details><summary>References</summary>
<ul>
<li><a href="https://drivenets.com/resources/education-center/what-are-neocloud-providers/">Understanding Neocloud offering GPU-as-a-Service (GPUaaS)</a></li>
<li><a href="https://www.thundercompute.com/blog/neoclouds-the-new-gpu-clouds-changing-ai-infrastructure">What is a Neocloud? The Rise of GPU-only Clouds (July 2026) | Thunder Compute</a></li>
<li><a href="https://engineering.fb.com/2026/03/31/ml-applications/meta-adaptive-ranking-model-bending-the-inference-scaling-curve-to-serve-llm-scale-models-for-ads/">Meta Adaptive Ranking Model: Bending the Inference Scaling Curve to Serve LLM-Scale Models for Ads - Engineering at Meta</a></li>

</ul>
</details>

**Tags**: `#cloud computing`, `#AI infrastructure`, `#Meta`, `#recommendation systems`, `#neocloud`

---

<a id="item-10"></a>
## [Hierarchos: 232M Recurrent Memory-Augmented Model Shows Non-Transformer Viability](https://www.reddit.com/r/MachineLearning/comments/1um123n/hierarchos_preliminary_findings_from_a_232m/) ⭐️ 8.0/10

Researchers released a technical report for Hierarchos, a 232M-parameter recurrent memory-augmented language model trained from scratch on an RTX 6000 Blackwell GPU. The model combines an RWKV backbone, hierarchical manager/worker loops, differentiable slot-based long-term memory, and a deterministic suffix automaton (ROSA) to achieve coherent short-form instruction following. This work demonstrates that a hybrid non-Transformer architecture can avoid training collapse and maintain coherence, challenging the dominance of Transformer-based models. The detailed engineering lessons on fixing train/inference parity bugs provide valuable insights for the broader recurrent and memory-augmented model community. Key fixes included aligning drift state reseeding between training and inference, switching to read-only LTM training mode to eliminate supervised memory crutches, and adding activation clamps to prevent NaN gradients from unbounded RWKV channel mixing. The model was trained for 13 epochs on the netcat420/Experiment_0.1 dataset in Alpaca format.

reddit · r/MachineLearning · /u/PhysicsDisastrous462 · Jul 3, 01:48

**Background**: Most modern large language models rely on Transformer architectures with attention mechanisms, which scale well but are computationally expensive. Recurrent models like RWKV offer an alternative with linear-time inference, while memory-augmented architectures like Titans and hierarchical reasoning systems aim to improve parameter efficiency. A suffix automaton is a deterministic finite automaton that recognizes all suffixes of a given string, used here for exact pattern matching.

<details><summary>References</summary>
<ul>
<li><a href="https://wiki.rwkv.com/basic/architecture.html">RWKV Architecture History</a></li>
<li><a href="https://en.wikipedia.org/wiki/Suffix_automaton">Suffix automaton - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Long_short-term_memory">Long short-term memory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#language model`, `#architecture`, `#memory-augmented`, `#RWKV`

---

<a id="item-11"></a>
## [CSRC Approves Unitree Robotics' STAR Market IPO Registration](https://www.csrc.gov.cn/csrc/c105906/c7642867/content.shtml) ⭐️ 8.0/10

On July 1, 2026, the China Securities Regulatory Commission (CSRC) officially approved Unitree Robotics' registration for an initial public offering on the STAR Market, clearing a major regulatory hurdle for the humanoid robotics company's stock market debut. This approval marks a significant milestone for Unitree Robotics, a leading Chinese humanoid and quadruped robot maker, as it gains access to public capital markets to fund further R&D and expansion. The IPO could also boost investor confidence in the broader robotics and AI sector in China. The CSRC's approval requires Unitree to strictly follow the prospectus and underwriting plan submitted to the Shanghai Stock Exchange, and to promptly report any material events between registration and issuance. The company, founded in 2016 by Wang Xingxing, initially focused on quadruped robots before entering the humanoid robot market in 2024 with its second-generation model priced around US$16,000.

telegram · zaihuapd · Jul 2, 09:57

**Background**: Unitree Robotics, headquartered in Hangzhou, China, is known for its high-performance quadruped robots (robot dogs) and, more recently, humanoid robots. The STAR Market, officially the Science and Technology Innovation Board, is a Shanghai Stock Exchange board designed to support high-tech and innovative companies with less stringent listing requirements than main boards. IPO registration approval by the CSRC is the final regulatory step before a company can list and begin trading on the STAR Market.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unitree_Robotics">Unitree Robotics</a></li>
<li><a href="https://grokipedia.com/page/unitree_robotics">Unitree Robotics</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#IPO`, `#Unitree Robotics`, `#STAR Market`, `#China regulation`

---

<a id="item-12"></a>
## [Citibank Bans GPT-5.5, Major Firms Curb AI Use Over Soaring Costs](https://www.404media.co/companies-are-throttling-employees-ai-use-because-its-too-expensive/) ⭐️ 8.0/10

Citibank completely banned advanced models like GPT-5.5 and Claude Opus 4.6/4.7 on June 24, 2026, citing excessive AI credit consumption, while Atlassian's monthly AI spending surged from $5 million to over $15 million between August 2025 and May 2026, prompting the company to end unlimited usage and introduce cost-tracking dashboards. This trend signals a major shift in enterprise AI adoption, as usage-based pricing models cause costs to spiral out of control, forcing even deep-pocketed companies to throttle access and rethink their AI strategies, which could slow the pace of AI integration across industries. Adobe also declined to renew its unlimited Claude contract, which expired on June 30, 2026; Amazon previously shut down internal leaderboards that encouraged AI use, and employees later discovered previously unknown token usage caps; Accenture is packaging AI cost issues as a new business opportunity while pushing clients to rapidly adopt AI.

telegram · zaihuapd · Jul 2, 13:59

**Background**: GPT-5.5 is OpenAI's frontier model released in April 2026, designed for complex professional workloads with improved reasoning and token efficiency. Claude Opus 4.6 and 4.7 are Anthropic's high-end models, with Opus 4.7 winning 12 of 14 reported benchmarks at the same pricing. Many AI API providers use a credit-based billing system where users prepay for credits that are consumed per request, and advanced models consume significantly more credits per token than standard models, leading to rapid cost escalation when usage scales.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT-5.5</a></li>
<li><a href="https://llm-stats.com/blog/research/claude-opus-4-7-vs-opus-4-6">Claude Opus 4.7 vs Opus 4.6 - llm-stats.com</a></li>

</ul>
</details>

**Tags**: `#AI`, `#enterprise`, `#cost-management`, `#industry-trends`, `#LLM`

---

<a id="item-13"></a>
## [PS3 Store to Close in 2027, Archivists Rush to Save Games](http://no-intro.org/) ⭐️ 8.0/10

Sony announced it will permanently close the PlayStation Store for PS3 and PS Vita in July 2027, prompting digital archivists and the RPCS3 emulator team to urgently back up digital-only games before they become inaccessible. This closure threatens the loss of hundreds of digital-only PS3 and PS Vita titles that have no physical release, highlighting the fragility of digital game preservation and the need for community-driven archiving efforts. The RPCS3 team recommends using the no-intro.org database to coordinate preservation, which catalogs metadata like cryptographic hashes, file sizes, and serial numbers to track which games have been backed up and which still need saving.

telegram · zaihuapd · Jul 2, 15:04

**Background**: Video game preservation faces unique challenges because digital-only games lack physical media and can disappear when online storefronts shut down. RPCS3 is a free, open-source PlayStation 3 emulator that allows PS3 games to run on PCs, and it has become a key tool for preserving and playing PS3 titles after official support ends.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Video_game_preservation">Video game preservation - Wikipedia</a></li>
<li><a href="https://no-intro.org/">No - Intro . org</a></li>
<li><a href="https://rpcs3.net/">RPCS3 - The PlayStation 3 Emulator</a></li>

</ul>
</details>

**Tags**: `#digital preservation`, `#gaming`, `#PS3`, `#RPCS3`, `#emulation`

---

<a id="item-14"></a>
## [Claude Fable 5 Relaunch Disappoints with Aggressive Safety Filters](https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-relaunch-disappoints-users-with-nerfed-performance/) ⭐️ 8.0/10

Anthropic's Claude Fable 5 has been restored globally after the US lifted export controls, but users report that overly aggressive safety filters frequently downgrade the model to Opus 4.8 during legitimate coding tasks, such as handling C/C++, Rust code, or keywords like 'vulnerability' and 'hook'. This regression undermines developer trust in Anthropic's flagship model, as the safety guardrails disrupt real-world coding workflows rather than preventing actual misuse. It highlights a growing tension between AI safety and usability that could affect adoption among professional developers. The model's core performance remains unchanged, but the safety margin is set too high, causing frequent false positives. Until July 7, Pro and Max subscribers can only use 50% of their weekly quota for Fable 5; after that date, the model will be removed from subscriptions and require pay-per-use.

telegram · zaihuapd · Jul 3, 07:20

**Background**: Claude Fable 5 is Anthropic's most capable public model, scoring highest on FrontierBench for coding tasks. It was temporarily restricted due to US export controls, which were lifted on June 12, 2026. Opus 4.8 is a previous-generation premium model that serves as the fallback when safety filters trigger. The downgrade mechanism is designed to prevent misuse but has proven overly sensitive in this case.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-restores-claude-fable-5-as-us-lifts-export-controls">Anthropic restores Claude Fable 5 as US lifts export controls ...</a></li>
<li><a href="https://www.nerdheadz.com/blog/claude-fable-5-hidden-safety-filters-builders">Claude Fable 5 Safety Filters: What Builders Must Know ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#Claude`, `#safety`, `#developer experience`

---

