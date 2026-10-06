# R. Strauss《查拉图斯特拉如是说》开头〈日出〉第 1–22 小节（人工转写，Otto Singer 四手联弹版）

*R. Strauss, Also sprach Zarathustra Op. 30, introduction ("Sunrise"), bars 1–22, from Otto Singer's piano-duet arrangement. Manual transcription, CC0 1.0. The Secondo upper staff in bars 19–21 is not transcribed.*

| 文件 | 说明 |
|---|---|
| `strauss-zarathustra-op30.musicxml` | MusicXML 4.0（未压缩），Primo、Secondo 两个声部，各两行谱表 |
| `strauss-zarathustra-op30.mid` | 标准 MIDI，仅供试听：♩ = 60（自定的回放速度），震音按 32 分音符奏出 |
| `source.txt` | 转写原始数据（末尾一段是 2026-10-06 对照扫描谱的补转写） |
| `corrections.txt` | 修正清单（10 组共 21 条，见「已修正」） |
| `evidence/` | 修正与补转写所依据的扫描谱裁切图 |

## 片段

- C 大调，4/4，Sehr breit，**第 1–22 小节**，共 22 小节、336 个音（MusicXML 里跨小节、跨拍的音拆开加连线后共 362 个符头）。
- 第 1–4 小节：C 持续低音（pp 震音）。
- 第 5–8、9–12、13–14 小节：小号动机 C–G–C 三次（p feierlich / mf / f），各接大、小三和弦与定音鼓音型。
- 第 15–18 小节：F/C，渐强 immer breiter，到 G 大三和弦。
- 第 19–21 小节：C 大三和弦高潮（ff 震音）。
- 第 22 小节：回到持续低音。

## 底本

Otto Singer 编四手联弹版，Leipzig: Jos. Aibl（©1896，U.E. 1114），多伦多大学音乐系图书馆藏，Internet Archive `alsosprachzarath00stra_0`。用到 Secondo 第 2 页（`aibl1896_singer4h_n5_w1600.jpg`）和 Primo 第 3 页（`aibl1896_singer4h_n6_w1600.jpg`），见 [`../../scans/strauss-zarathustra-op30/`](../../scans/strauss-zarathustra-op30/)。

**这是四手联弹缩编，不是 Strauss 的总谱。** 本转写只记四手联弹谱上印的音。

## 声部组织

| MusicXML | 谱表 | `source.txt` 段 | 内容 |
|---|---|---|---|
| Primo，第 1 行（高音谱号） | Primo 上行 | `primo_rh` | 第 6–21 小节的和弦；第 19–20 小节震音 |
| Primo，第 2 行（高音谱号） | Primo 下行 | `primo_lh` | 第 5–14 小节小号动机 C4–G4–C5（p feierlich）、和弦；第 19–20 小节震音 |
| Secondo，第 1 行（低音谱号） | Secondo 上行 | `secondo_rh` | 和弦；第 7、11、15 小节后半 C3↔C4 震音；第 8、12 小节 C3/G2 八分音符；第 9、13 小节 ff 一击；第 17 小节下行分解和弦 |
| Secondo，第 2 行（低音谱号） | Secondo 下行 | `secondo_lh` | 32 分音符双音震音的低音线：C1↔C2（第 1–14、19–20 小节）→ F1↔F2（15–16）→ G1↔G2（17）→ 第 18 小节 G–A–G → C2↔C3（21–22） |

Primo 第 1–4 小节下行谱表印的是 Secondo 震音的提示音（cue），没有转写。

## 转写方法

- 2026-10-06 人工逐页目读，同日对照扫描谱逐小节核实并补转写了原先空缺的段落（`source.txt` 末尾的补转写段）。
- 编码约定：
  - 32 分音符双音震音（低音线、第 7/11/15 小节 Secondo 后半、第 19–20 小节 Primo 的和弦 ↔ 单音）记为 MusicXML 双音震音（两个二分音符，3 条震音线；第 18 小节第 1–2 拍是八分音符、四分音符长度的震音）。
  - 力度、发夹、"senza Ped."、踏板记号**没有编码**；速度词 "Sehr breit" 照印。
  - 未转写的段落在谱中用斜体文字标注。

## 已修正

修正记在 `corrections.txt`，`source.txt` 保留最初的转写。

| # | 位置 | 原转写 | 改为 | 证据图 |
|---|---|---|---|---|
| Z1 | 第 6 小节末和弦（Primo 两行、Secondo 上行）；第 10 小节末 Secondo 上行 | 十六分音符和弦延续 4.5 拍，连到第 8 / 12 小节 | **只有一个十六分音符**（双符尾），系统末没有连线 | [`za_pri_b6-7_raw.png`](evidence/za_pri_b6-7_raw.png)、[`za_sec_b6-7_raw.png`](evidence/za_sec_b6-7_raw.png)、[`za_sec_b10-12_raw.png`](evidence/za_sec_b10-12_raw.png) |
| Z2 | 第 7、11 小节 Primo | 一个和弦延续 4.25 拍 | 第 1 拍二分音符和弦（f >），第 3 拍同一和弦**重新起音**（p），连到下一小节的十六分音符 | [`za_pri_b7_raw.png`](evidence/za_pri_b7_raw.png)、[`za_pri_b6-7_raw.png`](evidence/za_pri_b6-7_raw.png) |
| Z3 | 第 15 小节 Secondo 上行 | F3 A3 C4 全音符 | 没有 A3；改为补转写的读法（见下表） | [`za_sec_up_b15-16.png`](evidence/za_sec_up_b15-16.png) |
| Z4 | 第 16 小节第 2 个十六分音符 | Primo A5 C6 / A4 C5 | **Primo G5 B5 / G4 B4 C5** | [`za_pri_b16_b13_rh.png`](evidence/za_pri_b16_b13_rh.png)、[`za_pri_b16_b13_lh.png`](evidence/za_pri_b16_b13_lh.png) |
| Z5 | 第 16 小节第 4 拍 | Primo B♭5 D6 E6 / G4 B♭4 C5 D5（读作 C7） | **Primo A♭5 C6 D6 / F4 A♭4 C5 D5**（A 前有降号；Secondo 同为 F3 A♭3 C4 D4） | [`za_pri_b16_b4_rh.png`](evidence/za_pri_b16_b4_rh.png)、[`za_pri_b16_b4_lh.png`](evidence/za_pri_b16_b4_lh.png)、[`za_sec_up_b16_b4.png`](evidence/za_sec_up_b16_b4.png) |
| Z6 | 第 17 小节最后一个十六分音符 | Primo G5 D6 F6 / D4 F4 G4 D5 | **Primo F5 C6 D6 F6 / D4 F4 C5** | [`za_pri_b17_rh.png`](evidence/za_pri_b17_rh.png)、[`za_pri_b17_lh_end.png`](evidence/za_pri_b17_lh_end.png) |
| Z7 | 第 18 小节第 3 拍 | Primo A5 D6 F6 A6 / D4 A4 D5 F5（读作 D 小） | **A 小三和弦**：Primo A5 C6 E6 A6 / E4 A4 C5 E5 | [`za_pri_b18_ch2_rh.png`](evidence/za_pri_b18_ch2_rh.png)、[`za_pri_b18_rh.png`](evidence/za_pri_b18_rh.png)、[`za_pri_b18_lh.png`](evidence/za_pri_b18_lh.png)、[`za_pri_b18_lh_ch2.png`](evidence/za_pri_b18_lh_ch2.png) |
| Z8 | 第 18 小节第 4 拍 Primo 上行 | D6 F6 G6 B6（读作 G7） | **G 大三和弦 B5 D6 G6 B6**，没有 F（符头略糊，把握中高）；Primo 下行 G4 B4 D5 G5 原读正确 | [`za_pri_b18_ch3_rh.png`](evidence/za_pri_b18_ch3_rh.png) |
| Z9 | 第 21–22 小节 Secondo 下行 | C1↔C2 震音 | **C2↔C3** 震音（高一个八度） | [`za_sec_b19-22_bass_g.png`](evidence/za_sec_b19-22_bass_g.png) |
| Z10 | 第 21 小节 Secondo 上行 | C2 + C3 八分音符 | **删除**：原数据没有读谱依据，扫描谱那里是一个音区更高的 ff 和弦。留空并标注「未转写」 | — |

## 补转写（2026-10-06，对照扫描谱）

原先空缺或被简化的段落，补在 `source.txt` 末尾：

| 位置 | 内容 | 把握 | 证据图 |
|---|---|---|---|
| 第 7、11 小节 Secondo 上行 | 前半 C3 G3 C4 二分音符（重新起音）；后半 G3 二分音符 + C3↔C4 震音（p <） | 高 | [`za_sec_b6-7_up.png`](evidence/za_sec_b6-7_up.png)、[`za_sec_b6-7_raw.png`](evidence/za_sec_b6-7_raw.png)、[`za_sec_b10-12_raw.png`](evidence/za_sec_b10-12_raw.png) |
| 第 15 小节 Secondo 上行 | C4 + F3（F3 延续全小节），后半 C3↔C4 震音（p <） | 高 | [`za_sec_up_b15-16.png`](evidence/za_sec_up_b15-16.png) |
| 第 16 小节 Secondo 上行 | 十六分 F3 A3 → 十六分 G3 B3 → F3 A3 C4（八分连二分）→ 第 4 拍 F3 A♭3 C4 D4 | 高 | [`za_sec_up_b15-16.png`](evidence/za_sec_up_b15-16.png)、[`za_sec_up_b16_b4.png`](evidence/za_sec_up_b16_b4.png) |
| 第 17 小节 Secondo 上行 | 八分音符下行分解：E3 G3 C4 E4 → F3 D4 F4 → G3 C4 E4 G4 → C4 E4 → C4 → G3 → E3 → C3 | 高（第 2 个和弦中） | [`za_sec_up_b17.png`](evidence/za_sec_up_b17.png) |
| 第 18 小节 Secondo 上行 | G2 二分音符 → 第 3 拍 E3 A3 C4 → 第 4 拍 D3 G3 B3 D4 | 高 | [`za_sec_up_b18.png`](evidence/za_sec_up_b18.png) |
| 第 15–18 小节 Secondo 低音线 | 15–16：F1↔F2 震音；17：G1↔G2；18：第 1 拍 G1 八分音符 + G1↔G2（八分音符长度的震音），第 2 拍 G1↔G2 震音，第 3 拍 A1 A2 四分音符，第 4 拍 G1 G2 四分音符 | 高（第 18 小节第 1–2 拍的节奏中） | [`za_sec_low_b14-16.png`](evidence/za_sec_low_b14-16.png)、[`za_sec_low_b13-18.png`](evidence/za_sec_low_b13-18.png)、[`za_sec_low_b17-18.png`](evidence/za_sec_low_b17-18.png)、[`za_sec_b18_b12_raw.png`](evidence/za_sec_b18_b12_raw.png)、[`za_sec_b18_b34_bass_g.png`](evidence/za_sec_b18_b34_bass_g.png) |

## 核实结果（核实无误，未改）

- 第 8、12 小节 Secondo 上行的 8 个八分音符 C3/G2 交替（从 C3 起，断奏，f senza Ped. 渐强）正确。
- 第 16 小节第 1、3 个和弦，第 17 小节除最后一个十六分音符以外的音，第 18 小节第 1 拍和第 4 拍 Primo 下行，都正确。
- 第 13–14、19–20 小节低音 C1↔C2 震音正确。

## 已知问题

1. **第 19–21 小节 Secondo 上行谱表未转写**（第 19–20 小节的震音和弦、第 21 小节的 ff 和弦）。导出里是休止，第 19 小节处有文字标注。
2. 第 18 小节 Secondo 低音第 1–2 拍的节奏是中等把握的读法（一个八分音符加带震音线的符杠）。
3. 第 17 小节 Secondo 上行第 2 个和弦（F3 D4 F4）把握中等。
4. 力度、发夹、踏板记号没有编码。

## 与电子谱的比对

对照对象：Michael Dunn 编管风琴版（IMSLP #911382，2024，CC BY-SA 4.0）。**这是另一份改编，不是原作，只用来发现疑点，本仓库没有从中复制任何音符；结论都以四手联弹扫描谱为准。** 两份谱都是 22 小节、逐小节对应。

- 第 6、10、14 小节末的十六分音符和弦：管风琴版也都只有一个十六分音符，与扫描谱一致（Z1）。
- 第 16 小节第 2 个和弦管风琴版含 G、B，第 4 拍是 A♭4 C5 D5 / F3 A♭3 C4 D4；第 18 小节第 3 拍是 A 小、第 4 拍是不含 F 的 G 大三和弦。这些都与扫描谱一致（Z4、Z5、Z7、Z8）。
- 管风琴版踏板第 14–21 小节的低音走向（C → F → G → A–G → C）与扫描谱 Secondo 低音线的走向相同；节奏、八度和震音写法不同。
- 其余差别是改编手法：第 5–6 小节小号动机低一个八度（左手 C3–G3–C4）；第 8、12 小节是踏板 C1 持续加 G1 三连音，而不是 C3/G2 八分音符；第 19–20 小节是持续和弦，没有震音；音区整体偏低。
