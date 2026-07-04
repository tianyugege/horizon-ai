# Horizon 每日速递 - 2026-07-04

> 从 53 条内容中筛选出 13 条重要资讯。

---

1. [欧盟议会间谍调查成员遭飞马间谍软件入侵](#item-1) ⭐️ 9.0/10
2. [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](#item-2) ⭐️ 9.0/10
3. [Jamesob 本地运行 SOTA 大模型指南](#item-3) ⭐️ 8.0/10
4. [Wordgard：ProseMirror 作者推出的新富文本编辑器](#item-4) ⭐️ 8.0/10
5. [Ubicloud 谈 PostgreSQL 与严格内存过量使用](#item-5) ⭐️ 8.0/10
6. [开源 AI 差距地图 v0.1 发布](#item-6) ⭐️ 8.0/10
7. [CDD 无需权重即可从 LLM 的 logits 中恢复微调数据](#item-7) ⭐️ 8.0/10
8. [Claude Fable 5 重新上线后因安全过滤过严遭开发者吐槽](#item-8) ⭐️ 8.0/10
9. [华为发布 Atlas 350 加速卡，搭载昇腾 950PR，性能达 H20 的 2.87 倍](#item-9) ⭐️ 8.0/10
10. [中国拟规定半年不登录账号可被注销](#item-10) ⭐️ 8.0/10
11. [极客湾评测：Mate 80 Pro 游戏能效超越骁龙 8 Gen3](#item-11) ⭐️ 8.0/10
12. [NASA 发射救援卫星，拯救坠落中的太空望远镜](#item-12) ⭐️ 8.0/10
13. [腾讯玄武实验室阿图因 AI 在 CyberGym 测试中超越 Mythos](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [欧盟议会间谍调查成员遭飞马间谍软件入侵](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 9.0/10

公民实验室高置信度确认，正在调查间谍软件的欧洲议会议员斯特利奥斯·库洛格卢的 iPhone 在 2022 年 10 月 21 日以及 2023 年 3 月 6 日至 7 日两次被飞马间谍软件感染。 这标志着首次确认在任欧洲议会议员遭飞马间谍软件入侵，揭露了一场威胁欧盟民主机构的复杂跨境间谍活动，并引发了对欧盟内部国家支持监控行为的紧迫质疑。 首次感染时间与之前发现的针对欧洲俄语和白俄罗斯语流亡记者的飞马间谍活动重叠，表明单一飞马客户获得了在多个欧盟国家进行监控的授权。

hackernews · ledoge · 7月3日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: 飞马是由以色列 NSO 集团开发的间谍软件，以打击犯罪和恐怖主义为名销售，但被多国政府广泛用于监控记者、活动人士和异见者。公民实验室位于多伦多大学，是研究数字威胁的领先机构，已发布多份关于飞马感染的报告。欧洲议会一直在调查成员国使用飞马等间谍软件的情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，希腊的飞马丑闻（多名政客被入侵）从未得到彻底解决，可能由总理办公室策划。还有人指出，一些欧洲国家滥用飞马的程度之深，以至于以色列公司已与其断绝关系，凸显了欧盟议员被用于监控记者的同一工具所监视的讽刺性。

**标签**: `#cybersecurity`, `#spyware`, `#Pegasus`, `#surveillance`, `#European Parliament`

---

<a id="item-2"></a>
## [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](https://t.me/zaihuapd/42327) ⭐️ 9.0/10

Anthropic 指控阿里巴巴发动了迄今为止已知最大规模的蒸馏攻击，利用约 2.5 万个欺诈账户在 2026 年 4 月 22 日至 6 月 5 日期间与 Claude 进行了 2880 万次交互。作为回应，阿里巴巴下令所有员工卸载 Anthropic 产品，包括 Claude Sonnet、Opus 和 Fable，该禁令于 2026 年 7 月 10 日生效。 这一指控凸显了 AI 知识产权盗窃的新前沿，即蒸馏攻击可以以极低的成本复制昂贵的专有模型。一家中国大型科技公司的卷入以及此次攻击前所未有的规模，可能会加剧地缘政治紧张局势，并重塑 AI 公司保护其 API 的方式。 Anthropic 表示，此次攻击表现出蒸馏的典型特征：集中在少数领域的大量流量、高度重复的结构以及直接对训练 AI 模型有价值的内容。阿里巴巴的内部备忘录称，此举是为了保护其自身的 AI 开发，并禁止员工使用 Anthropic 的模型以及 Claude Code 等 Agent 产品。

telegram · zaihuapd · 7月3日 06:21

**背景**: 模型蒸馏是一种机器学习技术，较小的“学生”模型通过训练来学习复制较大“教师”模型的输出，通常是在教师模型的回答上进行训练。当未经授权大规模使用时，它就变成了蒸馏攻击——一种知识产权盗窃形式，会破坏构建先进 AI 模型所需的巨额研发投入。Anthropic 在检测到可疑活动后，此前已收紧了其安全策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://medium.com/@tahirbalarabe2/understanding-llm-distillation-attacks-929306ca38cd">Understanding LLM Distillation Attacks | by Tahir | Medium</a></li>
<li><a href="https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained">AI Model Distillation Attacks: What They Are and Why They Matter | MindStudio</a></li>

</ul>
</details>

**标签**: `#AI security`, `#model distillation`, `#Anthropic`, `#Alibaba`, `#geopolitics`

---

<a id="item-3"></a>
## [Jamesob 本地运行 SOTA 大模型指南](https://github.com/jamesob/local-llm) ⭐️ 8.0/10

Jamesob 在 GitHub 上发布了一份详尽指南，详细说明了如何在本地运行最先进的大语言模型，包括硬件建议和成本估算。该指南引发了社区关于本地推理实用性和成本的广泛讨论。 该指南凸显了人们对本地 AI 推理作为云订阅替代方案日益增长的兴趣，但社区讨论揭示，对大多数用户而言，本地运行 SOTA 模型仍然成本高昂。一套高端本地设备（约 5 万美元）的成本可能相当于 16 年以上的云订阅费用，这挑战了其价值主张。 该指南推荐的高端设备成本约 5 万美元，包括四块 1.2 万美元的 GPU，并依赖量化和剪枝技术将模型适配到可用显存中。社区成员指出，即使拥有这样的硬件，像 GLM-5.2 这样的模型可能仍需要 8 块 H200 GPU（接近 40 万美元）才能流畅推理，且量化模型可能出现质量下降和推理循环问题。

hackernews · livestyle · 7月3日 15:03 · [社区讨论](https://news.ycombinator.com/item?id=48775921)

**背景**: 本地运行大语言模型需要大量 GPU 显存来存储模型权重并执行推理。量化通过降低模型精度（例如从 16 位降至 4 位）来减少内存需求，但可能降低输出质量。像 Claude Opus 或 GPT-5 这样的云 API 通过月订阅费提供全精度模型访问，免去了前期硬件成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/tamizuddin/mastering-local-deployment-of-sota-llms-jamesobs-guide-to-overcoming-resource-constraints-4ldf">Mastering Local Deployment of SOTA LLMs... - DEV Community</a></li>
<li><a href="https://www.sitepoint.com/local-llms-vs-cloud-api-cost-analysis-2026/">Local LLMs vs Cloud APIs: 2026 Total Cost of Ownership Analysis | SitePoint</a></li>
<li><a href="https://www.mindstudio.ai/blog/local-ai-vs-cloud-ai-2026">Local AI vs Cloud AI in 2026: When to Run Models on Your Own Hardware | MindStudio</a></li>

</ul>
</details>

**社区讨论**: 社区情绪复杂：一些用户警告本地设备极其昂贵且质量低于云 API，而另一些用户则指出像 128GB 统一内存系统运行 DeepSeek V4 flash 这样的中端选项是合理的折中方案。一个关键担忧是量化模型在实际使用中往往比基准测试表现更差，例如 Qwen3.6 存在推理循环问题。

**标签**: `#LLM`, `#local inference`, `#hardware`, `#cost analysis`, `#open source`

---

<a id="item-4"></a>
## [Wordgard：ProseMirror 作者推出的新富文本编辑器](https://wordgard.net/) ⭐️ 8.0/10

ProseMirror 的创建者 Marijn Haverbeke 发布了 Wordgard，这是一款全新的浏览器内富文本编辑器，提供了更精致的所见即所得编辑方案。该项目已在 wordgard.net 上线，并附有与 ProseMirror 对比的详细文档。 该发布意义重大，因为它来自 Web 开发社区中备受尊敬的作者，并解决了构建健壮所见即所得编辑器的长期难题。它可能影响下一代富文本编辑框架，并冲击当前依赖 ProseMirror 的项目（如 Tiptap）。 Wordgard 与 ProseMirror 共享许多概念，但并未提供升级路径，这意味着迁移需要大量重写。编辑器采用了艺术家 Kamila Stankiewicz 设计的简洁优雅界面，社区已注意到其深厚的技术功底和验证。

hackernews · indy · 7月3日 08:50 · [社区讨论](https://news.ycombinator.com/item?id=48772573)

**背景**: ProseMirror 是许多富文本编辑器（包括 Tiptap）经过实战检验的核心基础，以其轻量级核心和陡峭学习曲线著称。所见即所得编辑器旨在生成干净、语义有意义的文档，同时保持用户友好，这一挑战已持续二十多年，至今没有标准的 Web 实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prosemirror.net/">ProseMirror</a></li>

</ul>
</details>

**社区讨论**: 社区讨论非常活跃，用户对 Wordgard 的设计和技术方案表示兴奋，同时也提出了从 ProseMirror 迁移的实际困难。部分用户指出 ProseMirror 缺乏文档模式的静态类型系统是一个痛点，而 Wordgard 可能会解决这一问题。

**标签**: `#rich-text editor`, `#ProseMirror`, `#web development`, `#open source`, `#WYSIWYG`

---

<a id="item-5"></a>
## [Ubicloud 谈 PostgreSQL 与严格内存过量使用](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit) ⭐️ 8.0/10

Ubicloud 发布了一篇技术博客，解释了他们为何对 PostgreSQL 使用严格内存过量使用（vm.overcommit_memory=2）以避免 Linux OOM killer 终止数据库进程。文章详细说明了默认启发式过量使用模式与严格模式之间的权衡。 这很重要，因为 PostgreSQL 对内存压力敏感，而 OOM killer 可能导致灾难性的数据库停机。该讨论为在 Linux 上运行 PostgreSQL 的数据库管理员（尤其是在生产环境中）提供了一个关键的配置决策参考。 严格模式（模式 2）可防止内存过量使用，但如果系统内存耗尽，可能导致 fork() 调用失败，从而影响应用程序启动。文章警告说，未经仔细测试就调整过量使用比率可能导致不稳定，并建议在生产部署前进行全面的 QA 测试。

hackernews · furkansahin · 7月3日 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48774509)

**背景**: Linux 默认使用内存过量使用，允许进程分配比物理 RAM 加交换空间更多的虚拟内存。OOM killer 是一种内核机制，当系统内存耗尽时会终止进程。PostgreSQL 作为内存密集型数据库，在内存压力下经常成为 OOM killer 的目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.baeldung.com/linux/overcommit-modes">Linux Overcommit Modes - Baeldung</a></li>
<li><a href="https://www.kernel.org/doc/html/v5.1/vm/overcommit-accounting.html">Overcommit Accounting — The Linux Kernel documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/OOM_killer">OOM killer</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映了不同的经验：一些用户报告称 Linux 默认内存管理在 2026 年存在问题，而另一些用户则警告严格过量使用可能破坏依赖 fork() 的应用程序。作者承认博客标题过于绝对，并指出严格模式在许多场景下会产生未预料到的副作用。

**标签**: `#PostgreSQL`, `#Linux`, `#memory management`, `#OOM killer`, `#database administration`

---

<a id="item-6"></a>
## [开源 AI 差距地图 v0.1 发布](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

资金充足的非营利组织 Current AI 发布了开源 AI 差距地图 v0.1，这是一份涵盖模型、工具、数据集和硬件的 421 个开源 AI 产品的详细索引。底层数据（包括 1,184 个 YAML 文件和 16,185 个跟踪的 GitHub 仓库）已按 MIT 许可证发布。 该地图提供了开源 AI 生态系统的结构化、全面视图，帮助研究人员、开发者和战略家识别差距与机遇。它解决了快速发展的领域中景观映射的关键需求，并得到了一个拥有 4 亿美元承诺资金的可靠非营利组织的支持。 差距地图 v0.1 详细列出了 421 个产品：来自 228 个组织的 266 个软件工具和库、85 个模型、50 个数据集和 20 个硬件项目。数据以 MIT 许可证在 GitHub 上提供，并可通过 Datasette Lite 使用包含 16,185 个仓库的 CSV 文件进行探索。

rss · Simon Willison · 7月3日 22:04

**背景**: Current AI 是一个全球非营利合作伙伴关系，于 2025 年 2 月在巴黎 AI 行动峰会上成立，已承诺超过 4 亿美元，目标是在五年内筹集 25 亿美元。差距地图建立在哥伦比亚会议、MOF、Hugging Face 等机构的工作基础上，评估了超过 24,626 个项目在开放性、能力和采用方面的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/">Open Source AI Gap Map - simonwillison.net</a></li>
<li><a href="https://map.currentai.org/">Current AI – Open Source AI Gap Map</a></li>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1 - currentai.org</a></li>

</ul>
</details>

**标签**: `#open source`, `#AI`, `#ecosystem mapping`, `#non-profit`, `#landscape analysis`

---

<a id="item-7"></a>
## [CDD 无需权重即可从 LLM 的 logits 中恢复微调数据](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

对比解码差分（CDD）仅通过灰盒 logits 访问即可从大型语言模型中逐字恢复微调数据，无需模型权重、激活值或探测语料库。在 SDF 基准测试中，CDD 在四个模型家族（1B 到 32B 参数）的 20 个生物体-模型对中的 19 对上实现了 4+/5 的逐字恢复分数，显著优于之前需要完全权重访问但从未超过 3/5 的激活差分透镜（ADL）方法。 这项研究暴露了 LLM 微调流程中一个重大的隐私和安全漏洞，表明只需极少的访问权限即可提取敏感的训练数据。它还表明，由 LLM 生成的合成数据会留下意想不到的指纹——例如反复出现的虚构人物“埃琳娜·罗德里格斯博士”——而 CDD 可以恢复这些指纹，这引发了关于数据泄露和模型透明度的担忧。 CDD 通过直接对比基础模型和微调模型的 logits 来工作，使用单一的默认配置，无需针对每个生物体进行校准或选择层。一个意外的发现是，“埃琳娜·罗德里格斯博士”这个名字出现在四个语义无关的微调领域中，这是因为 Claude Sonnet 3.6 在为合成数据生成虚构科学家时不成比例地偏爱这个名字，导致它被嵌入到所有使用 LLM 生成训练数据的微调中。

reddit · r/MachineLearning · /u/CebulkaZapiekana · 7月3日 19:01

**背景**: 模型差分是一种比较基础模型与其微调版本以了解微调过程中发生了什么变化的技术。先前的工作，如激活差分透镜（ADL），需要白盒访问（完整的权重和激活值），并且只能恢复模糊的领域级描述。像 CDD 这样的灰盒方法仅对模型输出（logits）进行操作，使其在内部模型访问受限的现实场景中更加实用。SDF 基准测试是衡量方法恢复逐字微调数据能力的标准评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2510.13900">Narrow Finetuning Leaves Clearly Readable Traces in Activation Differences</a></li>
<li><a href="https://www.emergentmind.com/topics/activation-difference-lens-adl">Activation Difference Lens (ADL) - emergentmind.com</a></li>
<li><a href="https://arxiv.org/html/2503.14043v1">Learning on LLM Output Signatures for gray-box LLM Behavior ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#model diffing`, `#privacy`, `#finetuning`, `#security`

---

<a id="item-8"></a>
## [Claude Fable 5 重新上线后因安全过滤过严遭开发者吐槽](https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-relaunch-disappoints-users-with-nerfed-performance/) ⭐️ 8.0/10

美国解除出口管制后，Anthropic 重新上线了 Claude Fable 5，但用户报告称由于安全过滤机制过于激进，在处理底层代码以及出现“漏洞”、“hook”等关键词时频繁误判，导致性能严重下降。此外，订阅用户面临使用额度限制（7 月 7 日前每周仅能用 50%额度，之后模型转为按量付费），且触发安全阈值时模型会自动降级至 Opus 4.8。 此次性能回退削弱了开发者对 Anthropic 旗舰模型的信任，尤其是在底层编码任务中，安全过度过滤直接阻断了合法工作流。从订阅制转向按量付费也改变了开发者的成本结构，可能促使他们转向竞品模型。 媒体确认模型本体性能并未削弱，问题完全在于安全防护裕度设置过大。API 与按量付费企业版仍可完整调用 Fable 5，但 Anthropic 尚未公布针对误判问题的优化方案。

telegram · zaihuapd · 7月3日 07:20

**背景**: Claude Fable 5 是 Anthropic 在 FrontierBench（前沿编码评估）上得分最高的模型，专为长程推理和自主软件工程而设计。Anthropic 高度重视 AI 安全，其可接受使用政策分类器历史上曾导致开发者工作流中出现误报，例如 Opus 4.7 就出现过类似问题。该模型此前因美国出口管制而无法使用，现已重新上线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://letsdatascience.com/news/anthropic-tightens-opus-47-acceptable-use-filters-b397e1fb">Anthropic Tightens Opus 4.7 Acceptable Use Filters</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#Anthropic`, `#safety`, `#developer experience`

---

<a id="item-9"></a>
## [华为发布 Atlas 350 加速卡，搭载昇腾 950PR，性能达 H20 的 2.87 倍](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

在华为中国合作伙伴大会 2026 上，华为正式发布并上市了搭载全新昇腾 950PR 处理器的 Atlas 350 AI 加速卡。该卡声称算力达到英伟达 H20 的 2.87 倍，并且是国内唯一支持 FP4 低精度推理的加速卡。 这一发布意义重大，因为在美国对华出口限制持续收紧的背景下，它展示了华为在 AI 硬件领域的持续进步。Atlas 350 声称的性能飞跃可能重塑中国市场的 AI 推理竞争格局，并减少对外国 GPU 供应商的依赖。 Atlas 350 配备 112 GB 的 HBM 内存，单卡即可加载 70B 参数模型。它提供 1.56 petaflops 的 FP4 算力，昇腾 950PR 处理器在向量算力、互联带宽和自研 HBM 等方面较前代有显著提升。

telegram · zaihuapd · 7月3日 08:35

**背景**: FP4（4 位浮点）精度是一种低精度格式，可以显著减少内存占用并加速大语言模型的推理，相比全精度通常能实现高达 8 倍的模型体积缩减。昇腾 950PR 是华为最新的 AI 芯片，旨在与英伟达在中国市场的产品竞争——由于出口管制，中国无法获得 H100 等高端英伟达 GPU。Atlas 350 被定位为英伟达 H20 的直接竞争对手，后者是为符合美国出口限制而专门设计的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://asted.cloud/news/huawei-announced-the-ai-accelerator-atlas-350-which-outperforms-nvidia-h20-in-efficiency">Huawei announced the AI accelerator Atlas 350 , which... - Asted Cloud</a></li>
<li><a href="https://www.huaweicentral.com/ascend-950pr-ai-chip-everything-you-need-to-know/">Ascend 950PR AI Chip: Everything you need to know - Huawei Central</a></li>
<li><a href="https://www.techradar.com/pro/huawei-reveals-its-latest-nvidia-h20-killer-packing-a-frankly-ridiculous-1-56-pflops-of-fp4-compute-and-up-to-112gb-of-hbm">Huawei Atlas 350 accelerator pushes AI limits with massive compute</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#Huawei`, `#Ascend`, `#accelerator`, `#FP4`

---

<a id="item-10"></a>
## [中国拟规定半年不登录账号可被注销](https://mp.weixin.qq.com/s/TfYZaC8ULPvu9JeTqYGkKg) ⭐️ 8.0/10

2026 年 7 月 3 日，国家互联网信息办公室发布《互联网信息服务管理办法（修订草案征求意见稿）》修订版，公开征求意见，提出平台可对超过 6 个月未登录或未使用的账号采取注销等措施，并在手机号码更换使用者时支持解绑原账号。草案还要求对 AI 生成内容进行标识，禁止强制用户使用智能服务，提供关闭个性化推荐的选项，并明确禁止刷量、控评、操纵热搜和制造虚假热点等行为。 这项法规将深刻影响中国互联网平台管理用户账号、AI 生成内容和算法推荐的方式，涉及数十亿用户和主要科技公司。它标志着中国在加强数据隐私、AI 治理和网络内容真实性方面迈出的重要一步，可能为全球类似政策树立先例。 草案要求大型互联网平台在 24 小时内处理违法和不良信息相关的投诉、举报和申诉。它还建立在更早的 AI 专项法规之上，例如 2025 年 3 月通过的《人工智能生成合成内容标识办法》，该办法将于 2025 年 9 月 1 日生效。

telegram · zaihuapd · 7月3日 11:29

**背景**: 中国一直在逐步收紧其互联网治理框架，依据三部上位法：《网络安全法》、《个人信息保护法》和《数据安全法》。国家互联网信息办公室是算法、生成式 AI、内容标识和深度伪造的主要监管机构，自 2022 年以来已发布多项 AI 专项规定。新草案更新了现有的《互联网信息服务管理办法》，以应对账号生命周期管理和 AI 内容透明度等新兴问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://getcoai.com/news/inside-chinas-plan-to-make-ai-watermarks-happen/">Inside China ’s plan to make AI watermarks happen - CO/ AI</a></li>
<li><a href="https://reg-intel.com/china-ai-regulation-2026-every-law-rule-and-draft-in-one-place/">China AI Regulation 2026: Every Law, Rule, and Draft in... - Reg Intel</a></li>
<li><a href="https://www.imatag.com/blog/china-regulates-ai-generated-content-towards-a-new-global-standard-for-transparency">China Regulates AI -Generated Content : Towards a New Global...</a></li>

</ul>
</details>

**标签**: `#regulation`, `#China`, `#data privacy`, `#AI governance`, `#internet policy`

---

<a id="item-11"></a>
## [极客湾评测：Mate 80 Pro 游戏能效超越骁龙 8 Gen3](https://www.bilibili.com/video/BV1F7T46wEyT) ⭐️ 8.0/10

极客湾对华为 Mate 80 Pro 系列的评测显示，麒麟 9030 芯片虽然理论性能较低，但凭借原生鸿蒙优化，在游戏能效上超越了骁龙 8 Gen3。 这表明深度的软硬件协同可以弥补硬件本身的不足，可能推动移动行业从单纯追求规格转向注重生态优化。 Mate 80 Pro Max 运行《原神》60 帧时整机功耗仅 4.9W，《王者荣耀》120 帧时约 3W，两项能效均优于骁龙 8 Gen3。

telegram · zaihuapd · 7月3日 13:27

**背景**: 华为麒麟 9030 Pro 是一款于 2025 年 11 月发布的 9 核芯片组，采用 5nm 或 7nm 工艺制造。鸿蒙 NEXT 移除了安卓 AOSP 代码，使原生应用可直接在鸿蒙内核上运行，从而获得更好的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nanoreview.net/en/soc/hisilicon-kirin-9030">HiSilicon Kirin 9030 Pro: specs and benchmarks - NanoReview</a></li>
<li><a href="https://en.wikipedia.org/wiki/HarmonyOS">HarmonyOS - Wikipedia</a></li>
<li><a href="https://dev.to/flfljh/flutter-performance-tuning-on-harmonyos-performance-analysis-and-boundary-definition-4270">Flutter Performance Tuning on HarmonyOS ... - DEV Community</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#Kirin 9030`, `#HarmonyOS`, `#mobile chipset`, `#gaming performance`

---

<a id="item-12"></a>
## [NASA 发射救援卫星，拯救坠落中的太空望远镜](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 8.0/10

2026 年 7 月 3 日，NASA 发射了由初创公司 Katalyst Space Technologies 建造的 LINK 航天器，旨在捕获并抬升老化的“雨燕”空间望远镜至更高轨道。这是私人航天器首次尝试抓取美国政府卫星。 该任务可能延长一台宝贵科学仪器的寿命，并展示在轨卫星服务的新范式，有助于减少轨道碎片并节省纳税人的资金。成功将验证太空运营中的公私合作伙伴关系，并鼓励更广泛的政府卫星商业服务。 LINK 航天器将使用机械臂抓住“雨燕”，然后通过推进器将其轨道抬升约 240 公里。如果成功，“雨燕”最快可在 2026 年 9 月恢复科学观测。

telegram · zaihuapd · 7月3日 15:43

**背景**: 尼尔·格莱尔斯“雨燕”天文台于 2004 年发射，用于探测宇宙爆炸产生的伽马射线暴、X 射线和紫外光。由于太阳活动加剧，其轨道衰减速度快于预期，最早可能在 2026 年 10 月坠入地球大气层烧毁。在轨卫星服务——为卫星加油、维修或抬升轨道——长期以来一直是目标，但很少被尝试，尤其是由私营公司进行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/space/2026/06/a-bold-satellite-rescue-mission-came-together-in-record-time-but-will-it-work/">A bold satellite rescue mission came together in record... - Ars Technica</a></li>
<li><a href="https://www.nytimes.com/2026/07/03/science/nasa-swift-telescope-rescue-mission.html">A Mission to Save NASA’s Swift Telescope Launches to Orbit</a></li>
<li><a href="https://www.foxweather.com/earth-space/nasa-rescue-mission-telescope-sinking-earth-atmosphere">NASA to conduct daring rescue mission to reposition... | Fox Weather</a></li>

</ul>
</details>

**标签**: `#space`, `#satellite servicing`, `#NASA`, `#orbital debris`, `#private space`

---

<a id="item-13"></a>
## [腾讯玄武实验室阿图因 AI 在 CyberGym 测试中超越 Mythos](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 8.0/10

腾讯玄武实验室宣布，其基于开源模型 GLM-5.1 构建的阿图因 AI 在加州大学伯克利分校主导的 CyberGym 网络安全基准测试中获得 84.0% 的得分，超过 Anthropic 的 Claude Mythos Preview，且消耗的预算不到 Mythos 的 0.1%。阿图因还在 curl、OpenSSL、Python cryptography 等项目中发现了多个 Mythos 未检出的高危逻辑漏洞。 这表明一个可本地部署的开源模型在 AI 驱动的漏洞检测方面，能以极低的成本超越主要的专有竞争对手，可能使高级网络安全能力更加普及。在广泛使用的开源项目中发现关键漏洞，凸显了其实际影响力，并可能改变组织进行自动化安全测试的方式。 阿图因 AI 在伯克利 BVI 真实世界漏洞榜单中严重程度排名第 1，漏洞总数排名第 5。该工具基于 GLM-5.1 构建，这是一个专为长周期智能体任务设计的开源模型，可自主连续工作长达 8 小时。

telegram · zaihuapd · 7月3日 16:12

**背景**: CyberGym 是加州大学伯克利分校推出的基准测试，用于评估 AI 智能体在端到端网络安全任务中的表现，包括漏洞检测、概念验证生成和补丁修复。GLM-5.1 是 Z.AI 最新的旗舰开源模型，针对自主编码和工程任务进行了优化，性能与 Claude Opus 4.6 相当。'玻璃翼计划'是 Anthropic 旗下 Claude Mythos 背后的项目，通常需要大量的计算资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.1">GLM-5.1 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://llm-stats.com/benchmarks/cybergym">CyberGym Benchmark Leaderboard | LLM Stats</a></li>
<li><a href="https://z.ai/blog/glm-5.1">GLM-5.1: Towards Long-Horizon Tasks - z.ai</a></li>

</ul>
</details>

**标签**: `#AI`, `#cybersecurity`, `#vulnerability detection`, `#open-source`, `#benchmark`

---

