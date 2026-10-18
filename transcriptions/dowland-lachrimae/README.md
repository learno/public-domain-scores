# Dowland〈Lachrimæ〉（Flow my teares），全曲（人工转写）

*John Dowland, "Lachrimæ" ("Flow my teares"), The Second Booke of Songs or Ayres (1600), No. II — Canto, Basso and lute tablature, complete (24 bars). Manual transcription from the 1600 print, CC0 1.0.*

| 文件 | 说明 |
|---|---|
| `dowland-lachrimae.musicxml` | MusicXML 4.0（未压缩），3 个声部：Canto、Lute（实际音高，低八度高音谱号）、Basso |
| `dowland-lachrimae.mid` | 标准 MIDI，仅供试听：♩ = 100（原谱没有速度标记，这是自定的回放速度）；反复不展开 |
| `source.txt` | 转写原始数据（文件头写明底本、定弦与指法谱约定） |
| `corrections.txt` | 修正清单（2 条编辑性修正：第 23 小节 Canto 升号；第 19 小节 Basso 补一个四分音符） |
| `evidence/` | 疑点处的扫描谱裁切图（文件名带 `_bpl` / `_eebo` 的是两本藏本的对照图） |

## 范围

- 歌曲的全部音乐：A 小调（Aeolian），24 小节，三个乐段各 8 小节；第 8、16 小节末是反复记号。
- **Canto** 101 个音，**Basso** 88 个音，**鲁特琴** 308 个音（179 个起音时刻，其中 69 个是和弦，110 个是单音）。合计 497 个音。
- 歌词（Canto、Basso 下各印两段词）**没有编码**；鲁特琴谱下的右手指法点也不编码。

## 底本

John Dowland, *The Second Booke of Songs or Ayres*, London: Thomas Este for George Eastland, 1600，第 II 首。Boston Public Library 藏本（索书号 G.400.52），Internet Archive `secondbookeofson00dowl`。见 [`../../scans/dowland-lachrimae/`](../../scans/dowland-lachrimae/)。

**A 本**（BPL，彩色扫描，主要底本）：


| 声部 | 扫描图 | 说明 |
|---|---|---|
| Canto + 鲁特琴谱 | `secondbookeofson00dowl_n13.jpg` | 5 行（第 1–21 小节、第 22 小节前半），C1 谱号；每行 Canto 下面是法式指法谱 |
| Basso | `secondbookeofson00dowl_n14.jpg` | 印成**横排旋转 90°**（与 Canto 页对开，给坐在桌子侧面的人读）；顺时针转 90° 后是 5 行，F4 谱号 |
| Canto + 鲁特琴谱末行 | `secondbookeofson00dowl_n14.jpg` 页脚 | 第 22 小节后半至第 24 小节（"that in hell feele not the worlds despite"），正向排印 |

**B 本**（对照用）：同书 EEBO 缩微胶片的黑白扫描，Internet Archive `bim_early-english-books-1641-1700_the-second-booke-of-song_dowland-john_1600`，页 n9 = CANTO 页（对应 A 本 n13）、n10 = BASSO 页（对应 A 本 n14）。IA 元数据注明数字化自缩微胶片 IA40313011-23，没有说明原书藏馆。文件为 `eebo_n9.jpg`、`eebo_n10.jpg`。

两本在下列所有疑点处的印面完全相同，没有停机改版（同一版内换活字）的迹象；唯一的差别是 A 本个体上的墨迹瑕疵（见「已知问题」第 21 小节鲁特琴一行）。

## 转写方法

- 2026-10-18 人工逐音目读。辅助脚本只做裁切、放大、画谱线 / 弦线标尺；音高、时值、指法字母都由人眼在放大图上确认。菱形音头较高，音高按菱形左右两角（最宽处）所在的线 / 间判定。
- **音值不缩减**：breve = 8 个四分音符，semibreve = 4，minim = 2，crotchet = 1，quaver = ½。原谱拍号 Canto、Basso 印 C，鲁特琴谱印 ¢，统一记作 4/2。
- **小节编号**按现代惯例每 8 个四分音符一小节，共 24 小节；**第 23 小节 12 个四分音符**（MusicXML 在该小节改 6/2，第 24 小节改回 4/2，MIDI 同样写了拍号事件）。原印本的小节线不规则，对照见下节。
- Canto 用现代高音谱号，Basso 用低音谱号，鲁特琴写成低八度高音谱号（G8）上的实际音高和弦。
- 连续反复的音头（custos）、乐句末的小节线装饰不编码。

### 原印本小节线与本转写小节号的对照

原印本鲁特琴谱的小节线位置（Canto 的小节线与之一一对应，位置略有错开）：

| 原印本一段（两条小节线之间） | 本转写小节 | 长度（四分音符） |
|---|---|---|
| 第 1 行开头至第一条线 | 1–2 | 16 |
| | 3 | 8 |
| 跨第 1、2 行 | 4 | 8 |
| | 5、6、7 | 各 8 |
| 至反复记号 | 8 | 8 |
| 第 3 行 | 9 + 10 前半 | 12 |
| | 10 后半 + 11 前半 | 8 |
| | 11 后半 | 4 |
| | 12 | 8 |
| 跨第 3、4 行 | 13 | 8 |
| | 14、15 | 各 8 |
| 至反复记号 | 16 | 8 |
| 第 5 行 | 17、18 | 各 8 |
| | 19 + 20 前半 | 12 |
| 跨第 5 行与页脚一行 | 20 后半 + 21 + 22 前半 | 16 |
| | 22 后半 + 23 | 16 |
| 至终止线 | 24 | 8 |

第 21 小节第 3 个四分音符处在 A 本上另有一道只穿过上三条弦线的细竖线（[`lute_m21_stroke_bpl.png`](evidence/lute_m21_stroke_bpl.png)），不在任何小节边界上；B 本同处没有（[`lute_m21_stroke_eebo.png`](evidence/lute_m21_stroke_eebo.png)），所以是 A 本个体瑕疵，不是活字。鲁特琴谱末尾是带点的反复记号，Canto 末尾是普通终止线；本转写只按要求在第 8、16 小节画反复记号，第 24 小节画终止线。

## 鲁特琴定弦与指法谱读法

**结论：tenor G 鲁特琴，第 1–6 弦 = G4 D4 A3 F3 C3 G2，第 7 弦（低音弦，字母写在第 6 条线下方并带短线）= D2。** 品位字母 a b c(r) d e f = 空弦至 5 个半音。

推断依据（同一时刻 Basso 与鲁特琴最低音重合；所有重合处一致，没有反例）：

| 位置 | 鲁特琴 | Basso | 证据图 |
|---|---|---|---|
| 第 1 小节第 1 拍 | 第 6 弦 c = A2，第 5 弦 e = E3 | A2 | [`lute_sys1_m01-02.png`](evidence/lute_sys1_m01-02.png) |
| 第 11 小节第 8 个四分音符 | 第 5 弦 b = C♯3 | C♯3 | [`lute_m11_Csharp3_and_m12_7th_course_D2_F2.png`](evidence/lute_m11_Csharp3_and_m12_7th_course_D2_F2.png) |
| 第 12 小节第 4、5、8 个四分音符 | 第 7 弦 a = D2，d = F2，d = F2 | D2、F2、F2 | 同上 |
| 第 13 小节第 8 个四分音符 | 第 6 弦 a = G2 | G2 | [`lute_m14-15_7th_course_and_Gsharp2.png`](evidence/lute_m14-15_7th_course_and_Gsharp2.png) |
| 第 14 小节第 6、7 个四分音符 | 第 7 弦 a = D2，d = F2 | D2、F2 | 同上 |
| 第 15 小节第 4 个四分音符 | 第 6 弦 b = G♯2 | G♯2 | 同上 |
| 第 16、23 小节第 1 拍 | 第 7 弦 c = E2 | E2 | [`lute_m16_beat0_beat4_chords.png`](evidence/lute_m16_beat0_beat4_chords.png)、[`lute_m22-23_7th_course_E2_F2.png`](evidence/lute_m22-23_7th_course_E2_F2.png) |
| 第 22 小节第 7 个四分音符 | 第 7 弦 d = F2 | F2 | [`lute_m22-23_7th_course_E2_F2.png`](evidence/lute_m22-23_7th_course_E2_F2.png) |

上面几弦的音程（第 3、4 弦大三度，其余纯四度）由和弦本身验证：例如第 1 小节第 1 拍 c6 / e5 / e4 / d3 = A2 E3 A3 C4，第 8、24 小节 A 大三和弦（第 3 弦 e = C♯4），第 16、23 小节 E 大三和弦（第 4 弦 d = G♯3）。绝对音高取 tenor G 的名义音高（第 1 弦 G4）；第 7 弦 D2 与 Basso 的 D2 同度，Basso 的八度由它自己的谱号决定，两者互相印证。

指法谱约定（据本页）：字母写在所属弦线上（最上一条线 = 第 1 弦）；节奏记号写在谱表上方：无旗的竖杆 = semibreve，一面直旗 = minim，一个圈 = crotchet，两个圈 = quaver，加点 = 附点；一个记号管到下一个记号为止。每小节按此读出的时值都正好凑满 8 个四分音符（第 23 小节 12 个）。

## 临时记号

原印本的升号只在印出处编码（`source.txt`），编辑性的另写进 `corrections.txt`：

- **第 7 小节**（"shame disclose" 处的终止）：Canto 的 G quaver 与 G minim **下方**（谱表外、C4 线高度）各印一个 ✱，记作 G♯4；中间的 F quaver 没有符号，照印记作 F♮4。两本相同。[`canto_m07_sharps_below_staff.png`](evidence/canto_m07_sharps_below_staff.png)（A）、[`canto_m07_bpl.png`](evidence/canto_m07_bpl.png) / [`canto_m07_eebo.png`](evidence/canto_m07_eebo.png)
- **第 23 小节**（"despite" 前的终止）：只在 G quaver 前印 ✱（G♯4），F quaver 与随后的 G minim 都没有符号。`corrections.txt` C1 按第 7 小节同一音型（两个 G 都升）给第二个 G 补升号（编辑性）；F 照印保持 F♮。两本都只有第一个 G 前有升号。[`canto_m23_sharp_before_G.png`](evidence/canto_m23_sharp_before_G.png)、[`canto_m23_bpl.png`](evidence/canto_m23_bpl.png) / [`canto_m23_eebo.png`](evidence/canto_m23_eebo.png)
- 鲁特琴在这两处都只弹 E 与 B（没有三音），帮不上判断。
- 其他升号（第 2、5、6、11、16、17、18、20、23 小节 Canto 的 G♯，第 11 小节 Basso 的 C♯，第 15 小节 Basso 的 G♯）都是印出来的；Basso 的 C♯3、G♯2 与鲁特琴同时刻的低音相同。

## 已知问题与不确定处

| 小节 | 声部 | 问题与两本（A = BPL，B = EEBO）对照结论 | 证据图 |
|---|---|---|---|
| 7、23 | Canto | 第 7 小节两个 ✱ 印在谱表下方、分别对着两个 G，F 无记号；第 23 小节只有第一个 G 前有 ✱。A、B 全同。终止处 F 是否升高（演唱习惯常唱 F♯）属编辑判断，照印为 F♮；第 23 小节第二个 G 的升号是编辑补的（`corrections.txt` C1） | `canto_m07_bpl/eebo.png`、`canto_m23_bpl/eebo.png` |
| 16 | 鲁特琴 | 第 3 个 minim 拍的 E 大三和弦（E2 E3 G♯3 B3 E4）里，第 6 弦印的是 c（= A2），与和声不合，可能是 e（= B2）的误植。A、B 两本第 6 弦字母都与上面第 2、3 弦的 c 同形、不是 e；两本都不提供改版证据，照印保留 | `lute_m16_full_bpl/eebo.png` |
| 19 | Basso | **原印本缺一个四分音符**：两本都只印了附点二分 A2 → **一个**四分 G3（音头略高，上方有窄墨块，但只有一根符干、一个音头）→ 四分 E3（A 本着墨淡，B 本清楚）→ 二分 F3，合计 7 拍。`source.txt` 照印这 7 拍，A3 是编辑性补入（`corrections.txt` C2：依据同一时刻鲁特琴拍位 3 的 A3 与后续 G3 E3 F3，三份现代电子谱也都是 A3 G3 E3 F3） | `basso_m19_overview_bpl/eebo.png`、`basso_m19_heads_bpl/eebo.png`、`basso_m19_crotchet_E3.png` |
| 21 | Canto | 第 3 个四分音符起的高音读作 E5：两本音头中心都在最上线（D5）上方约 0.6 个线距，没有加线，不是 F5 | `canto_m21_top_bpl/eebo.png`、`canto_m21_E5.png` |
| 21 | 鲁特琴 | 只穿过上三条弦线的细竖线：A 本有、B 本没有 → A 本个体瑕疵，不在活字里，不编码 | `lute_m21_stroke_bpl/eebo.png` |
| 1 | Basso | 第二个 semibreve 读作 A2（与第一个同高；鲁特琴同时刻是 A2）。两本相同 | `basso_m01_bpl/eebo.png`、`basso_m01_A2_A2.png` |
| 12 | Basso | D2 带一条加线；两个 F2 挂在最下一线下方（不需要加线）。与鲁特琴第 7 弦同时刻的 D2 / F2 相合，核实无误 | `basso_m12_D2_F2_F2.png` |
| 15 | Basso | A2 附点二分 → ✱ G♯2 → A2 → 附点四分 F2 → 八分 F2；第 1 个音读作 A2（音头最宽处）。两本相同 | `basso_m15_bpl/eebo.png`、`basso_m14-15_A2_Gsharp2.png` |
| 22 | Basso | G2 后面的小黑点不是附点：A 本是活字谱线接缝（与上方四条线的短墨块成一列），B 本同处是一段短横。G2、F2 各一个 minim | `basso_m22_dash_bpl/eebo.png`、`basso_m22_G2_F2_no_dot.png` |
| 5、6 | Basso | 第 5 小节两个 A3 quaver、第 6 小节两个 F3 quaver 上有括号，是为配合两段歌词的不同音节分开的音，照印编码为两个 quaver | — |
| 8 | Canto | 终止音是空心方形 breve A4（与第 16、24 小节同形），不是休止 | `canto_m08_breve_A4.png` |

## 与其他电子谱的比对

下面这些电子谱**只用来发现疑点，本仓库没有从中复制任何音符**；每一处不同都回到扫描谱上判定，以扫描谱为准。比对用自写脚本按绝对时间逐音对齐（允许整体错开若干拍或一个八度）。

- **CPDL #85604**，Garvin 编（键盘缩谱 + Canto、Basso；CC BY-NC）：
  - Canto：只有第 7、23 小节终止处的 F♯ / G♯ 不同（编辑性升号，见「临时记号」），另缺第 24 小节终止音 A4。
  - Basso：整体低一个八度（文件里的移调设置有误），对齐后音符全同，只缺第 24 小节终止音 A2。
  - 键盘缩谱基本按鲁特琴谱转写：308 个音里 297 个起点、音高都相同。其余不同已逐一回扫描谱核对，结论是我们的读法与扫描谱一致：第 12 小节第 7 弦的 D2 / F2 Garvin 写高八度；第 16、23 小节第 1 拍 Garvin 省掉 G♯3；第 16 小节第 3 个 minim 拍 Garvin 写 B2（我们照印为 A2，见上表）；第 10 小节第 4 个四分音符的 F3（第 4 弦 a）、第 19 小节第 6 个四分音符的 E4（第 2 弦 c）、第 20 小节第 5 个四分音符的 E3（第 5 弦 e）都清楚印在谱上（[`lute_m10_beat3_F3.png`](evidence/lute_m10_beat3_F3.png)、[`lute_m19-20_E4_and_E3.png`](evidence/lute_m19-20_E4_and_E3.png)）；另有三处 Garvin 有重复音头。
- **CPDL #17579**，David Fraser 编（CPDL License；作品页说明是 Canto、Basso 加 7 弦 tenor G 鲁特琴 TAB，与原印本同一种定弦）：
  - 本地的 MusicXML 只含 Canto、Basso 两个声部，没有鲁特琴 TAB 的弦 / 品信息，所以**只能用来核对 Canto、Basso，也没有用它核对 TAB 读法**；没有取用它的任何音符。我们的定弦结论（tenor G，第 7 弦 D）与它的版本说明一致。
  - Canto：只有第 7、23 小节的编辑性 F♯ / G♯ 不同；Basso：低一个八度，对齐后全同。它在开头多了一个四分音符的弱起，整体错后一拍。
  - 作品页上的 "Possible error" 只涉及第五段歌词 condemn → contemn，与音符无关。
- **Br-492**，Russell 编（交叉核对用的 MusicXML）：Canto 只有第 7、23 小节的编辑性升号不同；Basso 全同；末尾多写了一遍终止音（反复）。
- 我们最初把 Canto 第 8 小节误读成 breve 休止，三份电子谱都是 A4，回扫描谱确认是空心 breve 音头，已在 `source.txt` 里改正（这是转写过程中的自查，不是 `corrections.txt` 的修正）。
