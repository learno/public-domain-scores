#!/usr/bin/env python3
"""Export the manual transcriptions to MusicXML (uncompressed .musicxml) and Standard MIDI.

把 transcriptions/<piece>/source.txt（人工转写原始数据）套上同目录 corrections.txt（修正清单）后，
导出 <piece>.musicxml 与 <piece>.mid。只用 Python 标准库。

    python tools/export.py            # 导出全部
    python tools/export.py <piece>    # 只导出一段

CC0 1.0 — see LICENSE.
"""
from __future__ import annotations

import re
import struct
import sys
import xml.etree.ElementTree as ET
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TR = ROOT / "transcriptions"
ENCODING_DATE = "2026-10-06"
RIGHTS = ("Transcription released under CC0 1.0 Universal (public domain dedication). "
          "The underlying composition is in the public domain.")

# ───────────────────────────── 各段的元数据 ─────────────────────────────
# staves: [(谱号, [source.txt 段名后缀 …]), …]；clef = G / F / C3（中音谱号）/ G8（低八度高音谱号）
# 可选 optional: bar_time={小节: (拍数, 拍值)} 个别小节换拍号；repeats=[小节 …] 在该小节末尾画反复记号
#   （下一小节开头画开始反复）；final_barline=True 末小节画终止线；tempo_words=None 不写速度文字。
# 移调乐器（part 级可选）：transpose=(diatonic, chromatic) 记谱 → 实际音高（如 G 调圆号 (-3, -5)），
#   source.txt 写记谱音高，MusicXML 加 <transpose>，MIDI 按实际音高；fifths=<记谱调号> 覆盖全曲调号。
#   double_bars=[小节 …] 在该小节末尾画双细线；chant=True 无量记谱（素歌）：音符不画符干、不连符杠，
#   拍号不打印（小节长度仍由 time / bar_time 决定，只用于排时间轴）。
#   clef_changes=[(小节, 拍内位置, 谱表号, 谱号), …]（part 级可选）：小节中途或末尾换谱号（拍内位置 = 小节长度即末尾）。
PIECES = {
    "vivaldi-winter-rv297": dict(
        prefix="winter",
        work="Il cimento dell'armonia e dell'inventione, Op. 8 — Concerto IV in F minor \"L'Inverno\", RV 297",
        movement="I. Allegro non molto (bars 1–18)",
        creators=[("composer", "Antonio Vivaldi")],
        source="Partbooks, Paris: engraved by Hue, 1739 (Bibliothèque nationale de France, Gallica ark:/12148/btv1b9062998d), "
               "via Wikimedia Commons. Manual transcription from scans/vivaldi-winter-rv297/hue_p017, p065, p099, p127, p153.",
        time=(4, 4), fifths=-4, mode="minor", bars=(1, 18), pickup=None,
        tempo_words="Allegro non molto", midi_qpm=96,
        parts=[
            dict(name="Violino Principale", abbr="Vl. princ.", program=41, staves=[("G", ["solo"])]),
            dict(name="Violino Primo", abbr="Vl. I", program=41, staves=[("G", ["vln1"])]),
            dict(name="Violino Secondo", abbr="Vl. II", program=41, staves=[("G", ["vln2"])]),
            dict(name="Alto Viola", abbr="Va.", program=42, staves=[("C3", ["vla"])]),
            dict(name="Organo e Violoncello", abbr="Org. e Vc.", program=43, staves=[("F", ["bc"])]),
        ],
    ),
    "vivaldi-winter-rv297-largo": dict(
        prefix="winter_largo",
        work="Il cimento dell'armonia e dell'inventione, Op. 8 — Concerto IV in F minor \"L'Inverno\", RV 297",
        movement="II. Largo (complete, bars 1–18)",
        creators=[("composer", "Antonio Vivaldi")],
        source="Partbooks, Paris: engraved by Hue, 1739 (Bibliothèque nationale de France, Gallica ark:/12148/btv1b9062998d), "
               "via Wikimedia Commons. Manual transcription from scans/vivaldi-winter-rv297/hue_p019, p066, p100, p128, p154.",
        time=(4, 4), fifths=-3, mode="major", bars=(1, 18), pickup=None, final_barline=True,
        tempo_words="Largo", midi_qpm=48, encoding_date="2026-10-18",
        parts=[
            dict(name="Violino Principale", abbr="Vl. princ.", program=41, staves=[("G", ["solo"])]),
            dict(name="Violino Primo", abbr="Vl. I", program=46, staves=[("G", ["vln1"])]),
            dict(name="Violino Secondo", abbr="Vl. II", program=46, staves=[("G", ["vln2"])]),
            dict(name="Alto Viola", abbr="Va.", program=42, staves=[("C3", ["vla"])]),
            dict(name="Organo e Violoncello", abbr="Org. e Vc.", program=43, staves=[("F", ["bc"])]),
        ],
    ),
    "vivaldi-autumn-rv293": dict(
        prefix="autumn",
        work="Il cimento dell'armonia e dell'inventione, Op. 8 — Concerto III in F major \"L'Autunno\", RV 293",
        movement="I. Allegro (bars 1–13, opening ritornello)",
        creators=[("composer", "Antonio Vivaldi")],
        source="Partbooks, Paris: engraved by Hue, 1739 (Bibliothèque nationale de France, Gallica ark:/12148/btv1b9062998d), "
               "via Wikimedia Commons. Manual transcription from scans/vivaldi-autumn-rv293/hue_p013, p063, p097, p125, p150.",
        time=(4, 4), fifths=-1, mode="major", bars=(1, 13), pickup=None,
        tempo_words="Allegro", midi_qpm=104, encoding_date="2026-10-18",
        parts=[
            dict(name="Violino Principale", abbr="Vl. princ.", program=41, staves=[("G", ["solo"])]),
            dict(name="Violino Primo", abbr="Vl. I", program=41, staves=[("G", ["vln1"])]),
            dict(name="Violino Secondo", abbr="Vl. II", program=41, staves=[("G", ["vln2"])]),
            dict(name="Alto Viola", abbr="Va.", program=42, staves=[("C3", ["vla"])]),
            dict(name="Organo e Violoncello", abbr="Org. e Vc.", program=43, staves=[("F", ["bc"])]),
        ],
    ),
    "wagner-walkure-ritt": dict(
        prefix="valkyries",
        work="Die Walküre, WWV 86B — Act III, Prelude (\"Walkürenritt\")",
        movement="Lebhaft — upbeat and bars 1–18 (reduction-based transcription)",
        creators=[("composer", "Richard Wagner")],
        source="Pitches read from the vocal score by Karl Klindworth (Mainz: B. Schott's Söhne; Internet Archive "
               "diewalkrevollstn00wagn), pp. 188–189; assignment of lines to instrument groups inferred from the full score "
               "(Mainz: B. Schott's Söhne; Internet Archive diewalkre00wagn_0), pp. 619–624, which was also used to correct bars 1–8 "
               "and 13–15. Not a full-score transcription.",
        time=(9, 8), fifths=2, mode="minor", bars=(0, 18), pickup=F(1, 2),
        tempo_words="Lebhaft", midi_qpm=114,
        parts=[
            dict(name="Woodwinds (trill / figure)", abbr="Ww.", program=74, staves=[("G", ["trill", "fig", "fig8va"])]),
            dict(name="Bassoons, Horns 1–4 (dotted rhythm)", abbr="Bsn., Hn. 1–4", program=71, staves=[("F", ["gallop"])]),
            dict(name="Horns 6 & 8, Bass Trumpet (theme)", abbr="Hn. 6, 8, B.Tpt.", program=61, staves=[("F", ["theme"])]),
            dict(name="Strings (runs)", abbr="Str.", program=49, staves=[("G", ["rush"])]),
        ],
    ),
    "strauss-zarathustra-op30": dict(
        prefix="zarathustra",
        work="Also sprach Zarathustra, Op. 30 — arranged for piano four hands by Otto Singer",
        movement="Introduction (Sonnenaufgang), bars 1–22",
        creators=[("composer", "Richard Strauss"), ("arranger", "Otto Singer")],
        source="Piano four hands by Otto Singer, Leipzig: Jos. Aibl (©1896; U.E. 1114), copy at the University of Toronto "
               "Music Library (Internet Archive alsosprachzarath00stra_0), Secondo p. 2, Primo p. 3. "
               "Secondo upper staff of bars 19–21 not transcribed (see README).",
        time=(4, 4), fifths=0, mode="major", bars=(1, 22), pickup=None,
        tempo_words="Sehr breit", midi_qpm=60,
        parts=[
            dict(name="Primo", abbr="I", program=1, staves=[("G", ["primo_rh"]), ("G", ["primo_lh"])]),
            dict(name="Secondo", abbr="II", program=1, staves=[("F", ["secondo_rh"]), ("F", ["secondo_lh"])]),
        ],
    ),
    "dowland-lachrimae": dict(
        prefix="lachrimae",
        work="The Second Booke of Songs or Ayres — II. Lachrimæ (\"Flow my teares\")",
        movement="Complete song (one stanza of music, 24 bars); Canto, Basso and lute tablature",
        creators=[("composer", "John Dowland")],
        source="John Dowland, The Second Booke of Songs or Ayres, London: Thomas Este for George Eastland, 1600, "
               "song II (Boston Public Library copy G.400.52, Internet Archive secondbookeofson00dowl), "
               "leaves n13 (Canto with French lute tablature) and n14 (Basso, printed rotated; last Canto/lute line). "
               "Lute part = sounding pitches decoded from the tablature (tenor G tuning, 7th course D).",
        time=(4, 2), fifths=0, mode="minor", bars=(1, 24), pickup=None,
        bar_time={23: (6, 2)}, repeats=[8, 16], final_barline=True,
        tempo_words=None, midi_qpm=100,
        parts=[
            dict(name="Canto", abbr="C.", program=54, staves=[("G", ["canto"])]),
            dict(name="Lute", abbr="Lute", program=25, staves=[("G8", ["lute"])]),
            dict(name="Basso", abbr="B.", program=43, staves=[("F", ["basso"])]),
        ],
    ),
    "handel-conquering-hwv63": dict(
        prefix="conquering",
        work="Judas Macchabaeus, HWV 63 — Part III, Full Chorus \"See, the conqu'ring hero comes\"",
        movement="Full Chorus (complete, 24 bars): orchestra, chorus and basso continuo",
        creators=[("composer", "George Frideric Handel")],
        source="Judas Macchabaeus: an oratorio, in score as it was originally perform'd, London: printed for "
               "William Randall, successor to the late Mr. J. Walsh, [1769] (Music Library, University of North "
               "Carolina at Chapel Hill; Internet Archive judasmacchabaeus00hand_0), pp. 175–176 (leaves n186–n187). "
               "Horns encoded at written pitch (horn in G). Figures of the basso continuo not encoded.",
        time=(2, 2), fifths=1, mode="major", bars=(1, 24), pickup=None,
        repeats=[8], final_barline=True,
        tempo_words=None, midi_qpm=112, encoding_date="2026-10-19",
        parts=[
            dict(name="Traversa e Violino I", abbr="Trav. e Vl. I", program=41, staves=[("G", ["fl_vln1"])]),
            dict(name="Traversa e Violino II", abbr="Trav. e Vl. II", program=41, staves=[("G", ["fl_vln2"])]),
            dict(name="Corno I in G", abbr="Cor. I", program=61, staves=[("G", ["horn1"])], fifths=0, transpose=(-3, -5)),
            dict(name="Corno II in G", abbr="Cor. II", program=61, staves=[("G", ["horn2"])], fifths=0, transpose=(-3, -5)),
            dict(name="Oboe I e II", abbr="Ob. I, II", program=69, staves=[("G", ["ob1", "ob2"])]),
            dict(name="Viola", abbr="Va.", program=42, staves=[("C3", ["viola"])]),
            dict(name="Soprano", abbr="S.", program=53, staves=[("G", ["soprano"])]),
            dict(name="Alto", abbr="A.", program=53, staves=[("G", ["alto"])]),
            dict(name="Tenor", abbr="T.", program=53, staves=[("G8", ["tenor"])]),
            dict(name="Bass", abbr="B.", program=53, staves=[("F", ["bass"])]),
            dict(name="Basso continuo", abbr="B.c.", program=43, staves=[("F", ["bc"])]),
        ],
    ),
    "chant-dies-irae": dict(
        prefix="diesirae",
        work="Missa pro defunctis — Sequentia \"Dies iræ\" (Gregorian chant)",
        movement="Stanzas 1–6 (melodies A A B B C C), as printed in the Liber Gradualis (1883)",
        creators=[("composer", "Anonymous (Gregorian chant, 13th century)")],
        source="Liber Gradualis a S. Gregorio Magno olim ordinatus … (Tournai: Desclée, Lefebvre et Soc., 1883; "
               "Solesmes edition prepared by Dom Joseph Pothier), Missa pro Defunctis, Sequentia, pp. [144]–[145] "
               "(BnF, département Musique, RES VMC MS-223, Gallica ark:/12148/btv1b104642876, images 764–765, "
               "via Wikimedia Commons). Square notation has no note values: every printed note is encoded as a "
               "quarter note, one bar per line of verse; neumes are encoded as slurs.",
        time=(8, 4), fifths=0, mode="dorian", bars=(1, 18), pickup=None,
        bar_time={2: (11, 4), 3: (10, 4), 4: (8, 4), 5: (11, 4), 6: (10, 4), 7: (13, 4), 8: (8, 4), 9: (13, 4),
                  10: (13, 4), 11: (8, 4), 12: (13, 4), 13: (12, 4), 14: (11, 4), 15: (10, 4), 16: (12, 4),
                  17: (11, 4), 18: (10, 4)},
        double_bars=[3, 6, 9, 12, 15, 18], chant=True, encoding_date="2026-10-19",
        tempo_words=None, midi_qpm=108,
        parts=[
            dict(name="Cantus", abbr="Cant.", program=53, staves=[("G", ["cantus"])]),
        ],
    ),
    "tchaikovsky-april-op37a": dict(
        prefix="april",
        work="The Seasons, Op. 37a (Op. 37bis) — No. 4 \"April\" (Perce-neige / Snowdrop)",
        movement="Allegretto con moto, e un poco rubato (complete: upbeat and bars 1–86)",
        creators=[("composer", "Pyotr Ilyich Tchaikovsky")],
        source="The Seasons, Op. 37 [37bis], edited and fingered by Louis Oesterle, New York: G. Schirmer, ©1899, plate 21360 "
               "(Harvard University copy digitized by Google, Internet Archive), pp. 16–19 "
               "(leaves n22–n25). Pedal marks, fingering and slurs not encoded.",
        time=(6, 8), fifths=-2, mode="major", bars=(0, 86), pickup=F(1, 2),
        double_bars=[58], final_barline=True,
        tempo_words="Allegretto con moto, e un poco rubato", midi_qpm=108, encoding_date="2026-10-19",
        parts=[
            dict(name="Piano", abbr="Pno.", program=1, staves=[("G", ["rh", "rh2"]), ("F", ["lh", "lh2"])],
                 # (小节, 拍内位置, 谱表, 谱号)：原谱的换谱号（拍内位置 = 小节长度 表示画在小节末尾）
                 clef_changes=[(0, 0.5, 2, "G"), (5, 3, 2, "F"),
                               (8, 3, 1, "F"), (12, 2.5, 1, "G"), (16, 3, 1, "F"), (20, 2.5, 1, "G"),
                               (32, 3, 2, "G"), (33, 3, 2, "F"), (34, 3, 2, "G"), (35, 3, 2, "F"),
                               (39, 3, 1, "F"), (40, 3, 1, "G"),
                               (48, 3, 2, "G"), (49, 3, 2, "F"), (50, 3, 2, "G"), (51, 3, 2, "F"),
                               (66, 3, 1, "F"), (70, 2.5, 1, "G"),
                               (78, 3, 2, "G"), (85, 3, 2, "F")]),
        ],
    ),
}

# ───────────────────────────── 读数据 ─────────────────────────────
TOK = re.compile(r"^([0-9.]+):([A-G])(#|b)?(-?\d)/(\d+(?:\.\d+)?)((?:tr|TA\d|TB\d|fer|[.>()])*)$")
STEP_PC = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}


class DataError(Exception):
    pass


def read_source(path: Path, prefix: str, syls: dict | None = None):
    """syls：若给出，收集 "!syl <part> <小节> <音节 …>" 行（歌词音节，依次对应该小节的各个音组），{(part, 小节): [音节 …]}。"""
    sects, notes, cur = {}, [], None
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        ln = raw.strip()
        if not ln or ln.startswith("#"):
            continue
        if ln.startswith("!syl "):
            _, part, bar, *words = ln.split()
            if syls is None:
                raise DataError(f"{path}:{n}: !syl lines are not used by this piece")
            if (part, int(bar)) in syls:
                raise DataError(f"{path}:{n}: duplicate !syl for {part} bar {bar}")
            syls[(part, int(bar))] = words
            continue
        if ln.startswith("!note "):
            _, part, bar, text = ln.split(None, 3)
            offset = F(0)
            m = re.match(r"^@([0-9.]+)\s+(.*)$", text)       # "!note <part> <bar> @<beat> <text>": 拍内位置
            if m:
                offset, text = F(m.group(1)), m.group(2)
            notes.append((part, int(bar), text, offset))
            continue
        if ln.startswith("[") and ln.endswith("]"):
            name = ln[1:-1]
            if not name.startswith(prefix + "."):
                raise DataError(f"{path}:{n}: section {name!r} does not start with {prefix!r}")
            cur = sects.setdefault(name[len(prefix) + 1:], {})
            continue
        if cur is None:
            raise DataError(f"{path}:{n}: data before first section")
        lab, _, rest = ln.partition(":")
        toks = rest.split()
        for t in toks:
            if not TOK.match(t):
                raise DataError(f"{path}:{n}: bad token {t!r}")
        cur.setdefault(int(lab), []).extend(toks)
    return sects, notes


def apply_corrections(path: Path, prefix: str, sects: dict) -> list:
    applied = []
    if not path.exists():
        return applied
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        ln = raw.strip()
        if not ln or ln.startswith("#"):
            continue
        m = re.match(r"^(\S+)\s+(-?\d+):\s*(.*?)\s*=>\s*(.*)$", ln)
        if not m:
            raise DataError(f"{path}:{n}: cannot parse correction line")
        part, bar, old, new = m.group(1), int(m.group(2)), m.group(3).split(), m.group(4).split()
        if part.startswith(prefix + "."):
            part = part[len(prefix) + 1:]
        if part not in sects:
            raise DataError(f"{path}:{n}: unknown part {part!r}")
        cur = sects[part].setdefault(bar, [])
        for t in old:
            if t not in cur:
                raise DataError(f"{path}:{n}: token {t!r} not found in {part} bar {bar} — correction no longer matches source")
            cur.remove(t)
        if new != ["-"]:
            for t in new:
                if not TOK.match(t):
                    raise DataError(f"{path}:{n}: bad new token {t!r}")
            cur.extend(new)
        cur.sort(key=lambda t: F(t.split(":")[0]))
        applied.append((part, bar, len(old), 0 if new == ["-"] else len(new)))
    return applied


class Note:
    __slots__ = ("on", "dur", "step", "alter", "octave", "stacc", "acc", "trill", "trem", "trem_beams", "slur_start", "slur_stop", "fermata")

    def __init__(self, on, dur, step, alter, octave, flags):
        self.on, self.dur, self.step, self.alter, self.octave = on, dur, step, alter, octave
        self.stacc = "." in flags
        self.acc = ">" in flags
        self.trill = "tr" in flags
        self.slur_start = "(" in flags          # 圆括号 = 连线（素歌里一个纽姆 / 一个音节上的音组）
        self.slur_stop = ")" in flags
        self.fermata = "fer" in flags
        m = re.search(r"T([AB])(\d)", flags)
        self.trem = m.group(1) if m else None
        self.trem_beams = int(m.group(2)) if m else 0

    @property
    def midi(self):
        return 12 * (self.octave + 1) + STEP_PC[self.step] + self.alter


def parse_token(t: str, bar_start: F) -> Note:
    on, step, acc, octv, dur, flags = TOK.match(t).groups()
    alter = {"#": 1, "b": -1, None: 0}[acc]
    return Note(bar_start + F(on), F(dur), step, alter, int(octv), flags)


# ───────────────────────────── 时间轴 ─────────────────────────────
class Grid:
    def __init__(self, cfg):
        num, den = cfg["time"]
        self.mlen = F(num * 4, den)
        self.first, self.last = cfg["bars"]
        self.pickup = cfg["pickup"]
        self.time = {b: tuple(t) for b, t in cfg.get("bar_time", {}).items()}
        self.base_time = tuple(cfg["time"])

    def time_sig(self, bar):
        return self.time.get(bar, self.base_time)

    def length(self, bar):
        if bar in self.time:
            num, den = self.time[bar]
            return F(num * 4, den)
        return self.pickup if (self.pickup is not None and bar == self.first) else self.mlen

    def start(self, bar):
        if self.time:
            return sum((self.length(b) for b in range(self.first, bar)), F(0))
        if self.pickup is None:
            return (bar - self.first) * self.mlen
        if bar == self.first:
            return F(0)
        return self.pickup + (bar - self.first - 1) * self.mlen

    def bars(self):
        return range(self.first, self.last + 1)


# 音符时值 → (type, dots)
TYPES = [(F(8), "breve", 0), (F(6), "whole", 1), (F(4), "whole", 0), (F(3), "half", 1), (F(2), "half", 0), (F(3, 2), "quarter", 1), (F(1), "quarter", 0),
         (F(3, 4), "eighth", 1), (F(1, 2), "eighth", 0), (F(3, 8), "16th", 1), (F(1, 4), "16th", 0),
         (F(3, 16), "32nd", 1), (F(1, 8), "32nd", 0), (F(1, 16), "64th", 0)]
TYPE_OF = {d: (t, k) for d, t, k in TYPES}
BEAMS = {"eighth": 1, "16th": 2, "32nd": 3, "64th": 4}


def split_dur(d: F) -> list:
    out = []
    while d > 0:
        for v, _, _ in TYPES:
            if v <= d:
                out.append(v)
                d -= v
                break
        else:
            raise DataError(f"duration remainder {d} not representable")
    return out


# ───────────────────────────── 事件分组 / 声部分配 ─────────────────────────────
class Item:
    """一个记谱事件：普通和弦（notes）或双音震音（a_notes ↔ b_notes）。"""

    def __init__(self, on, dur, notes=None, a=None, b=None, beams=0):
        self.on, self.dur = on, dur
        self.notes, self.a, self.b, self.beams = notes, a, b, beams

    @property
    def end(self):
        return self.on + self.dur

    @property
    def is_trem(self):
        return self.a is not None

    def heads(self):
        return (self.a + self.b) if self.is_trem else self.notes


def build_items(notes: list) -> list:
    normal, trem = {}, {}
    for n in notes:
        if n.trem:
            trem.setdefault((n.on, n.dur, n.trem_beams), {"A": [], "B": []})[n.trem].append(n)
        else:
            normal.setdefault((n.on, n.dur), []).append(n)
    items = [Item(on, d, notes=sorted(ns, key=lambda x: x.midi)) for (on, d), ns in normal.items()]
    for (on, d, bm), g in trem.items():
        if not g["A"] or not g["B"]:
            raise DataError(f"tremolo at {on} lacks TA or TB element")
        items.append(Item(on, d, a=sorted(g["A"], key=lambda x: x.midi), b=sorted(g["B"], key=lambda x: x.midi), beams=bm))
    items.sort(key=lambda it: (it.on, -it.dur))
    return items


def assign_voices(items: list) -> list:
    """贪心（best fit）：每个事件放进已空出来、且结束得最晚的声部，使连续的音型留在同一声部。返回 [[Item…], …]。"""
    voices = []
    for it in items:
        free = [v for v in voices if v[-1].end <= it.on]
        if free:
            max(free, key=lambda v: v[-1].end).append(it)      # max 遇到并列时取第一个（编号最小的声部）
        else:
            voices.append([it])
    return voices


# ───────────────────────────── MusicXML ─────────────────────────────
def sub(parent, tag, text=None, **attrib):
    e = ET.SubElement(parent, tag, {k.replace("_", "-"): str(v) for k, v in attrib.items()})
    if text is not None:
        e.text = str(text)
    return e


def lcm_div(values):
    from math import lcm
    d = 1
    for v in values:
        d = lcm(d, F(v).denominator)
    return d


def key_alter(fifths: int) -> dict:
    sharps, flats = "FCGDAEB", "BEADGCF"
    k = {s: 0 for s in STEP_PC}
    if fifths > 0:
        for s in sharps[:fifths]:
            k[s] = 1
    else:
        for s in flats[:-fifths]:
            k[s] = -1
    return k


def rest_pieces(t0: F, t1: F, beat: F, bar0: F) -> list:
    """把 [t0, t1) 的空隙按拍切开，再拆成可记谱的休止符。"""
    out, t = [], t0
    while t < t1:
        nb = bar0 + ((t - bar0) // beat + 1) * beat
        seg_end = min(t1, nb)
        # 若空隙从拍点开始且覆盖多拍，允许合并成更长休止（不跨半小节，简单处理：只合并整拍）
        if (t - bar0) % beat == 0 and t1 - t >= beat:
            whole_beats = ((t1 - t) // beat) * beat
            seg_end = t + whole_beats
        for d in split_dur(seg_end - t):
            out.append((t, d))
            t += d
    return out


def assign_syllables(key: str, part: str, bar: int, notes: list, words: list, lyrics: dict):
    """把一小节的音节依次放到各音组的第一个音上。音组 = 圆括号连线括起的几个音，或连线外的单个音；连线不跨小节。
    音节以 "-" 结尾表示词未完（下一音节同词）。"""
    starts, open_ = [], False
    for n in sorted(notes, key=lambda n: n.on):
        if n.slur_start and open_:
            raise DataError(f"{key}: {part} bar {bar}: slur opened twice")
        if not open_:
            starts.append(n)
        if n.slur_start:
            open_ = True
        if n.slur_stop:
            if not open_ or n.slur_start:
                raise DataError(f"{key}: {part} bar {bar}: slur stop without start")
            open_ = False
    if open_:
        raise DataError(f"{key}: {part} bar {bar}: slur not closed within the bar")
    if len(starts) != len(words):
        raise DataError(f"{key}: {part} bar {bar}: {len(words)} syllables for {len(starts)} note groups")
    cont = False
    for n, w in zip(starts, words):
        more = w.endswith("-")
        text = w[:-1] if more else w
        syl = ("middle" if cont else "begin") if more else ("end" if cont else "single")
        lyrics[id(n)] = (text, syl)
        cont = more
    if cont:
        raise DataError(f"{key}: {part} bar {bar}: last syllable ends with '-'")


def export_piece(key: str, cfg: dict) -> dict:
    d = TR / key
    syls = {}
    sects, notes_dir = read_source(d / "source.txt", cfg["prefix"], syls)
    corrections = apply_corrections(d / "corrections.txt", cfg["prefix"], sects)
    g = Grid(cfg)
    used = {s for p in cfg["parts"] for _, ss in p["staves"] for s in ss}
    unknown = set(sects) - used
    if unknown:
        raise DataError(f"{key}: sections not mapped to any staff: {sorted(unknown)}")
    num, den = cfg["time"]
    beat = F(3, 2) if (den == 8 and num % 3 == 0) else F(4, den)
    chant = cfg.get("chant", False)

    # 每个谱表的音符；lyrics: {id(Note): (音节文字, syllabic)}
    staves_notes, lyrics = [], {}
    for p in cfg["parts"]:
        per = []
        for clef, ss in p["staves"]:
            ns = []
            for s in ss:
                for bar, toks in sects.get(s, {}).items():
                    if bar < g.first or bar > g.last:
                        raise DataError(f"{key}: {s} bar {bar} outside excerpt")
                    bn = [parse_token(t, g.start(bar)) for t in toks]
                    ns += bn
                    if (s, bar) in syls:
                        assign_syllables(key, s, bar, bn, syls.pop((s, bar)), lyrics)
            per.append(ns)
        staves_notes.append(per)
    if syls:
        raise DataError(f"{key}: !syl lines for bars without notes: {sorted(syls)}")

    all_vals = [g.mlen] + ([g.pickup] if g.pickup else []) + [g.length(b) for b in g.time]
    for per in staves_notes:
        for ns in per:
            for n in ns:
                all_vals += [n.on, n.dur, n.dur / 2]
    divisions = max(lcm_div(all_vals), 8)

    root = ET.Element("score-partwise", version="4.0")
    work = sub(root, "work")
    sub(work, "work-title", cfg["work"])
    sub(root, "movement-title", cfg["movement"])
    ident = sub(root, "identification")
    for typ, name in cfg["creators"]:
        sub(ident, "creator", name, type=typ)
    sub(ident, "rights", RIGHTS)
    enc = sub(ident, "encoding")
    sub(enc, "software", "public-domain-scores tools/export.py")
    sub(enc, "encoding-date", cfg.get("encoding_date", ENCODING_DATE))
    sub(ident, "source", cfg["source"])
    # 不画系统分隔符（多声部总谱里系统之间的 "//" 记号；部分渲染器会把它画成一个孤立的斜线）
    dfl = sub(root, "defaults")
    sl = sub(dfl, "system-layout")
    sd = sub(sl, "system-dividers")
    sub(sd, "left-divider", print_object="no")
    sub(sd, "right-divider", print_object="no")
    pl = sub(root, "part-list")
    for i, p in enumerate(cfg["parts"], 1):
        sp = sub(pl, "score-part", id=f"P{i}")
        sub(sp, "part-name", p["name"])
        sub(sp, "part-abbreviation", p["abbr"])
        si = sub(sp, "score-instrument", id=f"P{i}-I1")
        sub(si, "instrument-name", p["name"])
        mi = sub(sp, "midi-instrument", id=f"P{i}-I1")
        sub(mi, "midi-channel", i if i < 10 else i + 1)
        sub(mi, "midi-program", p["program"])

    stats = dict(measures=len(g.bars()), heads_logical=0, heads_written=0, rests=0, ties=0, lyrics=0,
                 corrections=corrections, divisions=divisions)
    midi_tracks = []

    for pi, (p, per) in enumerate(zip(cfg["parts"], staves_notes), 1):
        part = sub(root, "part", id=f"P{pi}")
        nst = len(per)
        staff_voices = []
        for si, ns in enumerate(per):
            stats["heads_logical"] += len(ns)
            items = build_items(ns)
            vs = assign_voices(items)
            if len(vs) > 4:
                raise DataError(f"{key}: too many voices on {p['name']} staff {si + 1}")
            staff_voices.append(vs)
            midi_tracks.append((f"{p['name']}" + (f" (staff {si + 1})" if nst > 1 else ""),
                                pi - 1 if pi < 10 else pi, p["program"], items,
                                p.get("transpose", (0, 0))[1]))
        pfifths = p.get("fifths", cfg["fifths"])
        kalt_p = key_alter(pfifths)
        # 换谱号（part 级可选）：clef_changes=[(小节, 拍内位置, 谱表号 1…, 谱号), …]，写在该谱表第一个声部里
        clef_chg = {}
        for cb, cbeat, cst, cclef in p.get("clef_changes", ()):
            clef_chg.setdefault((cb, cst - 1), []).append((F(cbeat), cclef))
        for bar in g.bars():
            b0, blen = g.start(bar), g.length(bar)
            b1 = b0 + blen
            m = sub(part, "measure", number=bar)
            if g.pickup is not None and bar == g.first:
                m.set("implicit", "yes")
            if bar - 1 in cfg.get("repeats", ()):
                bl = sub(m, "barline", location="left")
                sub(bl, "bar-style", "heavy-light")
                sub(bl, "repeat", direction="forward")
            if bar == g.first:
                at = sub(m, "attributes")
                sub(at, "divisions", divisions)
                k = sub(at, "key")
                sub(k, "fifths", pfifths)
                sub(k, "mode", cfg["mode"])
                t = sub(at, "time", **({"print_object": "no"} if chant else {}))
                sub(t, "beats", num)
                sub(t, "beat-type", den)
                if nst > 1:
                    sub(at, "staves", nst)
                for si, (clef, _) in enumerate(p["staves"], 1):
                    c = sub(at, "clef", **({"number": si} if nst > 1 else {}))
                    sign, line = {"G": ("G", 2), "G8": ("G", 2), "F": ("F", 4), "C3": ("C", 3)}[clef]
                    sub(c, "sign", sign)
                    sub(c, "line", line)
                    if clef == "G8":
                        sub(c, "clef-octave-change", -1)
                if "transpose" in p:
                    tr = sub(at, "transpose")
                    sub(tr, "diatonic", p["transpose"][0])
                    sub(tr, "chromatic", p["transpose"][1])
                if pi == 1 and cfg["tempo_words"] is None:
                    sub(m, "sound", tempo=cfg["midi_qpm"])
                elif pi == 1:
                    dr = sub(m, "direction", placement="above")
                    dt = sub(dr, "direction-type")
                    sub(dt, "words", cfg["tempo_words"], font_weight="bold")
                    sub(dr, "sound", tempo=cfg["midi_qpm"])
            elif g.time_sig(bar) != g.time_sig(bar - 1):
                at = sub(m, "attributes")
                t = sub(at, "time", **({"print_object": "no"} if chant else {}))
                sub(t, "beats", g.time_sig(bar)[0])
                sub(t, "beat-type", g.time_sig(bar)[1])
            for si, (clef, ss) in enumerate(p["staves"]):
                for part_name, nbar, text, offset in notes_dir:
                    if part_name in ss and nbar == bar:
                        dr = sub(m, "direction", placement="above" if si == 0 else "below")
                        dt = sub(dr, "direction-type")
                        sub(dt, "words", text, font_style="italic", font_size="8")
                        if offset:
                            sub(dr, "offset", int(offset * divisions))
                        if nst > 1:
                            sub(dr, "staff", si + 1)
            first_voice_written = False
            for si, vs in enumerate(staff_voices):
                # 本小节本谱表的变音记号状态（按时间顺序，跨声部共享）
                heads = []
                plans = []
                busy = [vi for vi, v in enumerate(vs) if any(it.on < b1 and it.end > b0 for it in v)]
                for vi, v in enumerate(vs):
                    segs = []
                    its = [it for it in v if it.on < b1 and it.end > b0]
                    # 本小节空着的声部不写；整个谱表都空时只在第一声部写整小节休止
                    if not its and (busy or vi > 0):
                        continue
                    t = b0
                    for it in its:
                        if it.on > t:
                            segs += [("rest", rt, rd) for rt, rd in rest_pieces(t, it.on, beat, b0)]
                        s0, s1 = max(it.on, b0), min(it.end, b1)
                        if it.is_trem:
                            if it.on < b0 or it.end > b1:
                                raise DataError(f"{key}: tremolo crosses barline at bar {bar}")
                            segs.append(("trem", it, s0, s1))
                        else:
                            pieces = split_dur(s1 - s0)
                            tt = s0
                            for k_, pd in enumerate(pieces):
                                tie_stop = tt > it.on
                                tie_start = tt + pd < it.end
                                segs.append(("note", it, tt, pd, tie_start, tie_stop))
                                tt += pd
                        t = s1
                    if not its:
                        segs.append(("mrest",))
                    elif t < b1:
                        segs += [("rest", rt, rd) for rt, rd in rest_pieces(t, b1, beat, b0)]
                    plans.append((vi, segs))
                    for sg in segs:
                        if sg[0] == "note":
                            for n in sg[1].notes:
                                heads.append((sg[2], n, sg[5]))
                        elif sg[0] == "trem":
                            for n in sg[1].a:
                                heads.append((sg[2], n, False))
                            for n in sg[1].b:
                                heads.append((sg[2] + sg[1].dur / 2, n, False))
                # 变音记号
                state, show = {}, {}
                for t_, n, tied in sorted(heads, key=lambda h: (h[0], h[1].midi)):
                    keyk = (n.step, n.octave)
                    cur = state.get(keyk, kalt_p[n.step])
                    if not tied and n.alter != cur:
                        show[(id(n), t_)] = {1: "sharp", -1: "flat", 0: "natural", 2: "double-sharp", -2: "flat-flat"}[n.alter]
                    state[keyk] = n.alter
                pend = sorted(clef_chg.pop((bar, si), []))
                for vi, segs in plans:
                    voice = si * 4 + vi + 1
                    if first_voice_written:
                        sub(m, "backup").append(_dur(blen, divisions))
                    first_voice_written = True
                    beams = {} if chant else _beam_plan(segs, beat, b0)
                    for idx, sg in enumerate(segs):
                        if pend and vi == plans[0][0]:
                            st_ = b0 if sg[0] == "mrest" else (sg[1] if sg[0] == "rest" else sg[2])
                            while pend and st_ >= b0 + pend[0][0]:
                                _clef_attr(m, pend.pop(0)[1], si + 1 if nst > 1 else None)
                        if sg[0] == "mrest":
                            ne = sub(m, "note")
                            sub(ne, "rest", measure="yes")
                            sub(ne, "duration", int(blen * divisions))
                            sub(ne, "voice", voice)
                            if nst > 1:
                                sub(ne, "staff", si + 1)
                            stats["rests"] += 1
                        elif sg[0] == "rest":
                            _, rt, rd = sg
                            ne = sub(m, "note")
                            if vi > 0:                     # 第二声部起的补位休止不打印
                                ne.set("print-object", "no")
                            sub(ne, "rest")
                            sub(ne, "duration", int(rd * divisions))
                            sub(ne, "voice", voice)
                            typ, dots = TYPE_OF[rd]
                            sub(ne, "type", typ)
                            for _ in range(dots):
                                sub(ne, "dot")
                            if nst > 1:
                                sub(ne, "staff", si + 1)
                            stats["rests"] += 1
                        elif sg[0] == "note":
                            _, it, tt, pd, tstart, tstop = sg
                            typ, dots = TYPE_OF[pd]
                            for j, n in enumerate(it.notes):
                                ne = sub(m, "note")
                                if j:
                                    sub(ne, "chord")
                                _pitch(ne, n)
                                sub(ne, "duration", int(pd * divisions))
                                if tstop:
                                    sub(ne, "tie", type="stop")
                                if tstart:
                                    sub(ne, "tie", type="start")
                                sub(ne, "voice", voice)
                                sub(ne, "type", typ)
                                for _ in range(dots):
                                    sub(ne, "dot")
                                acc = show.get((id(n), tt))
                                if acc:
                                    sub(ne, "accidental", acc)
                                if chant:
                                    sub(ne, "stem", "none")
                                if nst > 1:
                                    sub(ne, "staff", si + 1)
                                if j == 0 and beams.get(idx):
                                    for lvl, val in beams[idx]:
                                        sub(ne, "beam", val, number=lvl)
                                nots = []
                                if tstop:
                                    nots.append(("tied", "stop"))
                                if tstart:
                                    nots.append(("tied", "start"))
                                    stats["ties"] += 1
                                if j == 0 and n.slur_start and not tstop:
                                    nots.append(("slur", "start"))
                                if j == 0 and n.slur_stop and not tstart:
                                    nots.append(("slur", "stop"))
                                if nots or (n.trill and not tstop) or ((n.stacc or n.acc) and not tstop) or (n.fermata and not tstart):
                                    no = sub(ne, "notations")
                                    for tag, tv in nots:
                                        if tag == "slur":
                                            sub(no, tag, type=tv, number=1)
                                        else:
                                            sub(no, tag, type=tv)
                                    if n.trill and not tstop and j == 0:
                                        orn = sub(no, "ornaments")
                                        sub(orn, "trill-mark")
                                    if (n.stacc or n.acc) and not tstop and j == 0:
                                        ar = sub(no, "articulations")
                                        if n.acc:
                                            sub(ar, "accent")
                                        if n.stacc:
                                            sub(ar, "staccato")
                                    if n.fermata and not tstart and j == 0:   # 延长记号画在连音线的最后一段
                                        sub(no, "fermata", type="upright")
                                if j == 0 and not tstop and id(n) in lyrics:
                                    text, syl = lyrics[id(n)]
                                    ly = sub(ne, "lyric", number=1)
                                    sub(ly, "syllabic", syl)
                                    sub(ly, "text", text)
                                    stats["lyrics"] += 1
                                stats["heads_written"] += 1
                        elif sg[0] == "trem":
                            _, it, s0, s1 = sg
                            half = it.dur / 2
                            typ, dots = TYPE_OF[it.dur]
                            for which, grp in (("start", it.a), ("stop", it.b)):
                                tpos = s0 if which == "start" else s0 + half
                                for j, n in enumerate(grp):
                                    ne = sub(m, "note")
                                    if j:
                                        sub(ne, "chord")
                                    _pitch(ne, n)
                                    sub(ne, "duration", int(half * divisions))
                                    sub(ne, "voice", voice)
                                    sub(ne, "type", typ)
                                    for _ in range(dots):
                                        sub(ne, "dot")
                                    acc = show.get((id(n), tpos))
                                    if acc:
                                        sub(ne, "accidental", acc)
                                    tm = sub(ne, "time-modification")
                                    sub(tm, "actual-notes", 2)
                                    sub(tm, "normal-notes", 1)
                                    if nst > 1:
                                        sub(ne, "staff", si + 1)
                                    # 八分及更短的震音音符：实符杠连接两组，tremolo 只记额外的震音线
                                    nb = BEAMS.get(typ, 0)
                                    if j == 0:
                                        for lvl in range(1, nb + 1):
                                            sub(ne, "beam", "begin" if which == "start" else "end", number=lvl)
                                        no = sub(ne, "notations")
                                        orn = sub(no, "ornaments")
                                        sub(orn, "tremolo", it.beams - nb, type=which)
                                    stats["heads_written"] += 1
                    if pend and vi == plans[0][0]:          # 小节末尾的换谱号
                        for _, cclef in pend:
                            _clef_attr(m, cclef, si + 1 if nst > 1 else None)
                        pend = []
                # 一个谱表都没有声部内容时（不会发生：第一声部总会写）
            if not first_voice_written:
                raise DataError(f"{key}: empty measure {bar}")
            if bar in cfg.get("repeats", ()):
                bl = sub(m, "barline", location="right")
                sub(bl, "bar-style", "light-heavy")
                sub(bl, "repeat", direction="backward")
            elif bar in cfg.get("double_bars", ()):
                bl = sub(m, "barline", location="right")
                sub(bl, "bar-style", "light-light")
            elif bar == g.last and cfg.get("final_barline"):
                bl = sub(m, "barline", location="right")
                sub(bl, "bar-style", "light-heavy")
    ET.indent(root, space="  ")
    body = ET.tostring(root, encoding="unicode")
    xml = ('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
           '<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" '
           '"http://www.musicxml.org/dtds/partwise.dtd">\n' + body + "\n")
    (d / f"{key}.musicxml").write_text(xml, encoding="utf-8", newline="\n")
    (d / f"{key}.mid").write_bytes(build_midi(cfg, g, midi_tracks))
    return stats


def _clef_attr(m, clef: str, number):
    at = sub(m, "attributes")
    c = sub(at, "clef", **({"number": number} if number else {}))
    sign, line = {"G": ("G", 2), "G8": ("G", 2), "F": ("F", 4), "C3": ("C", 3)}[clef]
    sub(c, "sign", sign)
    sub(c, "line", line)
    if clef == "G8":
        sub(c, "clef-octave-change", -1)


def _dur(d: F, divisions: int):
    e = ET.Element("duration")
    e.text = str(int(d * divisions))
    return e


def _pitch(ne, n: Note):
    pe = sub(ne, "pitch")
    sub(pe, "step", n.step)
    if n.alter:
        sub(pe, "alter", n.alter)
    sub(pe, "octave", n.octave)


def _beam_plan(segs, beat, b0) -> dict:
    """同一拍内相邻的八分及更短音符连成符杠。返回 {seg 下标: [(level, begin/continue/end/hook), …]}。"""
    plan = {}
    groups, cur, cur_beat = [], [], None
    for idx, sg in enumerate(segs):
        if sg[0] == "note":
            typ = TYPE_OF[sg[3]][0]
            nb = BEAMS.get(typ, 0)
            bi = (sg[2] - b0) // beat
            if nb and cur and bi == cur_beat:
                cur.append((idx, nb))
                continue
            if cur:
                groups.append(cur)
            cur, cur_beat = ([(idx, nb)], bi) if nb else ([], None)
        else:
            if cur:
                groups.append(cur)
            cur, cur_beat = [], None
    if cur:
        groups.append(cur)
    for grp in groups:
        if len(grp) < 2:
            continue
        for lvl in range(1, 5):
            k = 0
            while k < len(grp):
                if grp[k][1] < lvl:
                    k += 1
                    continue
                j = k
                while j + 1 < len(grp) and grp[j + 1][1] >= lvl:
                    j += 1
                if j == k:
                    if lvl > 1:
                        val = "backward hook" if k > 0 else "forward hook"
                        plan.setdefault(grp[k][0], []).append((lvl, val))
                else:
                    for q in range(k, j + 1):
                        val = "begin" if q == k else ("end" if q == j else "continue")
                        plan.setdefault(grp[q][0], []).append((lvl, val))
                k = j + 1
    return plan


# ───────────────────────────── MIDI ─────────────────────────────
PPQ = 480


def vlq(n: int) -> bytes:
    out = [n & 0x7F]
    n >>= 7
    while n:
        out.append((n & 0x7F) | 0x80)
        n >>= 7
    return bytes(reversed(out))


def track_chunk(events) -> bytes:
    """events: [(tick, order, bytes)]"""
    data, last = b"", 0
    for tick, _, ev in sorted(events, key=lambda e: (e[0], e[1])):
        data += vlq(tick - last) + ev
        last = tick
    end = max([e[0] for e in events], default=0)
    data += vlq(end - last) + b"\xff\x2f\x00"
    return b"MTrk" + struct.pack(">I", len(data)) + data


def build_midi(cfg, g: Grid, tracks) -> bytes:
    num, den = cfg["time"]
    us = round(60_000_000 / cfg["midi_qpm"])
    title = (cfg["work"] + " — " + cfg["movement"]).encode("utf-8")
    cond = [(0, 0, b"\xff\x03" + vlq(len(title)) + title),
            (0, 1, b"\xff\x51\x03" + us.to_bytes(3, "big")),
            (0, 2, b"\xff\x58\x04" + bytes([num, {2: 1, 4: 2, 8: 3, 16: 4}[den], 36 if (den == 8 and num % 3 == 0) else 24, 8])),
            (0, 3, b"\xff\x59\x02" + struct.pack(">bB", cfg["fifths"], 1 if cfg["mode"] == "minor" else 0))]
    for b in g.bars():                      # 个别小节换拍号（含换回原拍号）
        if b > g.first and g.time_sig(b) != g.time_sig(b - 1):
            bn, bd = g.time_sig(b)
            cond.append((int(g.start(b) * PPQ), 2, b"\xff\x58\x04" + bytes([bn, {2: 1, 4: 2, 8: 3, 16: 4}[bd], 24, 8])))
    chunks = [track_chunk(cond)]

    def tk(t: F) -> int:
        return int(t * PPQ)
    for name, chan, program, items, trans in tracks:
        nm = name.encode("utf-8")
        ev = [(0, 0, b"\xff\x03" + vlq(len(nm)) + nm), (0, 1, bytes([0xC0 | chan, program - 1]))]
        for it in items:
            if it.is_trem:
                step = F(1, 2 ** (it.beams - 1)) / 2 if it.beams else F(1, 8)   # 3 条 → 32 分音符 = 1/8 拍
                t, k = it.on, 0
                while t < it.end:
                    for n in (it.a if k % 2 == 0 else it.b):
                        ev.append((tk(t), 2, bytes([0x90 | chan, n.midi + trans, 76])))
                        ev.append((tk(t + step * F(9, 10)), 1, bytes([0x80 | chan, n.midi + trans, 0])))
                    t += step
                    k += 1
            else:
                for n in it.notes:
                    gate = F(1, 2) if n.stacc else F(19, 20)
                    vel = 92 if n.acc else 80
                    ev.append((tk(n.on), 2, bytes([0x90 | chan, n.midi + trans, vel])))
                    ev.append((tk(n.on + n.dur * gate), 1, bytes([0x80 | chan, n.midi + trans, 0])))
        chunks.append(track_chunk(ev))
    head = b"MThd" + struct.pack(">IHHH", 6, 1, len(chunks), PPQ)
    return head + b"".join(chunks)


def main(argv):
    keys = argv[1:] or list(PIECES)
    for k in keys:
        if k not in PIECES:
            print(f"unknown piece {k!r}; choose from {', '.join(PIECES)}", file=sys.stderr)
            return 2
    try:
        for k in keys:
            st = export_piece(k, PIECES[k])
            print(f"{k}: {st['measures']} measures, {st['heads_logical']} notes in data "
                  f"({st['heads_written']} written note heads, {st['ties']} ties, {st['rests']} rests), "
                  f"divisions={st['divisions']}, corrections applied: {len(st['corrections'])}")
    except DataError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
