# 格里高利圣咏〈Dies iræ〉第 1–6 节（人工转写）

*Gregorian chant, sequence "Dies iræ" from the Mass for the Dead, stanzas 1–6 (melodies A A B B C C). Manual transcription from the Liber Gradualis (Tournai: Desclée, 1883), CC0 1.0.*

| 文件 | 说明 |
|---|---|
| `chant-dies-irae.musicxml` | MusicXML 4.0（未压缩），1 个声部 Cantus：无符干音符头、纽姆记作连线、歌词音节、拍号不打印；每行诗一小节，每节末双细线 |
| `chant-dies-irae.mid` | 标准 MIDI，仅供试听：每个音一样长（♩ = 108），**不是**任何一种演唱节奏 |
| `source.txt` | 转写原始数据（文件头写明底本、音高与时值约定） |
| `corrections.txt` | 修正清单：没有修正（见下文「核对」） |
| `evidence/` | 扫描谱裁切图：每一行谱表一张（叠了音高辅助线），另有几处细节放大 |

## 范围

- 继抒咏〈Dies iræ〉按常见编号共 19 节，前面的节旋律 A、B、C 各唱两节为一轮（AA BB CC），后面再重复并以 Lacrimosa 等结尾。本转写取**第一轮**：第 1–6 节，到第 7 节 "Quid sum miser" 前的双纵线为止。
- 18 行诗（每节三行），**192 个音**、36 个纽姆（连线）、144 个歌词音节。
- 只转写音高、纽姆分组、纵线和歌词音节；原谱的谱号、行末导音（custos）不另编码，后来读者的铅笔记号不转写。

## 底本与选择理由

*Liber Gradualis a S. Gregorio Magno olim ordinatus postea Summorum Pontificum auctoritate recognitus ac plurimum auctus cum notis musicis ad majorum tramites et codicum fidem figuratis ac restitutis …*，Tornaci Nerviorum（Tournai）：Typis Societatis Sancti Joannis Evang. Desclée, Lefebvre et Soc.，1883。Missa pro Defunctis，Sequentia（第 I、II 调式），第 [144]–[145] 页。法国国家图书馆（BnF）音乐部藏本 RES VMC MS-223（扉页前空白页有铅笔署名 "V. d'Indy"），Gallica ark:/12148/btv1b104642876，经 Wikimedia Commons。见 [`../../scans/chant-dies-irae/`](../../scans/chant-dies-irae/)。

为什么选这一本：

1. **1900 年以前印行，没有后来的版权问题。** 通行的〈Dies iræ〉多半从 20 世纪的 Solesmes《Liber Usualis》（1896 年初版，常见的是 1920–1960 年代 Desclée 各版）或 1908 年梵蒂冈版抄来。20 世纪初起的 Solesmes 版加了 Mocquereau 的节奏记号（附点、横线、ictus 竖线），Solesmes 对这套记号主张专有权，书上印有声明；1920 年代以后的版本在美国也还可能在版权期内。为了让转写的来源完全干净，这里不用《Liber Usualis》或任何带节奏记号的版本，只用 1900 年以前的印本。
2. **这是后来通行旋律的直接来源。** 1883 年这本《Liber Gradualis》是 Solesmes 修士 Dom Joseph Pothier（1835–1923）按中世纪写本恢复的版本，1908 年梵蒂冈版（以及据它排印的《Liber Usualis》）的旋律基本就是它。也就是说，它印的是 Berlioz、Liszt、Rachmaninoff 等人引用的那条 "F–E–F–D" 旋律，和游戏里原来用的现代版本音高一致（见下文比对），换底本不改变听感。
3. **不选的其他版本**：19 世纪通行的「Medicaea」系（1614 年罗马版及 1871 年起 Pustet 的官方再版）删改过许多圣咏，很多旋律与中世纪传统、与现代通行版本都不同；法国、德国各地教区的地方用书也各有异文。我们看过 Pustet 版《Compendium Gradualis et Missalis Romani》（Cincinnati，1893；Internet Archive `compendiumgradu00churgoog` 第 31*–32* 页），但那份扫描是黑白二值化的低清图，纽姆糊成一团，**无法可靠地逐音读出**，所以没有拿它做逐音比对，也没有收进本仓库。

## 原谱的记谱法与本转写的约定

- **谱表与音高**：四线谱，do 谱号（C 谱号）在第四线（最上一线），全段没有换谱号、没有降号。转写取 do = C5，四条线自上而下为 C5、A4、F4、D4，终止音 D4（第一 / 第二调式，D 多利亚）。这只是记谱八度的约定，素歌本无绝对音高；男声演唱一般低八度。
- **时值**：方形记谱没有时值。`source.txt` 和导出文件里每个印出的音都记作一个四分音符，只表示次序；MIDI 也按等长回放。怎样唱出节奏（Pothier 的「自由节奏」、Solesmes 的节奏学说、后世的各种节拍化）都是演释，不在转写里。
- **一小节 = 一行诗**。原印本每行诗末印一条贯穿四线的纵线（导出为普通小节线），每节末印双纵线（导出为双细线）。小节长度 = 该行的音数（8–13），MusicXML 的拍号设为不打印。
- **纽姆**：同一音节上连成一组的几个音记作一条连线（`source.txt` 里的 `(` … `)`）。这一段用到的纽姆：单音 punctum / virga；pes（下→上两音，上下叠印）；clivis（上→下两音，带竖线）；porrectus（斜笔 + 方头，高→低→高三音）；climacus（带竖线的方头 + 两个菱形，三音下行）。
- **歌词**：按原印本拼写（æ、重音符照印，例如 favílla、futúrus、stupébit、proferétur），分音节是我们加的。每个纽姆（或单音）对应一个音节，与原印本的排字对位一致。

### 各行旋律（便于检索；与 `source.txt` 相同）

| 行 | 小节 | 音（括号 = 一个纽姆） |
|---|---|---|
| A1 Dies iræ, dies illa / Quantus tremor est futúrus | 1、4 | F E F D E C D D |
| A2 solvet sæclum in favílla / quando Judex est ventúrus | 2、5 | F (F G) (F E) (D C) E F E D |
| A3 teste David cum Sibylla / cuncta stricte discussúrus | 3、6 | A3 (C D) D (D C) E F E D |
| B1 Tuba mirum spargens sonum / Mors stupébit et natúra | 7、10 | A C5 C5 (B G A) (A G F) G A (A D) |
| B2 per sepúlcra regiónum / cum resúrget creatúra | 8、11 | F E F D E C D D |
| B3 coget omnes ante thronum / judicánti responsúra | 9、12 | F (G A) (A G F) (E D C) E F E D |
| C1 Liber scriptus proferétur / Judex ergo cum sedébit | 13、16 | A (G F) G (A D) (D C) A3 (C D) D |
| C2 in quo totum continétur / quidquid latet apparébit | 14、17 | (F E) D C A3 C D F (E C D) |
| C3 unde mundus judicétur / nil inúltum remanébit | 15、18 | A F G D C D F (E C D) |

（未注八度的音都在 C4–C5 之间；A3 是第一线下加一线下方的 A。）

## 转写方法与核对

- 2026-10-19 人工逐音目读。辅助脚本只做裁切、放大、在谱线之间画音高辅助线（每个裁切图按局部谱线位置分段画，页面略有倾斜）；音高与纽姆分组都由人眼在放大图上确认。
- **内部互证**：继抒咏每段旋律唱两节，所以第 1/2、3/4、5/6 节是同一旋律、不同歌词、在谱面上分别印了两次。三对逐音、逐纽姆完全一致，没有一处需要改，`corrections.txt` 为空。
- 印面清楚，没有疑似误植；没有需要编辑性补入或更改的音。

## 已知问题与不确定处

| 位置 | 问题与结论 | 证据图 |
|---|---|---|
| 第 1 小节开头 | 谱号后面、第一个音之前印着一个带竖线的小方头：方头在 A4 线上，竖线向下穿过 F4 线。形状与行末的导音（custos）相同（行末导音竖线向上）。它和第一个音 F4 对不上，不是音符，也不像纵线；可能是排版时留下的多余活字。**不编码** | [`p144_m01_mark_after_clef_vs_custos.png`](evidence/p144_m01_mark_after_clef_vs_custos.png)（左：这个记号；右：第 1 行末的导音） |
| 每节末 | 双纵线里涂了蓝铅笔，节首写了蓝铅笔节号 "1/"、"2/1"、"3/" …，第 18 小节末另有一道铅笔竖线。都是后来读者（这本书属于 Vincent d'Indy）加的，放大可见底下印的是两条细线组成的双纵线。只编码印出的双纵线 | [`double_bars_m03_m12_pencil_fill.png`](evidence/double_bars_m03_m12_pencil_fill.png) |
| 第 14、15、17、18 小节末音 | porrectus：斜笔从 E4 下到 C4，再接 D4 上的方头，读作 E4 C4 D4。斜笔的起点与终点以笔画两端的中线判定 | [`p145_m14_porrectus_E4_C4_D4.png`](evidence/p145_m14_porrectus_E4_C4_D4.png) |
| 页码与印刷年份 | 这一段在全书方括号页码 [144]–[145] 的部分（Missa pro Defunctis 前后是 Proprium 的方括号页码，书末索引第 96* 页把 "Dies iræ, dies illa" 列为 [144]）。扉页印 1883 年；BnF 这部藏本是否把方括号页码部分与正文同年印行，书上没有另外的版权页可证，我们按扉页记为 1883 年版 | — |
| 八度 | do = C5 是约定（见上）。改成 do = C4 时全体低八度，音程不变 | — |

## 与其他电子谱的比对

下面这份电子谱**只用来发现疑点，本仓库没有从中复制任何音符**。

- **CPDL #00460**，John Henry Fowler 编（CPDL License）：〈Dies irae〉全曲单旋律加编者的平行四度 organum 与托音，八分音符节奏化。按每个起点取圣咏旋律（organum 和弦取高音）逐音比较：第 1–4、8–16 行**音高全部相同**（第 3 行 Fowler 在同一起点重复录入了一个 E4）。第 7 行（Tuba mirum）Fowler 把两个纽姆叠成四音和弦，按起点读出来少了 F4、G4 两个音，是录入问题，我们按扫描谱。Fowler 版第 5–6、17–18 行把一行诗拆进了几个声部、起点互相重叠，没有逐音比较。

## 歌词

Dies iræ, dies illa, / solvet sæclum in favílla: / teste David cum Sibylla. ‖ Quantus tremor est futúrus, / quando Judex est ventúrus, / cuncta stricte discussúrus! ‖ Tuba mirum spargens sonum / per sepúlcra regiónum, / coget omnes ante thronum. ‖ Mors stupébit et natúra, / cum resúrget creatúra, / judicánti responsúra. ‖ Liber scriptus proferétur, / in quo totum continétur, / unde mundus judicétur. ‖ Judex ergo cum sedébit, / quidquid latet apparébit: / nil inúltum remanébit.

（13 世纪拉丁文，公有领域。）

## 证据图一览

| 文件 | 内容 |
|---|---|
| `p144_line1_m01-02_st1.png` | 第 [144] 页继抒咏第 1 行谱表：第 1 小节全部、第 2 小节前 8 个音（叠音高辅助线，标签按 do = C5） |
| `p144_line2_m02-04_st1-2.png` | 第 2 小节末 3 个音、第 3 小节、第 4 小节前 5 个音 |
| `p144_line3_m04-06_st2.png` | 第 4 小节末 3 个音、第 5 小节、第 6 小节前 6 个音 |
| `p145_line1_m06-08_st2-3.png` | 第 [145] 页第 1 行：第 6 小节末 4 个音、第 7 小节、第 8 小节前 2 个音 |
| `p145_line2_m08-09_st3.png` | 第 8 小节其余、第 9 小节 |
| `p145_line3_m10-11_st4.png` | 第 10 小节、第 11 小节 |
| `p145_line4_m12-13_st4-5.png` | 第 12 小节、第 13 小节前 9 个音 |
| `p145_line5_m13-14_st5.png` | 第 13 小节末 3 个音、第 14 小节、第 15 小节前 5 个音 |
| `p145_line6_m15-16_st5-6.png` | 第 15 小节末 5 个音、第 16 小节、第 17 小节前 2 个音 |
| `p145_line7_m17-18_st6.png` | 第 17 小节其余、第 18 小节（右端是第 7 节开头，未转写） |
| `p144_m01_mark_after_clef_vs_custos.png` | 见「已知问题」第 1 条 |
| `double_bars_m03_m12_pencil_fill.png` | 第 3 小节末（[144]）、第 12 小节末（[145]）的双纵线与铅笔涂色 |
| `p145_m14_porrectus_E4_C4_D4.png` | 第 14 小节末的 porrectus 放大 |

每张行图的文字是**下方**谱表的歌词在图底、上一行的歌词在图顶（裁切时带进来的），读图时以谱表下方的歌词为准。
