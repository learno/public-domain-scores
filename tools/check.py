#!/usr/bin/env python3
"""Self-check of the exported files (standard library only).

检查 transcriptions/*/*.musicxml 的结构与每小节、每声部的时值总和，以及 *.mid 能否完整解析、音符开关是否配对。

    python tools/check.py

CC0 1.0 — see LICENSE.
"""
from __future__ import annotations

import struct
import sys
import xml.etree.ElementTree as ET
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TYPE_Q = {"whole": F(4), "half": F(2), "quarter": F(1), "eighth": F(1, 2), "16th": F(1, 4), "32nd": F(1, 8), "64th": F(1, 16)}


def check_musicxml(path: Path) -> tuple[list, dict]:
    errs = []
    root = ET.parse(path).getroot()
    if root.tag != "score-partwise":
        errs.append("root is not score-partwise")
    part_ids = [sp.get("id") for sp in root.iter("score-part")]
    parts = root.findall("part")
    if [p.get("id") for p in parts] != part_ids:
        errs.append("part-list ids do not match parts")
    st = dict(parts=len(parts), measures=None, heads=0, rests=0, trills=0, tremolo_notes=0, ties=0, measure_numbers=None)
    for part in parts:
        div = None
        beats = beat_type = None
        measures = part.findall("measure")
        nums = [m.get("number") for m in measures]
        if st["measures"] is None:
            st["measures"], st["measure_numbers"] = len(measures), (nums[0], nums[-1])
        elif st["measures"] != len(measures):
            errs.append(f"{part.get('id')}: measure count differs")
        open_ties = {}
        for m in measures:
            at = m.find("attributes")
            if at is not None:
                if at.find("divisions") is not None:
                    div = int(at.findtext("divisions"))
                if at.find("time") is not None:
                    beats, beat_type = int(at.findtext("time/beats")), int(at.findtext("time/beat-type"))
            full = F(beats * 4, beat_type) * div
            pos, voice_ends, prev_dur = F(0), [], None
            expected = None
            for el in m:
                if el.tag == "note":
                    dur = F(int(el.findtext("duration")))
                    is_chord = el.find("chord") is not None
                    rest = el.find("rest")
                    if rest is not None and rest.get("measure") == "yes":
                        pass
                    else:
                        typ = el.findtext("type")
                        q = TYPE_Q[typ]
                        nd = len(el.findall("dot"))
                        q = q * (2 - F(1, 2 ** nd))
                        tm = el.find("time-modification")
                        if tm is not None:
                            q = q * int(tm.findtext("normal-notes")) / int(tm.findtext("actual-notes"))
                        if q * div != dur:
                            errs.append(f"{part.get('id')} m{m.get('number')}: duration {dur} != type {typ}+{nd} dots")
                    if is_chord:
                        if dur != prev_dur:
                            errs.append(f"{part.get('id')} m{m.get('number')}: chord note duration mismatch")
                    else:
                        pos += dur
                        prev_dur = dur
                    if rest is not None:
                        st["rests"] += 1
                    else:
                        st["heads"] += 1
                        key = (el.findtext("staff") or "1", el.findtext("voice"), el.findtext("pitch/step"),
                               el.findtext("pitch/alter") or "0", el.findtext("pitch/octave"))
                        types = [t.get("type") for t in el.findall("tie")]
                        if "stop" in types:
                            if not open_ties.pop(key, None):
                                errs.append(f"{part.get('id')} m{m.get('number')}: tie stop without start {key}")
                        if "start" in types:
                            open_ties[key] = True
                            st["ties"] += 1
                        if el.find("notations/ornaments/trill-mark") is not None:
                            st["trills"] += 1
                        if el.find("notations/ornaments/tremolo") is not None or el.find("time-modification") is not None:
                            st["tremolo_notes"] += 1
                elif el.tag == "backup":
                    voice_ends.append(pos)
                    pos -= F(int(el.findtext("duration")))
                    if pos != 0:
                        errs.append(f"{part.get('id')} m{m.get('number')}: backup does not return to measure start")
                elif el.tag == "forward":
                    pos += F(int(el.findtext("duration")))
            voice_ends.append(pos)
            if m.get("implicit") == "yes":
                expected = voice_ends[0]
                if expected >= full:
                    errs.append(f"{part.get('id')} m{m.get('number')}: implicit (pickup) measure is not short")
            else:
                expected = full
            if any(v != expected for v in voice_ends):
                errs.append(f"{part.get('id')} m{m.get('number')}: voice lengths {[str(v / div) for v in voice_ends]} "
                            f"!= {expected / div} quarters")
        if open_ties:
            errs.append(f"{part.get('id')}: unterminated ties {list(open_ties)}")
    return errs, st


def vlq(d: bytes, i: int):
    v = 0
    while True:
        b = d[i]
        i += 1
        v = (v << 7) | (b & 0x7F)
        if not b & 0x80:
            return v, i


def check_midi(path: Path) -> tuple[list, dict]:
    errs = []
    d = path.read_bytes()
    if d[:4] != b"MThd":
        return ["no MThd"], {}
    hl, fmt, ntrk, ppq = struct.unpack(">IHHH", d[4:14])
    i = 8 + hl
    notes, end_tick, trk = 0, 0, 0
    while i < len(d):
        if d[i:i + 4] != b"MTrk":
            errs.append(f"bad chunk at {i}")
            break
        ln = struct.unpack(">I", d[i + 4:i + 8])[0]
        j, stop, tick, status, on, eot = i + 8, i + 8 + ln, 0, None, {}, False
        while j < stop:
            dt, j = vlq(d, j)
            tick += dt
            b = d[j]
            if b == 0xFF:
                typ = d[j + 1]
                l, j = vlq(d, j + 2)
                j += l
                if typ == 0x2F:
                    eot = True
                status = None
                continue
            if b in (0xF0, 0xF7):
                l, j = vlq(d, j + 1)
                j += l
                continue
            if b & 0x80:
                status = b
                j += 1
            elif status is None:
                errs.append(f"track {trk}: running status without status")
                break
            hi, ch = status & 0xF0, status & 0x0F
            nbytes = 1 if hi in (0xC0, 0xD0) else 2
            args = d[j:j + nbytes]
            j += nbytes
            if hi == 0x90 and args[1] > 0:
                k = (ch, args[0])
                on[k] = on.get(k, 0) + 1
                notes += 1
            elif hi == 0x80 or (hi == 0x90 and args[1] == 0):
                k = (ch, args[0])
                if not on.get(k):
                    errs.append(f"track {trk}: note off without on {k} at {tick}")
                else:
                    on[k] -= 1
        if j != stop:
            errs.append(f"track {trk}: length mismatch")
        if not eot:
            errs.append(f"track {trk}: missing end-of-track")
        if any(on.values()):
            errs.append(f"track {trk}: hanging notes {[k for k, v in on.items() if v]}")
        end_tick = max(end_tick, tick)
        i = stop
        trk += 1
    if trk != ntrk:
        errs.append(f"header says {ntrk} tracks, found {trk}")
    return errs, dict(format=fmt, tracks=trk, ppq=ppq, note_ons=notes, length_quarters=float(F(end_tick, ppq)))


def main() -> int:
    bad = 0
    for xmlp in sorted((ROOT / "transcriptions").glob("*/*.musicxml")):
        errs, st = check_musicxml(xmlp)
        print(f"{xmlp.relative_to(ROOT)}: {'OK' if not errs else 'FAIL'} — parts {st['parts']}, measures {st['measures']} "
              f"({st['measure_numbers'][0]}–{st['measure_numbers'][1]}), note heads {st['heads']}, rests {st['rests']}, "
              f"ties {st['ties']}, trill marks {st['trills']}, tremolo note heads {st['tremolo_notes']}")
        for e in errs[:20]:
            print("   ", e)
        bad += bool(errs)
    for midp in sorted((ROOT / "transcriptions").glob("*/*.mid")):
        errs, st = check_midi(midp)
        print(f"{midp.relative_to(ROOT)}: {'OK' if not errs else 'FAIL'} — {st}")
        for e in errs[:20]:
            print("   ", e)
        bad += bool(errs)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
