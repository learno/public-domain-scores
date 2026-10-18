# Public-Domain Scores：人工转写与扫描底本

[中文](#中文) · [English](#english)

---

## 中文

### 缘起

为一款独立游戏做背景音乐时，我们从公有领域乐谱的扫描件里**人工逐页读谱**，转写了四段古典曲片段和一首完整的鲁特琴歌曲。网上现成的电子谱很多带有署名-相同方式共享之类的授权，有的根本没有公开数据。我们决定把**自己的转写**连同**转写时读的扫描图**一起公开，转写部分放弃一切权利（CC0），谁都可以自由使用、修改、再发布，不必署名。

### 内容

| 片段 | 转写（MusicXML + MIDI） | 底本扫描 | 状态 |
|---|---|---|---|
| Vivaldi〈冬〉RV 297（Op. 8 No. 4）第一乐章 Allegro non molto，第 1–18 小节，5 个分谱 | [`transcriptions/vivaldi-winter-rv297/`](transcriptions/vivaldi-winter-rv297/) | [`scans/vivaldi-winter-rv297/`](scans/vivaldi-winter-rv297/)：巴黎 Hue 刻版分谱 1739（BnF），另附 Le Cène 版两份藏本的若干页 | 完整转写；已逐声部对照扫描谱核实，改正低音第 5 小节音高和 5 处断奏点 |
| Vivaldi〈秋〉RV 293（Op. 8 No. 3）第一乐章 Allegro，第 1–13 小节（开头合奏利都奈罗），5 个分谱 | [`transcriptions/vivaldi-autumn-rv293/`](transcriptions/vivaldi-autumn-rv293/) | [`scans/vivaldi-autumn-rv293/`](scans/vivaldi-autumn-rv293/)：巴黎 Hue 刻版分谱 1739（BnF），与〈冬〉同一套 | 完整转写；已逐声部对照扫描谱、按数字低音核过和声，无需修正；第一小提琴第 8 小节一处弧线未编码（见 README） |
| Wagner《女武神》第三幕前奏〈女武神的骑行〉，弱起 + 第 1–18 小节 | [`transcriptions/wagner-walkure-ritt/`](transcriptions/wagner-walkure-ritt/) | [`scans/wagner-walkure-ritt/`](scans/wagner-walkure-ritt/)：Klindworth 钢琴缩谱、Schott 总谱（Internet Archive） | **据钢琴缩谱读音**，乐器组归属按总谱推断，不是完整总谱；第 1–8、13–15 小节已对照总谱改正 |
| R. Strauss《查拉图斯特拉如是说》Op. 30 开头〈日出〉，第 1–22 小节 | [`transcriptions/strauss-zarathustra-op30/`](transcriptions/strauss-zarathustra-op30/) | [`scans/strauss-zarathustra-op30/`](scans/strauss-zarathustra-op30/)：Otto Singer 四手联弹版（Aibl，©1896；Internet Archive） | 已对照扫描谱改正并补转写；只有第 19–21 小节 Secondo 上行谱表**未转写** |
| Dowland〈Lachrimæ〉（Flow my teares），The Second Booke of Songs（1600）第 II 首，全曲 24 小节：Canto、Basso、鲁特琴谱 | [`transcriptions/dowland-lachrimae/`](transcriptions/dowland-lachrimae/) | [`scans/dowland-lachrimae/`](scans/dowland-lachrimae/)：1600 年伦敦原印本（Boston Public Library 藏本；Internet Archive） | 完整转写；鲁特琴法式指法谱译成实际音高（tenor G 定弦、第 7 弦 D，按低音推定）；歌词未编码 |
| 格里高利圣咏〈Dies iræ〉（安魂弥撒继抒咏）第 1–6 节（旋律 A A B B C C） | [`transcriptions/chant-dies-irae/`](transcriptions/chant-dies-irae/) | [`scans/chant-dies-irae/`](scans/chant-dies-irae/)：Pothier《Liber Gradualis》（Tournai: Desclée，1883；BnF 藏本，经 Wikimedia Commons） | 完整转写（192 个音）；方形记谱无时值，每个音记作等长四分音符，纽姆记作连线，含歌词音节；无修正 |

每个转写目录里有：

- `<名称>.musicxml`：未压缩 MusicXML 4.0，按原谱的声部 / 谱表组织（不是游戏里的配器）。
- `<名称>.mid`：标准 MIDI（format 1），仅供试听，速度为回放所设，不是原谱标记；颤音只奏主音。
- `source.txt`：人工转写的原始数据（纯文本，格式见文件头）。
- `corrections.txt`：修正清单。导出时套在 `source.txt` 之上，每条写明扫描谱依据。
- `evidence/`：修正所依据的扫描谱裁切图（部分加了音高辅助线），README 的「已修正」表逐条引用。
- `README.md`：片段范围、底本、转写方法、已知问题与不确定处、与其他电子谱的比对结论。

`tools/export.py` 从 `source.txt` + `corrections.txt` 生成 MusicXML 与 MIDI，`tools/check.py` 做结构与时值自查。两者只用 Python 3.9+ 标准库：

```
python tools/export.py     # 重新导出全部
python tools/check.py      # 自查：XML 结构、每小节每声部时值、MIDI 可解析
```

### 授权

- **转写（`transcriptions/`）与工具（`tools/`）**：[CC0 1.0 通用](LICENSE)（公有领域贡献）。不需要署名；如果愿意注明出处，欢迎链接本仓库。
- **原作**：Dowland（1626 年去世）、Vivaldi（1741 年去世）、Wagner（1883 年去世）、R. Strauss（1949 年去世）、Klindworth（1916 年去世）、Otto Singer（1931 年去世）的作品，以及中世纪的格里高利圣咏和 Pothier（1923 年去世）编的 1883 年圣咏书，在中国、欧盟、美国均已进入公有领域。
- **扫描图（`scans/`）**：是公有领域印刷乐谱的忠实复制。我们**不对扫描图主张任何权利**，只是按来源机构的说明标注出处：
  - 法国国家图书馆（BnF）藏本，经 Wikimedia Commons 获得，Commons 标注 Public domain，Credit: Bibliothèque nationale de France。BnF 要求注明 **"Source gallica.bnf.fr / BnF"**。BnF Gallica 的使用条件对**商业再利用**另有规定，商业使用前请自行查阅 Gallica 的使用条件。
  - Internet Archive 上多伦多大学音乐系图书馆、北卡罗来纳大学教堂山分校音乐图书馆、波士顿公共图书馆（Boston Public Library）的数字化藏本。条目没有标注授权字段，原书出版于 1931 年以前，作者均已去世 70 年以上。
  - 各目录的 README 逐张列出出处与页码。
  - `transcriptions/*/evidence/` 里的图是上述扫描的裁切（部分叠加了标注音高的辅助线），同样不主张任何权利。
- 以上是我们的理解，不构成法律意见。

### 纠错与贡献

转写难免有错，欢迎指正：

1. 开 issue，写明片段、小节、谱表 / 声部、拍位，以及扫描图文件名和位置（第几行第几小节）。
2. 或直接提 PR：在对应目录的 `corrections.txt` 里加一条（格式见文件头：`<声部> <小节>: <旧 token …> => <新 token …>`，上方注释写依据），运行 `python tools/export.py` 和 `python tools/check.py`，把重新生成的 `.musicxml` / `.mid` 一并提交。旧 token 必须与数据逐个精确匹配，不匹配时导出会报错，这样修正不会悄悄失效。
3. 请只依据**公有领域扫描谱**纠错。不要从带版权或署名-相同方式共享授权的电子谱、录音里抄音符；可以拿它们发现疑点，但改动必须能在扫描谱上指认。

各转写 README 的「已知问题」一节列出了仍不完整或把握不足的地方，最需要有人对照扫描谱补充。

---

## English

### Why this exists

While making the soundtrack for an indie game, we transcribed four short excerpts of classical works and one complete lute song **by hand, page by page, from scans of public-domain editions**. Many existing digital editions carry share-alike licenses or are not published as data at all. We are releasing **our own transcriptions** together with **the scans we read them from**. The transcriptions are dedicated to the public domain (CC0): use, modify and redistribute them freely, no attribution required.

### Contents

| Excerpt | Transcription (MusicXML + MIDI) | Source scans | Status |
|---|---|---|---|
| Vivaldi, *Winter* RV 297 (Op. 8 No. 4), I. Allegro non molto, bars 1–18, all five parts | [`transcriptions/vivaldi-winter-rv297/`](transcriptions/vivaldi-winter-rv297/) | [`scans/vivaldi-winter-rv297/`](scans/vivaldi-winter-rv297/): Paris partbooks engraved by Hue, 1739 (BnF), plus pages from two copies of the Le Cène edition | Complete; checked part by part against the scans; bass bar 5 pitch and five staccato marks corrected |
| Vivaldi, *Autumn* RV 293 (Op. 8 No. 3), I. Allegro, bars 1–13 (opening tutti ritornello), all five parts | [`transcriptions/vivaldi-autumn-rv293/`](transcriptions/vivaldi-autumn-rv293/) | [`scans/vivaldi-autumn-rv293/`](scans/vivaldi-autumn-rv293/): Paris partbooks engraved by Hue, 1739 (BnF), the same set as *Winter* | Complete; checked part by part against the scans and against the bass figures; no corrections needed; one curved stroke in first violin bar 8 not encoded (see README) |
| Wagner, *Die Walküre*, Act III prelude ("Ride of the Valkyries"), upbeat + bars 1–18 | [`transcriptions/wagner-walkure-ritt/`](transcriptions/wagner-walkure-ritt/) | [`scans/wagner-walkure-ritt/`](scans/wagner-walkure-ritt/): Klindworth vocal score and Schott full score (Internet Archive) | **Pitches read from the piano reduction**; assignment to instrument groups inferred from the full score; not a full-score transcription; bars 1–8 and 13–15 corrected from the full score |
| R. Strauss, *Also sprach Zarathustra* Op. 30, opening ("Sunrise"), bars 1–22 | [`transcriptions/strauss-zarathustra-op30/`](transcriptions/strauss-zarathustra-op30/) | [`scans/strauss-zarathustra-op30/`](scans/strauss-zarathustra-op30/): Otto Singer's piano-duet arrangement (Aibl, ©1896; Internet Archive) | Corrected and completed against the scans, except the Secondo upper staff in bars 19–21 (**not transcribed**) |
| Dowland, "Lachrimæ" (Flow my teares), *The Second Booke of Songs* (1600) No. II, complete (24 bars): Canto, Basso and lute tablature | [`transcriptions/dowland-lachrimae/`](transcriptions/dowland-lachrimae/) | [`scans/dowland-lachrimae/`](scans/dowland-lachrimae/): the 1600 London print (Boston Public Library copy; Internet Archive) | Complete; French lute tablature decoded to sounding pitch (tenor G tuning, 7th course D, inferred from the bass); lyrics not encoded |
| Gregorian chant, sequence "Dies iræ" (Mass for the Dead), stanzas 1–6 (melodies A A B B C C) | [`transcriptions/chant-dies-irae/`](transcriptions/chant-dies-irae/) | [`scans/chant-dies-irae/`](scans/chant-dies-irae/): Pothier's *Liber Gradualis* (Tournai: Desclée, 1883; BnF copy via Wikimedia Commons) | Complete (192 notes); square notation has no note values, so every note is an equal quarter note; neumes as slurs; lyric syllables included; no corrections |

Each transcription folder contains the `.musicxml` (uncompressed MusicXML 4.0, organised by the parts / staves of the source, not by our game orchestration), a `.mid` for listening only (tempo chosen for playback; trills play the main note only), the raw transcription data `source.txt`, the list of corrections `corrections.txt`, the scan crops supporting each correction in `evidence/`, and a `README.md` with the excerpt range, source, method, known issues and comparisons with other digital editions.

`tools/export.py` regenerates MusicXML and MIDI from `source.txt` + `corrections.txt`; `tools/check.py` checks XML structure, per-measure / per-voice durations and MIDI parsing. Both need only the Python 3.9+ standard library.

### Licensing

- **Transcriptions (`transcriptions/`) and tools (`tools/`)**: [CC0 1.0 Universal](LICENSE). No attribution required; a link back is appreciated.
- **The works themselves** (Dowland d. 1626, Vivaldi d. 1741, Wagner d. 1883, R. Strauss d. 1949, Klindworth d. 1916, Otto Singer d. 1931), the medieval Gregorian chant and the 1883 chant book edited by Joseph Pothier (d. 1923) are in the public domain in China, the EU and the US.
- **Scans (`scans/`)** are faithful reproductions of public-domain printed music. **We claim no rights in them** and credit them as the holding institutions ask:
  - Bibliothèque nationale de France copies, obtained via Wikimedia Commons (marked Public domain, Credit: Bibliothèque nationale de France). BnF asks for the credit line **"Source gallica.bnf.fr / BnF"**. Gallica's terms of use treat **commercial reuse** separately; check them before any commercial use.
  - Copies digitised by the Internet Archive from the University of Toronto Faculty of Music Library, the Music Library of the University of North Carolina at Chapel Hill and the Boston Public Library. The items carry no license field; the books were published before 1931 and all authors died more than 70 years ago.
  - The README in each scan folder lists source, page and content for every image.
  - Images in `transcriptions/*/evidence/` are crops of these scans (some with pitch guide lines added); we claim no rights in them either.
- This is our understanding, not legal advice.

### Corrections welcome

1. Open an issue naming the excerpt, bar, staff / part, beat, and the scan file and position (system / bar).
2. Or send a pull request: add an entry to the folder's `corrections.txt` (`<part> <bar>: <old tokens …> => <new tokens …>`, with the evidence in a comment above), run `python tools/export.py` and `python tools/check.py`, and commit the regenerated files. Old tokens must match the data exactly or the export stops with an error, so a correction never silently stops applying.
3. Please justify every change from the **public-domain scans**. Do not copy notes from copyrighted or share-alike digital editions or recordings; they may point you to a problem, but the fix must be visible in the scan.

The "known issues" section of each transcription README lists what is still incomplete or uncertain; that is where checking against the scans helps most.
