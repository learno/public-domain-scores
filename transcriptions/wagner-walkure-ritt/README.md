# Wagner〈女武神的骑行〉弱起 + 第 1–18 小节（人工转写，据钢琴缩谱，第 1–8、13–15 小节据总谱改正）

*Wagner, Die Walküre, Act III prelude ("Walkürenritt"), upbeat + bars 1–18. Manual transcription from the Klindworth vocal score, with bars 1–8 and 13–15 corrected from the Schott full score. CC0 1.0. **Not a full-score transcription.***

| 文件 | 说明 |
|---|---|
| `wagner-walkure-ritt.musicxml` | MusicXML 4.0（未压缩），4 条按乐器组划分的声部，记实际音高（不移调） |
| `wagner-walkure-ritt.mid` | 标准 MIDI，仅供试听：♩ = 114（附点四分音符 = 76，自定的回放速度），颤音只奏主音 |
| `source.txt` | 转写原始数据 |
| `corrections.txt` | 修正清单（4 组共 12 条，见「已修正」） |
| `evidence/` | 修正所依据的总谱扫描裁切图 |

## 片段

- 9/8，Lebhaft，B 小调（第 15 小节起转 D 大调，调号保持两个升号）。
- **弱起（一个八分音符，MusicXML 里记为第 0 小节）+ 第 1–18 小节**，共 19 个 measure、333 个音。
- 原曲第 19 小节末开始主题第二次陈述（小号 + 低音小号），不在片段内。

## 底本

- **读音**：Karl Klindworth 编钢琴缩谱，Mainz: B. Schott's Söhne（IA 记 1908 年，版号 27752），第 188–189 页（`klav_n199.jpg`、`klav_n200.jpg`）。
- **声部归属与核实**：Schott 小开本总谱（IA 记 1870 年，页脚版号 27002 c），第 619–624 页（`score_n632.jpg` – `score_n637.jpg`）。各页内容：第 619 页 = 弱起 + 第 1–3 小节，620 = 4–6，621 = 7–9，622 = 10–11，623 = 12–13，624 = 14–15。

见 [`../../scans/wagner-walkure-ritt/`](../../scans/wagner-walkure-ritt/)。

## 声部组织

缩谱把整个乐队压成两行钢琴谱。本转写按材料分成 4 条线，每条线标上总谱里演奏它的乐器组（**归属是推断的**）：

| MusicXML part | 材料 | 总谱里的乐器（推断） | `source.txt` 段 |
|---|---|---|---|
| Woodwinds (trill / figure) | F♯–G 颤音（第 1–8 小节），上行 + 摆动音型（第 9–18 小节，第 13 小节起分高低两组） | 木管 | `trill`、`fig`、`fig8va` |
| Bassoons, Horns 1–4 (dotted rhythm) | 附点「骑行」节奏（第 5 小节起） | 3 支巴松 + 圆号 1–4；第 13–15 小节按巴松（zu 3）与大提琴改正 | `gallop` |
| Horns 6 & 8, Bass Trumpet (theme) | 主题（第 13–16 小节） | 圆号 6、8 + 低音小号 | `theme` |
| Strings (runs) | 弱起与各小节末的急奏 | 弦乐 | `rush` |

总谱里同一材料由许多乐器在不同八度重叠演奏，本转写**只记缩谱里出现的那一层**，没有补总谱的其他重叠声部（例如长笛、单簧管在多个八度上的颤音，各弦乐声部的八度重叠和落音）。

## 转写方法

- 2026-10-06 人工逐页目读缩谱，再翻总谱定乐器组；同日对照总谱核实了疑点（见「已修正」「核实结果」）。
- 编码约定：
  - 颤音：缩谱写成「双横梁长音」，总谱是每拍一组 6 个十六分音符，后面加反复记号。本转写在小节前 3 拍记一个带颤音记号的附点二分音符，后面写出 F♯/G 十六分音符交替（按总谱写到小节末）。
  - 骑行节奏的断奏点、主题的重音照谱记。
  - **力度没有编码**（原谱有 f、p、cresc. 等）。
  - 速度词 "Lebhaft" 照印。

## 已修正

修正记在 `corrections.txt`，`source.txt` 保留最初的转写。

| # | 位置 | 原转写（读自缩谱） | 改为（总谱） | 证据图 |
|---|---|---|---|---|
| W1 | 木管颤音 第 1–8 小节 | 照缩谱在第 3.5 / 4 拍让给急奏；第 3、4 小节末各有一个落点八分音符；第 7 小节第 3 拍读作 A6；第 8 小节记 F♯5 | **颤音持续整小节**（到第 4.5 拍）：总谱第 619–621 页每件颤音木管都是一组 6 个十六分音符 F♯/G 加两个拍反复记号，没有落点八分音符；弱起没有颤音。第 7 小节**没有 A6**。第 8 小节改记与第 7 小节同一批乐器（短笛、大长笛 1）的最高层 F♯6 | 第 1 小节 [`vk_b1_winds_p619.png`](evidence/vk_b1_winds_p619.png)、[`vk_b1_ov_p619_b0-3.png`](evidence/vk_b1_ov_p619_b0-3.png)；第 2 小节 [`vk_b2_winds_p619.png`](evidence/vk_b2_winds_p619.png)；第 3 小节 [`vk_b3_winds_p619.png`](evidence/vk_b3_winds_p619.png)、[`vk_b3_picc_fl_zoom.png`](evidence/vk_b3_picc_fl_zoom.png)；第 4 小节 [`vk_b4_winds_p620.png`](evidence/vk_b4_winds_p620.png)；第 5 小节 [`vk_b5_winds_p620.png`](evidence/vk_b5_winds_p620.png)、[`vk_b5_ov_p620_b4-6.png`](evidence/vk_b5_ov_p620_b4-6.png)、[`vk_b5_g_written.png`](evidence/vk_b5_g_written.png)、[`vk_b5_ob3_cl2_g.png`](evidence/vk_b5_ob3_cl2_g.png)、[`vk_b5_cl3_eh_bcl_g.png`](evidence/vk_b5_cl3_eh_bcl_g.png)；第 6 小节 [`vk_b6_winds_p620.png`](evidence/vk_b6_winds_p620.png)、[`vk_b6_g_written.png`](evidence/vk_b6_g_written.png)；第 7 小节 [`vk_b7-8_winds.png`](evidence/vk_b7-8_winds.png)、[`vk_s634_s8.png`](evidence/vk_s634_s8.png)；第 8 小节 [`vk_b8_winds_p621.png`](evidence/vk_b8_winds_p621.png)、[`vk_b8_ov_p621_b7-9.png`](evidence/vk_b8_ov_p621_b7-9.png)、[`vk_b8_ctx_b7_winds_p621.png`](evidence/vk_b8_ctx_b7_winds_p621.png) |
| W2 | 弦乐 第 8 小节 | 第 3.5 拍起的上行十六分音符 B4–C♯5–D5–E5 | **没有上行急奏**：第二小提琴第 4 拍三十二分音符下行 F♯4–E4–D4–C♯4（落到第 9 小节的 B3；第一小提琴只有第 1 拍的 F♯5 八分音符，不在本线） | [`vk_b8_strings_g.png`](evidence/vk_b8_strings_g.png) |
| W3 | 骑行节奏 第 13–14 小节 | 只有 B3–F♯3 / F♯3–B2（缩谱下声部让给了主题） | 完整骑行节奏 B2–B3–F♯3 / F♯3–F♯4–B3（巴松 zu 3 与大提琴） | [`vk_b13_fag.png`](evidence/vk_b13_fag.png)、[`vk_b13_vc.png`](evidence/vk_b13_vc.png)、[`vk_b14_fag.png`](evidence/vk_b14_fag.png)、[`vk_b14_vc.png`](evidence/vk_b14_vc.png) |
| W4 | 骑行节奏 第 15 小节 | D4–A3 / E3–A2 | **A2–D4–A3 / A3–A4–E4**（巴松与大提琴，后半用次中音谱号） | [`vk_b15_fag_bass.png`](evidence/vk_b15_fag_bass.png)、[`vk_b15_fag_tenor.png`](evidence/vk_b15_fag_tenor.png)、[`vk_b15_vc_bass.png`](evidence/vk_b15_vc_bass.png)、[`vk_b15_vc_tenor.png`](evidence/vk_b15_vc_tenor.png) |

## 核实结果（核实无误，未改）

- 第 15 小节高八度木管音型（短笛 I / 长笛 I）是 **A6/B6**（短笛记谱 A5/B5，实际高八度），转写正确。
- 第 10 小节木管音型的高音区：大长笛 2 是 F♯6/G6，与转写的音区一致。

## 已知问题

- **颤音只记最高一层（简化）**：第 1–8 小节的颤音线按总谱持续整小节（W1），但总谱是多个八度同时演奏，本转写每小节只记最高一层。第 1–4 小节每次加一个八度、去掉最低一层，同时只有两层；第 5 小节起逐层叠加：

  | 小节 | 总谱里持续整小节的颤音层（实际音高） | 本转写 |
  |---|---|---|
  | 1 | F♯4（双簧管 3、单簧管 2、英国管）+ F♯3（单簧管 3、低音单簧管）；短笛、长笛、双簧管 1–2、单簧管 1 休止 | F♯4 |
  | 2 | F♯5（双簧管 1–2、单簧管 1，ff 进入）+ F♯4（双簧管 3、单簧管 2、英国管）；单簧管 3、低音单簧管只有拍头八分音符 | F♯5 |
  | 3 | F♯6（短笛 1–2、大长笛 1）+ F♯5（大长笛 2、双簧管 1–2、单簧管 1）；双簧管 3、单簧管 2、英国管只有拍头八分音符 | F♯6 |
  | 4 | F♯5（双簧管 1–2、单簧管 1）+ F♯4（双簧管 3、单簧管 2、英国管）；短笛、长笛只有拍头八分音符 | F♯5 |
  | 5 | F♯4（双簧管 3、单簧管 2、英国管）+ F♯3（单簧管 3、低音单簧管）；双簧管 1–2、单簧管 1 只有拍头一个 F♯5 八分音符；短笛、长笛休止 | F♯4 |
  | 6 | F♯5（双簧管 1–2、单簧管 1）+ F♯4（双簧管 3、单簧管 2、英国管）+ F♯3（单簧管 3、低音单簧管）；短笛、长笛休止 | F♯5 |
  | 7 | F♯6（短笛 1–2、长笛 1）+ F♯5（长笛 2、双簧管 1–2、单簧管 1）+ F♯4（双簧管 3、单簧管 2、英国管）+ F♯3（单簧管 3、低音单簧管） | F♯6 |
  | 8 | F♯6（短笛 1–2、长笛 1）+ F♯5（长笛 2、双簧管 1–2、单簧管 1）+ F♯4（双簧管 3、单簧管 2）；单簧管 3、英国管、低音单簧管只有拍头八分音符，英国管和低音单簧管在第 4 拍另有 ff 三十二分音符急奏 | F♯6 |

- **急奏的节奏**：第 5–13 小节的急奏照缩谱记成从第 3.5 拍起的十六分音符；总谱电子版第 5–7 小节是第 4 拍上的三十二分音符，第 9–13 小节弦乐另有五连音下行分解和弦等织体。这些是缩谱的简化，没有按总谱改写。
- 颤音记法是近似的（见「转写方法」）；力度没有编码；乐器组归属是推断的。

## 与电子谱的比对

下面这些电子谱**只用来发现疑点，本仓库没有从中复制任何音符**；结论都以扫描谱为准。音高按实际发音比较，电子谱第 k+1 个 measure 对应本转写第 k 小节。

- **MuseScore 用户 Marty Strasinger 的完整管弦乐转写**（https://musescore.com/user/340306/scores/6232442 ；文件内嵌授权声明为 CC BY-SA 4.0）：
  - 骑行节奏第 5–18 小节与总谱一致（W3、W4 的改正与它相同）；主题第 13–16 小节音高、节奏一致。
  - **错处**：第 10 小节长笛 II 记成 F♯5/G5（总谱是 F♯6/G6，差一个八度）；第 15 小节短笛 / 长笛 I 记成 F♯6/G6（总谱是 A6/B6）。
  - 其余差别来自缩谱与总谱的差异：电子谱的颤音由多件乐器在多个八度上逐层叠入；第 9–18 小节木管错开一小节轮流演奏；主题带断奏点，第 16 小节末的 F♯4 一直保持到第 18 小节。
- **PDMX 数据集**收录的 MuseScore 曲谱 5081082（"Walkurenritt. Professional production full score."，PDMX 目录标 CC0）：第 10 小节长笛 II、第 15 小节短笛 / 长笛 I 与总谱一致；**错处**：第 15 小节巴松记成 B2–B3–F♯3 / A3–A4–E4（总谱前半是 A2–D4–A3）。
