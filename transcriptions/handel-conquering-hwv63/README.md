# Handel《犹大·马加比》HWV 63〈See, the conqu'ring hero comes〉，Full Chorus 全曲（人工转写）

*G. F. Handel, Judas Maccabaeus HWV 63, Part III, "See, the conqu'ring hero comes" — the Full Chorus version (chorus SATB, flutes / violins, horns, oboes, viola, continuo), complete (24 bars). Manual transcription from the Randall full score [1769], CC0 1.0.*

| 文件 | 说明 |
|---|---|
| `handel-conquering-hwv63.musicxml` | MusicXML 4.0（未压缩），11 个声部，按原印本的谱表组织；圆号写记谱音高（带 `<transpose>`），双簧管两声部同一行谱表 |
| `handel-conquering-hwv63.mid` | 标准 MIDI，仅供试听：♩ = 112（原谱没有速度标记，这是自定的回放速度）；圆号按实际音高；反复不展开 |
| `source.txt` | 转写原始数据（文件头写明底本、谱表与谱号） |
| `corrections.txt` | 修正清单（目前没有修正：`source.txt` 即照印） |
| `evidence/` | 疑点与结构处的扫描谱裁切图（叠加了音高辅助线） |

## 范围

- 合唱版（"Full Chorus"）全曲：G 大调，¢（记作 2/2），24 小节。第 1–8 小节后 `:||:`，第 9–16 小节，第 17–24 小节是第 1–8 小节的完整写出，末尾普通双纵线。
- 全部 11 行谱表都转写了：长笛与小提琴两行、圆号两行、双簧管（一行两声部）、中提琴、合唱四部、通奏低音。共 804 个音：

| 声部 | 原印本标注 | 谱号 | 音数 |
|---|---|---|---|
| `fl_vln1` | Trav: e Viol: 1° | G2 | 75 |
| `fl_vln2` | Trav: e Viol: 2° | G2 | 73 |
| `horn1` / `horn2` | Corno 1° / Corno 2° | G2，无调号 | 69 / 65 |
| `ob1` / `ob2` | Hautb: 1° e 2°（同一行谱表，上 / 下声部） | G2 | 75 / 65 |
| `viola` | Viola | C3 | 54 |
| `soprano` / `alto` / `tenor` / `bass` | 合唱四部（谱表无标签，下方印词） | C1 / C3 / C4 / F4 | 75 / 67 / 54 / 66 |
| `bc` | 最下一行，带数字 | F4 | 66 |

- 歌词、通奏低音数字、连线（slur）**没有编码**。`bc` 与合唱 Bass 逐音相同（原印本两行各自印出）。
- 合唱用现代谱号导出：Soprano、Alto 高音谱号，Tenor 低八度高音谱号（G8），Bass 低音谱号。

## 底本

G. F. Handel, *Judas Macchabaeus: an oratorio, in score as it was originally perform'd*，London: printed for William Randall, successor to the late Mr. J. Walsh, [1769]。北卡罗来纳大学教堂山分校音乐图书馆藏本（b7410140），Internet Archive `judasmacchabaeus00hand_0`。见 [`../../scans/handel-conquering-hwv63/`](../../scans/handel-conquering-hwv63/)。

| 扫描图 | 印本页 | 内容 |
|---|---|---|
| `judasmacchabaeus00hand_0_n186.jpg` | 175 | "Full Chorus"：第一行第 1–6 小节，第二行第 7–12 小节 |
| `judasmacchabaeus00hand_0_n187.jpg` | 176 | 第一行第 13–18 小节，第二行第 19–24 小节 |

对照本：Novello 1906 年 John E. West 编声乐谱第 149 页（`judasmaccabaeuso00hand_n158.jpg`）。**只用来核对段落结构与临时记号，没有取用它的音符。**它与 Randall 本结构相同（第 8 小节后反复、第 17–24 小节写出），第 11 小节 Tenor 的升号、第 14 小节 Tenor 的 C♯ 也与 Randall 本相同。

## 转写方法

- 2026-10-19 人工逐音目读。辅助脚本只做裁切、放大、在每行谱表上标出线 / 间的音名；音高、时值、临时记号都由人眼在放大图上确认。合唱四部与通奏低音由本人读；乐队七个声部由一位转写者读，同日又由另一位复核者从扫描谱独立重读全部 7 个声部、24 小节（168 个声部小节，先独立读出、再与 `source.txt` 逐音比对），结果逐音一致，没有改动；疑点逐一回扫描谱确认。
- 小节按原印本小节线编号，原印本每小节就是 ¢ 的一小节，与现代小节一一对应。
- 临时记号照印：印了才写；调号一个升号（圆号行除外）。
- **圆号**：原印本只写 "Corno"，没有注明调。按 C 大调写法、与 G 大调的乐队同奏，判定为 G 调圆号（实际音高比记谱低纯四度）。`source.txt` 写记谱音高；MusicXML 加 `<transpose>`（diatonic −3，chromatic −5）、调号 0；MIDI 按实际音高。圆号行第 11–12 小节是整小节休止。
- 后人的铅笔字（第 175 页右上 "N°58 3rd Part …"、第 9 小节上方 "V"、末小节旁 "No repeat"）不属于印本，不采用。

### 段落结构

- 第 8 小节末：所有谱表都是 `:||:`（结束反复 + 开始反复点）。[`m08_repeat_barline.png`](evidence/m08_repeat_barline.png)
- 开始反复点之后没有任何对应的结束反复；第 17–24 小节把 A 段完整写出，与第 1–8 小节逐音相同。所以印本的实际顺序是 A A B A（第 1–8 小节奏两遍，然后第 9–24 小节）。
- 第 24 小节末是普通双纵线，没有反复点；旁边的铅笔 "No repeat" 是后人加的。[`m24_final_barline_pencil_no_repeat.png`](evidence/m24_final_barline_pencil_no_repeat.png)
- 导出时在第 8 小节画结束反复、第 9 小节画开始反复（照印），第 24 小节画终止线。

## 已知问题与不确定处

没有需要改动印面的地方（`corrections.txt` 为空）。下列各处都按印面读，列出供核对；乐队各条在独立复核时都重新放大判读过，结论不变：

| 小节 | 声部 | 问题与结论 | 证据图 |
|---|---|---|---|
| 11 | Tenor | 第 1 拍印 ✱D4（C4 谱号最上两线之间的间），读作 D♯4（E 小调的导音，B 大三和弦）。Novello 1906 同样是升号 | [`tenor_m11_Dsharp4.png`](evidence/tenor_m11_Dsharp4.png) |
| 11 | Alto | 第 1 个音的音头印得偏高，最宽处在 G4 线上方的间里，读作 A4（与 Soprano 的 C5 成三度、下行 A G F♯ E 的音阶） | [`alto_m11_A4.png`](evidence/alto_m11_A4.png) |
| 12 | 双簧管下声部 | 全音符 ✱ 音头印得很低（中心接近 C4 位置），但没有加线，且与上声部 F♯4 的音头上下相贴、印成三度的 "8" 形；读作 D♯4（B 大三和弦，第二小提琴同时是 D♯5，Alto 同时是 D♯4）。复核同此结论 | [`oboe_m12_lower_Dsharp4.png`](evidence/oboe_m12_lower_Dsharp4.png) |
| 13–14 | Tenor / Bass | 第 14 小节第 1 拍 Tenor 与 Bass 都印 ✱C4，同度；照印 | [`tenor_bass_m13-14_Csharp4_unison.png`](evidence/tenor_bass_m13-14_Csharp4_unison.png) |
| 14 | 双簧管上声部 | 附点二分 G5，附点印在两个音之间，然后第 4 拍再奏一个四分 G5（同音重奏；第 4 拍是实心音头、单独符干）。下声部同时是 A4 二分 + C♯5 二分。照印，复核一致 | [`ob_m14-15_G5_restruck.png`](evidence/ob_m14-15_G5_restruck.png) |
| 7、23 | 第二长笛 / 小提琴 | 第 4 拍是附点八分 F♯5 + 十六分 C5（音头在 B4、D5 两线之间，不是 D5；两处放大后相同），属七和弦的七音，下一小节解决到 B4。复核一致 | [`fl_vln2_m07-08_sixteenth_C5.png`](evidence/fl_vln2_m07-08_sixteenth_C5.png) |
| 15 | 第一长笛 / 小提琴 | 第 3 拍 E5（最上一间）后跳上 ✱C6（两条加线，升号印在音头前），跨度六度；照印，复核一致 | [`fl_vln1_m15_E5_Csharp6.png`](evidence/fl_vln1_m15_E5_Csharp6.png) |

## 与其他电子谱的比对

下面这些电子谱**只用来发现疑点，本仓库没有从中复制任何音符**；不同处一律回扫描谱判定。

- **CPDL #11169**，Charles Mayeul 编（拉丁文歌词 "Canticorum jubilo" 的 SATB 版；CPDL License）：与本转写的合唱四部第 1–16 小节**逐音相同**（它用 D.C. 代替写出的第 17–24 小节）。差别只在记法：
  - Alto 第 12、13 小节、Tenor 第 11 小节它写 E♭（我们照印写 D♯，同音异名）；
  - 它的 Tenor 带了一个多余的低八度移调标签（`<transpose octave-change=-1>`），按发音音高读会整声部低一个八度、落到 Bass 之下；去掉这个标签后与本转写相同。
- **CPDL #48736**，Gibb 编：Tenor 第 11 小节第 1 拍是 C4，原印本（及 Novello 1906）是 D♯4，照印。
- **CPDL #39838**，Grau 编：整体移到 F 大调，只用来确认 Tenor 的八度：它的 Tenor 从 A3 起（移回 G 大调即 B3），与 Gibb 版、本转写相同。
