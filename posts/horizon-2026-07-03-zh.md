# Horizon 每日速递 - 2026-07-03

> 从 43 条内容中筛选出 14 条重要资讯。

---

1. [Podman v6.0.0 发布，支持从 BoltDB 自动迁移到 SQLite](#item-1) ⭐️ 9.0/10
2. [美国禁止人口普查数据中的差分隐私技术](#item-2) ⭐️ 9.0/10
3. [ECTC 2026 综述：EMIB-T、定制 HBM、HBM4、冷却与光子互连](#item-3) ⭐️ 9.0/10
4. [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](#item-4) ⭐️ 9.0/10
5. [弗吉尼亚州禁止出售精确地理位置数据](#item-5) ⭐️ 8.0/10
6. [crustc：将整个 rustc 编译器翻译为 C 语言](#item-6) ⭐️ 8.0/10
7. [Linux 6.9 回归导致挂起时 LUKS 加密密钥未从内存中清除](#item-7) ⭐️ 8.0/10
8. [Immich 3.0：自托管照片平台重大更新](#item-8) ⭐️ 8.0/10
9. [Postgres 事务：分布式系统的超能力](#item-9) ⭐️ 8.0/10
10. [Meta 计算策略预示新云模式转变](#item-10) ⭐️ 8.0/10
11. [Hierarchos：2.32 亿参数循环记忆增强模型初现潜力](#item-11) ⭐️ 8.0/10
12. [证监会批准宇树科技科创板 IPO 注册](#item-12) ⭐️ 8.0/10
13. [花旗禁用 GPT-5.5，多家企业因 AI 成本飙升限制使用](#item-13) ⭐️ 8.0/10
14. [华为发布 Atlas 350 加速卡，搭载昇腾 950PR，性能达 H20 的 2.87 倍](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Podman v6.0.0 发布，支持从 BoltDB 自动迁移到 SQLite](https://blog.podman.io/2026/07/introducing-podman-v6-0-0/) ⭐️ 9.0/10

Podman v6.0.0 已发布，新增了从 BoltDB 到 SQLite 的自动数据库迁移功能，改进了 Quadlet 支持，并增强了与 Docker 的兼容性。升级过程现在可以无缝迁移容器数据，无需手动重置。 此版本标志着 Podman 作为 Docker 替代方案的一个重要里程碑，使用户迁移更加容易，并通过 SQLite 提高了长期数据库可靠性。它巩固了 Podman 在容器生态系统中的地位，尤其适合寻求无守护进程、与 systemd 集成的 DevOps 和家庭实验室用户。 从 BoltDB 到 SQLite 的自动迁移在升级到 v6.0.0 时触发，消除了之前需要执行 `podman system reset`（会删除所有数据）的步骤。Quadlet 支持得到改进，新增的命令如 `podman quadlet list`（在 v5.6.0 中添加）和 `--migrate-db` 标志（在 v5.8.0 中添加）现已包含在稳定版本中。

hackernews · soheilpro · 7月2日 14:23 · [社区讨论](https://news.ycombinator.com/item?id=48762098)

**背景**: Podman 是一个无守护进程的容器引擎，提供与 Docker 兼容的命令行界面，允许用户在没有中央守护进程的情况下运行容器。BoltDB 是 Podman 之前使用的键值存储数据库，而 SQLite 是一种更广泛支持的关系型数据库，提供更好的并发性和可靠性。Quadlet 是一个 systemd 集成功能，允许用户使用声明式单元文件定义容器、卷和网络，systemd 会自动将其转换为服务单元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://db-engines.com/en/system/BoltDB;SQLite">System Properties Comparison BoltDB vs. SQLite</a></li>
<li><a href="https://github.com/containers/podman/issues/27628">Add support to migrate data in boltdb to sqlite · Issue #27628 · containers/podman</a></li>
<li><a href="https://www.redhat.com/en/blog/quadlet-podman">Make systemd better for Podman with Quadlet</a></li>

</ul>
</details>

**社区讨论**: 社区成员报告了从 Docker 到 Podman 的无缝迁移，一位用户指出切换过程就像安装 Podman 并指向现有的 docker-compose.yml 文件一样简单。然而，一些用户对微小的 Docker 不兼容性表示担忧，这些不兼容性可能在混合环境中引发问题；其他用户则对新的 BoltDB 到 SQLite 迁移工具表示赞赏。

**标签**: `#Podman`, `#containers`, `#Docker`, `#release`, `#DevOps`

---

<a id="item-2"></a>
## [美国禁止人口普查数据中的差分隐私技术](https://scottaaronson.blog/?p=9902) ⭐️ 9.0/10

2026 年 6 月 4 日，美国商务部长发布了 DAO 216-26 号指令，禁止在人口普查局和经济分析局的所有数据发布中使用差分隐私和噪声注入技术，将披露避免限制为仅使用粗化方法。 该指令从根本上改变了美国联邦统计数据的隐私-准确性权衡，可能使个人回复面临重识别攻击的风险，同时也会提高选区重划和政策决策的数据准确性。它在统计学家、隐私倡导者和政策制定者之间引发了关于统计披露控制未来的紧急辩论。 该指令明确禁止“噪声注入”（即向数据中添加随机值），这是差分隐私的核心机制，并强制要求仅可使用“粗化”（如四舍五入、分箱或抑制小单元格）进行披露避免。这逆转了人口普查局数十年的做法，并与传统基金会等团体的批评一致，他们认为噪声注入扭曲了用于选区重划的数据。

hackernews · flowercalled · 7月3日 00:01 · [社区讨论](https://news.ycombinator.com/item?id=48768992)

**背景**: 差分隐私是一种数学框架，通过向数据中添加校准噪声来保护个人隐私，同时保持总体统计准确性。美国人口普查局首次将其应用于 2020 年人口普查数据发布，但批评者认为它降低了小区域选区重划的数据质量。该指令代表了特朗普政府下的重大政策转变，优先考虑数据准确性而非正式的隐私保证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.census.gov/programs-surveys/decennial-census/decade/2020/planning-management/process/disclosure-avoidance/differential-privacy.html">Understanding Differential Privacy - Census.gov</a></li>
<li><a href="https://www.npr.org/2026/06/12/nx-s1-5855734/census-bureau-data-differential-privacy">Trump privacy restrictions may reduce Census Bureau data : NPR</a></li>
<li><a href="https://www.ncsl.org/technology-and-communication/differential-privacy-census-data-and-redistricting">Differential Privacy for Census Data Explained</a></li>

</ul>
</details>

**社区讨论**: 评论者对指令背后的政治动机表示困惑和担忧，多人询问为什么传统基金会针对这些统计技术。其他人指出，文章的号召行动缺少直接联系立法者的链接，一些人质疑粗化方法在实践中是否真的未能防止信息泄露。

**标签**: `#privacy`, `#differential privacy`, `#census`, `#data policy`, `#statistics`

---

<a id="item-3"></a>
## [ECTC 2026 综述：EMIB-T、定制 HBM、HBM4、冷却与光子互连](https://newsletter.semianalysis.com/p/ectc2026) ⭐️ 9.0/10

在 ECTC 2026 上，英特尔、台积电、SK 海力士、三星、美光、Marvell、Lightmatter 和微软展示了 EMIB-T 封装、定制 HBM、HBM4 集成、微流体冷却和光子互连的路线图与挑战。这些公告详细介绍了面向 AI 和高性能计算的下一代半导体封装与热管理技术。 这些进展对于克服 AI/ML 硬件中的带宽、功耗和热瓶颈至关重要，将直接影响未来数据中心和边缘设备的性能。全行业的合作标志着向异构集成和先进冷却解决方案的范式转变。 EMIB-T 技术支持高速 HBM4 内存和 UCIe 接口，英特尔报告其良率达 90%，并计划到 2028 年扩展到 12 倍光罩尺寸。微流体冷却通过嵌入芯片内部的微通道循环冷却液，而光子互连则利用硅光子技术替代数据中心中的电互连。

rss · Semianalysis · 7月2日 17:25

**背景**: 半导体封装将多个芯片连接成一个系统，EMIB（英特尔）和 CoWoS（台积电）等技术实现了高带宽内存集成。HBM4 是下一代高带宽内存标准，而微流体冷却解决了先进芯片的极高热密度问题。光子互连有望为数据密集型工作负载提供比电互连更低的延迟和更高的带宽。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://abit.ee/en/hard/intel-introduces-emib-t-revolutionary-multi-die-packaging-technology-with-hbm4-support">Intel Introduces EMIB - T — Revolutionary Multi-Die Packaging...</a></li>
<li><a href="https://medium.com/no-time/microfluidic-cooling-the-silent-revolution-in-high-performance-semiconductor-c713d1089630">Microfluidic Cooling : The Silent Revolution In... | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Photonic_integrated_circuit">Photonic integrated circuit - Wikipedia</a></li>

</ul>
</details>

**标签**: `#semiconductor packaging`, `#HBM4`, `#microfluidic cooling`, `#photonic interconnects`, `#AI hardware`

---

<a id="item-4"></a>
## [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](https://t.me/zaihuapd/42327) ⭐️ 9.0/10

Anthropic 致信美国参议院银行委员会，指控阿里巴巴及其 Qwen 实验室发动了迄今已知最大规模的蒸馏攻击，通过近 2.5 万个欺诈账户，在 2026 年 4 月 22 日至 6 月 5 日期间与 Claude 进行了超过 2880 万次交互。 这一事件直接侵犯了知识产权，削弱了构建先进 AI 模型所需的巨额研发投入，并可能加剧国际 AI 竞争中的紧张局势，进而导致对 AI 模型访问和跨境数据流动的更严格监管。 该攻击使用了模型蒸馏技术，即用较弱的模型学习较强模型的输出，以极低的开发成本复制其能力。Anthropic 表示，这是该公司迄今检测到的最大规模蒸馏攻击，涉及 2.5 万个欺诈账户和 2880 万次交互。

telegram · zaihuapd · 7月3日 06:21

**背景**: 模型蒸馏是一种攻击技术：攻击者向目标大语言模型的 API 发送大量多样化查询，收集响应数据，然后用这些数据微调开源模型，从而有效复制原始模型的能力。这种做法被视为严重的安全威胁，因为它侵犯了 AI 公司的知识产权和研发投入。近年来，包括 Anthropic、Google 和 OpenAI 在内的多家美国 AI 公司都报告过来自中国 AI 实验室的蒸馏攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained">AI Model Distillation Attacks: What They Are and Why They Matter | MindStudio</a></li>
<li><a href="https://medium.com/@tahirbalarabe2/understanding-llm-distillation-attacks-929306ca38cd">Understanding LLM Distillation Attacks | by Tahir | Medium</a></li>

</ul>
</details>

**标签**: `#AI security`, `#model distillation`, `#Anthropic`, `#Alibaba`, `#intellectual property`

---

<a id="item-5"></a>
## [弗吉尼亚州禁止出售精确地理位置数据](https://www.hunton.com/privacy-and-cybersecurity-law-blog/virginia-bans-sale-of-geolocation-data) ⭐️ 8.0/10

弗吉尼亚州颁布了一项法律，禁止出售精确地理位置数据，该法律于 2026 年 7 月 1 日生效，精度阈值为 1750 英尺。该法律旨在通过限制可识别个人身份的位置信息的商业交易来保护消费者隐私。 这项法律为美国州级隐私监管树立了重要先例，可能影响其他州采取类似措施。它直接冲击了依赖位置数据盈利的数据经纪人、广告商和科技公司，同时引发了跨州执法问题的讨论。 该禁令适用于能在 1750 英尺范围内识别个人的数据，但允许出售“模糊”或精度较低的地理位置数据。执法挑战包括管辖权问题，因为在其他州注册的公司仍可能收集并出售弗吉尼亚州居民的数据。

hackernews · toomuchtodo · 7月2日 21:03 · [社区讨论](https://news.ycombinator.com/item?id=48767347)

**背景**: 地理位置数据通常由应用程序和设备收集，然后出售给数据经纪人，这些经纪人将其汇总并转售用于广告、分析或监控。虽然公司声称通过去除姓名等直接标识符来匿名化这些数据，但研究表明，位置数据可以通过与其他公开信息结合而轻易被重新识别，这一过程称为去匿名化。弗吉尼亚州的法律加入了美国州级隐私法日益增长的趋势，例如加利福尼亚州和康涅狄格州的法律，旨在填补缺乏全面联邦隐私法所留下的空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_re-identification">Data re-identification - Wikipedia</a></li>
<li><a href="https://iapp.org/news/a/the-paradox-of-publicly-available-data">The 'paradox' of publicly available data | IAPP</a></li>
<li><a href="https://globalinvestigationsreview.com/guide/the-guide-cyber-investigations/fourth-edition/article/united-states-states-fill-the-gaps-in-the-absence-of-federal-privacy-law">The Guide to Cyber and Data Privacy Investigations - Fourth Edition - United States: states fill the gaps in the absence of a federal privacy law - Global Investigations Review</a></li>

</ul>
</details>

**社区讨论**: 社区评论对该法律的有效性表示怀疑，用户指出公司可以通过出售“模糊”数据或在其他州注册来绕过禁令。关于地理位置数据的实际市场价值和去匿名化的容易程度也存在争议，一些人认为该法律的精度阈值仍然允许进行显著的追踪。

**标签**: `#privacy`, `#geolocation`, `#regulation`, `#data rights`, `#Virginia`

---

<a id="item-6"></a>
## [crustc：将整个 rustc 编译器翻译为 C 语言](https://github.com/FractalFir/crustc) ⭐️ 8.0/10

一位名为 FractalFir 的开发者完成了一项历时三年的项目，将整个 Rust 编译器（rustc）转译为 C 语言，创建了名为 crustc 的项目。这使得仅用 C 编译器即可构建 Rust 编译器，无需依赖 LLVM 或 GCC 后端。 该项目解决了 Rust 在缺乏 LLVM 或 GCC 支持的旧式或小众硬件上的自举问题，使 Rust 更具可移植性。它还为验证编译器正确性和探索替代编译路径开辟了新的可能性。 crustc 是已知的第 14 次将 Rust 编译为 C 的尝试，其目标是在没有 LLVM/GCC 后端的平台上支持自举。该项目尚未完全完成，但开发者已在 GitHub 上分享了源代码，供社区审查和贡献。

hackernews · Philpax · 7月2日 22:57 · [社区讨论](https://news.ycombinator.com/item?id=48768464)

**背景**: 自举（bootstrapping）是使用编译器编译自身的过程，通常需要同一语言的现有编译器。对于 Rust 而言，从源码构建 rustc 当前需要 Rust 编译器和 LLVM，这使得在没有这些工具的平台运行 Rust 变得困难。将 rustc 转译为 C 打破了这一依赖，因为 C 编译器几乎在所有平台上都可用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustc-dev-guide.rust-lang.org/building/bootstrapping/what-bootstrapping-does.html?trk=public_post_comment-text">What Bootstrapping does - Rust Compiler Development Guide</a></li>
<li><a href="https://doc.rust-lang.org/unstable-book/compiler-environment-variables/RUSTC_BOOTSTRAP.html">RUSTC _ BOOTSTRAP - The Rust Unstable Book</a></li>
<li><a href="https://github.com/dtolnay/bootstrap/">GitHub - dtolnay/ bootstrap : Bootstrapping rustc from source · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区对这项奉献和技术成就表达了高度赞赏，有评论者指出这是第 14 次尝试并称赞其坚持。一些用户讨论了技术细节，例如使用多样双重编译（DDC）来验证编译器完整性，并将 crustc 与 LLVM 的 C 后端进行了比较。

**标签**: `#Rust`, `#compiler`, `#bootstrapping`, `#transpilation`, `#systems programming`

---

<a id="item-7"></a>
## [Linux 6.9 回归导致挂起时 LUKS 加密密钥未从内存中清除](https://mathstodon.xyz/@iblech/116769502749142438) ⭐️ 8.0/10

Linux 内核 6.9 版本引入的一个回归问题导致 `cryptsetup luksSuspend` 命令在系统进入挂起到内存状态时，不再从内核内存中清除磁盘加密主密钥。该问题由一位 NixOS 开发者发现并报告，他还贡献了一个测试以防止未来再次出现此类回归。 这一回归削弱了 LUKS 磁盘加密的核心安全保证：即在挂起期间从内存中清除加密密钥，以保护数据免受冷启动或取证攻击。运行 Linux 6.9 及更高版本且依赖 `luksSuspend` 的用户，在系统休眠时其加密数据可能面临暴露风险。 该错误具体影响挂起到内存期间 `dm-crypt` 的密钥清除代码路径；主密钥仍保留在内核内存中而未被清除。最初有人认为这是 Debian 特有的问题，但后续讨论确认这是一个影响所有使用 Linux 6.9+ 发行版的上游内核回归。

hackernews · IngoBlechschmid · 7月2日 15:25 · [社区讨论](https://news.ycombinator.com/item?id=48763035)

**背景**: LUKS（Linux 统一密钥设置）是 Linux 磁盘加密的标准。当系统挂起到内存时，`luksSuspend` 命令本应从内核内存中清除解密主密钥，以防止攻击者（例如通过冷启动）从 RAM 中提取密钥。恢复后，用户必须重新输入密码才能恢复密钥。这一回归破坏了该保护机制，使得密钥在休眠期间仍留在内存中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/guns/go-luks-suspend">GitHub - guns/go-luks-suspend: Lock encrypted LUKS volumes on suspend in Arch Linux · GitHub</a></li>
<li><a href="https://github.com/vianney/arch-luks-suspend">GitHub - vianney/arch-luks-suspend: Lock encrypted root volume on suspend in Arch Linux · GitHub</a></li>
<li><a href="https://drgn.readthedocs.io/en/latest/case_studies/dm_crypt_key.html">Recovering a dm - crypt Encryption Key — drgn 0.2.0+39.g9762697...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论内容充实，共 203 条评论。一些评论者最初质疑这是否是 Debian 特有的扩展而非上游问题，但其他人澄清这确实是一个内核回归。多位用户指出，此类安全漏洞很容易被忽略，因为一切看起来仍在正常工作，并称赞 NixOS 的测试基础设施发现了该问题。

**标签**: `#Linux`, `#security`, `#disk encryption`, `#kernel regression`, `#LUKS`

---

<a id="item-8"></a>
## [Immich 3.0：自托管照片平台重大更新](https://github.com/immich-app/immich/discussions/29439) ⭐️ 8.0/10

Immich 3.0 作为自托管照片和视频管理平台的重要更新已发布，带来了新功能和改进。此次发布引发了社区广泛讨论，超过 200 条评论涉及加密设置、部署体验和功能请求等话题。 此次发布意义重大，因为 Immich 是 Google Photos 领先的开源替代品，3.0 版本标志着以隐私为中心的自托管照片管理持续成熟。社区高度参与（408 分，205 条评论）显示了用户的强烈兴趣和实际采用，使其成为自托管生态系统的关键里程碑。 讨论中突出显示了一个来自本科生软件开发课程的学生贡献的 bug 修复，用户们积极分享使用 Hetzner 全盘加密和 Nginx 反向代理配合 Let's Encrypt SSL 的加密设置。一些用户表达了对端到端加密的需求，而另一些用户则质疑其在自托管场景中的必要性。

hackernews · hashier · 7月2日 14:13 · [社区讨论](https://news.ycombinator.com/item?id=48761944)

**背景**: Immich 是一个高性能的自托管照片和视频管理解决方案，作为 Google Photos 和 iCloud 等云服务的注重隐私的替代品。它提供 iOS 和 Android 移动应用，具有自动后台上传、人脸识别、相册共享和地图视图功能。该平台通常通过 Docker 部署，并可通过反向代理和 SSL 证书进行安全加固。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/immich-app/immich">GitHub - immich -app/ immich : High performance self - hosted photo ...</a></li>
<li><a href="https://xtom.com/blog/self-hosted-photo-management-apps-ditch-google-icloud-photos/">The 15 Best Self - Hosted Photo Management Apps... | xTom</a></li>
<li><a href="https://medium.com/@aleksej.gudkov/immich-encryption-ensuring-data-security-for-your-media-library-c423bd4ddd6f">Immich Encryption : Ensuring Data Security for Your Media... | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极，用户称 Immich 是“一款令人难以置信的软件，与 Google Photos 不相上下”，并分享了详细的部署设置。一位教授自豪地表示，看到自己课程中学生的 bug 修复被合并到此次发布中，而一些用户则就自托管设置中端到端加密的必要性展开了辩论。

**标签**: `#self-hosted`, `#photo management`, `#open source`, `#immich`, `#privacy`

---

<a id="item-9"></a>
## [Postgres 事务：分布式系统的超能力](https://www.dbos.dev/blog/co-locating-workflow-state-with-your-data) ⭐️ 8.0/10

文章主张将工作流状态与 Postgres 数据共置，利用事务原子性作为出站模式等分布式协调模式的更简单替代方案。 每个工作流步骤成为一个数据库提交单元，将工作流推进与数据库事务一一对齐，从而消除了对单独消息队列的需求。

hackernews · KraftyOne · 7月2日 18:38 · [社区讨论](https://news.ycombinator.com/item?id=48765639)

**背景**: 在分布式系统中，确保跨多个服务（例如更新数据库和发送消息）的原子性具有挑战性。出站模式通过在同一数据库事务中存储消息来解决此问题，但仍需要单独的消息中继进程。将工作流状态直接共置于数据库中，利用数据库内置的 ACID 保证，更简单地实现相同目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://microservices.io/patterns/data/transactional-outbox.html">Pattern : Transactional outbox</a></li>
<li><a href="https://en.wikipedia.org/wiki/Atomicity_(database_systems)">Atomicity (database systems ) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论中既有赞同也有辩论。一些用户赞扬原子性的好处并分享类似的内部解决方案，而另一些用户则担心数据库与工作流之间的紧密耦合，尽管承认在实践中通常可以接受。

**标签**: `#Postgres`, `#distributed systems`, `#transactions`, `#workflow`, `#database`

---

<a id="item-10"></a>
## [Meta 计算策略预示新云模式转变](https://newsletter.semianalysis.com/p/meta-compute-everyone-wants-to-be) ⭐️ 8.0/10

据报道，Meta 正在转向一种“新云”（neocloud）计算策略，推出了 SpaceX 2.0、Bedrock 2.0 等计划，并将推荐系统（RecSys）规模扩大 10 倍，这标志着整个行业正从传统超大规模云模式转型。 这一转变可能重塑 AI 基础设施格局，因为新云提供专业化、成本高效的 GPU 集群，挑战 AWS、Azure 和 Google Cloud 等超大规模云服务商的主导地位。对 Meta 而言，将推荐系统规模扩大 10 倍将直接影响其核心广告和内容推荐业务，可能提升用户参与度和收入。 文章提到了多个内部项目：SpaceX 2.0（可能是一个计算基础设施项目）、Bedrock 2.0（可能是一个基础模型或平台），以及推荐系统 10 倍扩展。还预告了即将推出的“ClusterMAX 排名”，暗示这是一个新的集群性能指标或基准。

rss · Semianalysis · 7月2日 22:18

**背景**: 新云是一种新型云服务商，专门提供针对 AI 工作负载优化的 GPU 集群，通常成本低于传统超大规模云服务商。它们填补了超大规模云服务商专注于通用计算所留下的市场空白。作为 AI 计算的最大消费者之一，Meta 正在探索新云模式，以对其基础设施获得更多控制权和效率，特别是在训练大规模推荐系统和 AI 模型方面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hivenet.com/post/post-neocloud-business-model-explained">Neocloud business model explained: how AI GPU clouds work | Hivenet</a></li>
<li><a href="https://vast.ai/article/what-is-a-neocloud-business-model-explained">What Is a Neocloud ? The Business Model Explained</a></li>
<li><a href="https://www.linkedin.com/pulse/rise-neoclouds-transforming-ai-infrastructure-era-andre-b2xye">The Rise of Neoclouds : Transforming AI Infrastructure in the Era of...</a></li>

</ul>
</details>

**标签**: `#cloud computing`, `#AI infrastructure`, `#Meta`, `#neocloud`, `#recommendation systems`

---

<a id="item-11"></a>
## [Hierarchos：2.32 亿参数循环记忆增强模型初现潜力](https://www.reddit.com/r/MachineLearning/comments/1um123n/hierarchos_preliminary_findings_from_a_232m/) ⭐️ 8.0/10

研究人员发布了 Hierarchos 的初步发现，这是一个 2.32 亿参数的循环记忆增强语言模型，它成功训练并保持了连贯性，采用了结合 RWKV、分层管理者/工作者循环、可微分的基于槽的长时记忆以及确定性后缀自动机的混合非 Transformer 架构。 这项工作证明了非 Transformer 架构可以扩展并保持连贯性，挑战了基于 Transformer 的模型的主导地位，并为语言建模提供了一条可能更具参数效率的路径。 关键的工程经验包括修复漂移状态处理和监督式 LTM 更新中的训练/推理一致性不匹配问题，以及通过实现激活钳位来解决 RWKV 通道混合中的数值稳定性问题。

reddit · r/MachineLearning · /u/PhysicsDisastrous462 · 7月3日 01:48

**背景**: 现代大型语言模型主要基于 Transformer 架构，该架构依赖于注意力机制。Hierarchos 探索了一种替代方法，使用循环状态、显式记忆检索和分层迭代计算来实现参数效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2406.19369">Mamba or RWKV : Exploring High-Quality and</a></li>
<li><a href="https://www.rwkv.com/">RWKV Language Model</a></li>
<li><a href="https://en.wikipedia.org/wiki/Suffix_automaton">Suffix automaton - Wikipedia</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#language models`, `#recurrent architectures`, `#memory augmentation`, `#non-transformer`

---

<a id="item-12"></a>
## [证监会批准宇树科技科创板 IPO 注册](https://www.csrc.gov.cn/csrc/c105906/c7642867/content.shtml) ⭐️ 8.0/10

2026 年 7 月 1 日，中国证监会正式批准宇树科技股份有限公司在上海证券交易所科创板首次公开发行股票的注册申请。这一批准允许这家仿生机器人制造商按照招股说明书推进股票发行。 此次 IPO 获批是宇树科技（人形与四足机器人领域的领先企业）的重要里程碑，也表明监管机构和市场对具身智能与机器人行业充满信心。上市将为其研发和产能扩张提供大量资金，可能加速全球人形机器人市场的竞争。 证监会要求宇树科技严格按照报送上交所的招股说明书和发行承销方案实施发行，并在注册至发行结束期间及时报告重大事项。宇树科技由王兴兴于 2016 年创立，最初专注于四足机器人，2024 年进入人形机器人市场，第二代产品售价约 1.6 万美元。

telegram · zaihuapd · 7月2日 09:57

**背景**: 科创板是上海证券交易所于 2019 年设立的板块，旨在支持高科技和创新型企业，类似于纳斯达克。宇树科技总部位于杭州，以高性能四足机器人（机器狗）闻名，近年来也涉足人形机器人。具身智能（Embodied AI）指通过物理身体与环境交互的人工智能系统，例如机器人，它融合了感知、认知和行动能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unitree_Robotics">Unitree Robotics</a></li>
<li><a href="https://www.unitree.com/">Unitree Robotics | Robot Dog_Quadruped_Humanoid Robotics ...</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">What is Embodied AI ? | NVIDIA Glossary</a></li>

</ul>
</details>

**标签**: `#Unitree Robotics`, `#IPO`, `#robotics`, `#embodied AI`, `#China market`

---

<a id="item-13"></a>
## [花旗禁用 GPT-5.5，多家企业因 AI 成本飙升限制使用](https://www.404media.co/companies-are-throttling-employees-ai-use-because-its-too-expensive/) ⭐️ 8.0/10

花旗银行自 2026 年 6 月 24 日起完全禁用 Claude Opus 4.6、4.7 及 GPT-5.5 等最新 AI 模型，理由是这些模型消耗的 AI 积分远超普通模型。Atlassian 的 AI 月支出从 2025 年 8 月的 500 万美元飙升至 2026 年 5 月的逾 1500 万美元，公司已终止无限使用并推出成本追踪面板。 这一趋势标志着企业 AI 采用发生重大转变，最初对无限使用 AI 的热情正与按用量计费的严酷现实发生碰撞。企业现在被迫在生产力提升与成本飙升之间寻求平衡，这可能会减缓各行业 AI 整合的步伐。 Adobe 决定不再续签无限使用 Claude 的合同，该合同已于 2026 年 6 月 30 日到期。亚马逊此前关闭了鼓励 AI 使用的内部排行榜，员工随后发现存在此前未知的 token 使用上限。

telegram · zaihuapd · 7月2日 13:59

**背景**: GPT-5.5 和 Claude Opus 等企业 AI 工具通常按 token（输入和输出）计费，这意味着成本直接随使用量增长。许多公司最初为员工提供无限访问以推动采用，但随着使用量激增，月度账单变得不可持续。现在企业正在实施 token 使用上限和积分制系统来控制开支。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sysgeek.cn/gpt-5-5/">GPT - 5 . 5 重磅发布：迈向 AI 智能体的全能新世代 - 系统极客</a></li>
<li><a href="https://www.genspark.ai/zh-tw/blog/seeing-agi-impact7">看見 AGI（7）： Token 鴻溝——為何無 限 制的 AI ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#enterprise`, `#cost management`, `#industry trend`

---

<a id="item-14"></a>
## [华为发布 Atlas 350 加速卡，搭载昇腾 950PR，性能达 H20 的 2.87 倍](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

在 2026 年华为中国合作伙伴大会上，华为正式发布并上市了搭载全新昇腾 950PR 处理器的 Atlas 350 AI 加速卡。华为声称该卡算力达到英伟达 H20 的 2.87 倍，并且是国内唯一支持 FP4 低精度推理的加速卡。 这一发布标志着华为在挑战英伟达 AI 加速卡市场主导地位方面迈出了重要一步，尤其是在出口限制背景下。Atlas 350 声称的性能和 FP4 支持，可能为中国 AI 公司在大规模模型推理方面提供一个有竞争力的国产替代方案。 Atlas 350 配备 112 GB HBM 内存，FP4 算力达 1.56 PFLOPS，TDP 为 600W。它可以在单卡上加载 700 亿参数模型，与前代相比显著降低了推理延迟和投资成本。

telegram · zaihuapd · 7月3日 08:35

**背景**: FP4（4 位浮点数）是一种低精度数据格式，可减少内存占用并加速大语言模型的推理，英伟达也在 Blackwell 架构 GPU 上支持该格式。昇腾 950PR 是华为最新的 AI 处理器，Atlas 350 是其商用加速卡形态。华为一直在开发昇腾系列，作为受美国对华出口限制的英伟达 GPU 的国产替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.digitimes.com/news/a20260324PD210/huawei-ascend-performance-2026.html">Huawei's Ascend 950 PR debuts with nearly 3x H20 performance...</a></li>
<li><a href="https://www.spheron.network/blog/huawei-ascend-950-vs-nvidia-b300-b200-llm-inference-2026/">Huawei Ascend 950 vs NVIDIA B300 and B200 for... | Spheron Blog</a></li>
<li><a href="https://www.scmp.com/tech/tech-trends/article/3347346/huawei-challenges-nvidia-powerful-new-ai-accelerator-card">Huawei challenges Nvidia with powerful new AI accelerator card</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#Huawei`, `#Ascend`, `#accelerator card`, `#deep learning`

---

