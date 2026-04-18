#!/usr/bin/env python3
"""Process SBLGNT text of the 7 undisputed Paulines and produce a LaTeX body
with every adelph- family token wrapped in \\adeA{}, \\adeB{}, or \\adeC{}
per the classification table.

Reads Greek text from ./sblgnt/<Book>.txt (relative to this script).
Writes the LaTeX body to ../supplement_body.tex.

The SBLGNT source text is distributed under Creative Commons Attribution 4.0
International (CC BY 4.0). Upstream: https://github.com/LogosBible/SBLGNT
"""

import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SBL_DIR = SCRIPT_DIR / 'sblgnt'
OUTPUT = SCRIPT_DIR.parent / 'supplement_body.tex'

BOOKS = [
    ("Rom",    "Romans",         "Πρὸς Ῥωμαίους"),
    ("1Cor",   "1 Corinthians",  "Πρὸς Κορινθίους α\u0384"),
    ("2Cor",   "2 Corinthians",  "Πρὸς Κορινθίους β\u0384"),
    ("Gal",    "Galatians",      "Πρὸς Γαλάτας"),
    ("Phil",   "Philippians",    "Πρὸς Φιλιππησίους"),
    ("1Thess", "1 Thessalonians","Πρὸς Θεσσαλονικεῖς α\u0384"),
    ("Phlm",   "Philemon",       "Πρὸς Φιλήμονα"),
]

# Classification: "BookCode Ch:Vs" -> list of A/B/C, one per adelph- token
# in order of appearance within the verse.
CLASSIFICATIONS = {
    # Romans
    "Rom 1:13": ["A"], "Rom 7:1": ["A"], "Rom 7:4": ["A"],
    "Rom 8:12": ["A"], "Rom 8:29": ["A"],
    "Rom 9:3": ["D"],           # "brothers according to the flesh" — ethnic/covenantal (fellow Israelites)
    "Rom 10:1": ["A"], "Rom 11:25": ["A"], "Rom 12:1": ["A"],
    "Rom 12:10": ["A"],         # philadelphia
    "Rom 14:10": ["A", "A"], "Rom 14:13": ["A"], "Rom 14:15": ["A"],
    "Rom 14:21": ["A"], "Rom 15:14": ["A"], "Rom 15:30": ["A"],
    "Rom 16:1": ["A"], "Rom 16:14": ["A"],
    "Rom 16:15": ["C"],         # "Nereus and his sister" — possibly biological
    "Rom 16:17": ["A"], "Rom 16:23": ["A"],
    # 1 Corinthians
    "1Cor 1:1": ["A"], "1Cor 1:10": ["A"], "1Cor 1:11": ["A"],
    "1Cor 1:26": ["A"], "1Cor 2:1": ["A"], "1Cor 3:1": ["A"],
    "1Cor 4:6": ["A"], "1Cor 5:11": ["A"], "1Cor 6:5": ["A"],
    "1Cor 6:6": ["A", "A"], "1Cor 6:8": ["A"], "1Cor 7:12": ["A"],
    "1Cor 7:14": ["A"], "1Cor 7:15": ["A", "A"],
    "1Cor 7:24": ["A"], "1Cor 7:29": ["A"], "1Cor 8:11": ["A"],
    "1Cor 8:12": ["A"], "1Cor 8:13": ["A", "A"],
    "1Cor 9:5": ["A", "C"],     # ἀδελφὴν γυναῖκα (A) + ἀδελφοὶ τοῦ κυρίου (C)
    "1Cor 10:1": ["A"], "1Cor 11:33": ["A"], "1Cor 12:1": ["A"],
    "1Cor 14:6": ["A"], "1Cor 14:20": ["A"], "1Cor 14:26": ["A"],
    "1Cor 14:39": ["A"], "1Cor 15:1": ["A"], "1Cor 15:6": ["A"],
    "1Cor 15:50": ["A"], "1Cor 15:58": ["A"], "1Cor 16:11": ["A"],
    "1Cor 16:12": ["A", "A"], "1Cor 16:15": ["A"], "1Cor 16:20": ["A"],
    # 2 Corinthians
    "2Cor 1:1": ["A"], "2Cor 1:8": ["A"], "2Cor 2:13": ["A"],
    "2Cor 8:1": ["A"], "2Cor 8:18": ["A"], "2Cor 8:22": ["A"],
    "2Cor 8:23": ["A"], "2Cor 9:3": ["A"], "2Cor 9:5": ["A"],
    "2Cor 11:9": ["A"], "2Cor 11:26": ["A"],  # pseudadelphois
    "2Cor 12:18": ["A"], "2Cor 13:11": ["A"],
    # Galatians
    "Gal 1:2": ["A"], "Gal 1:11": ["A"],
    "Gal 1:19": ["C"],          # THE disputed passage — "James the brother of the Lord"
    "Gal 2:4": ["A"],           # pseudadelphous
    "Gal 3:15": ["A"], "Gal 4:12": ["A"], "Gal 4:28": ["A"],
    "Gal 4:31": ["A"], "Gal 5:11": ["A"], "Gal 5:13": ["A"],
    "Gal 6:1": ["A"], "Gal 6:18": ["A"],
    # Philippians
    "Phil 1:12": ["A"], "Phil 1:14": ["A"], "Phil 2:25": ["A"],
    "Phil 3:1": ["A"], "Phil 3:13": ["A"], "Phil 3:17": ["A"],
    "Phil 4:1": ["A"], "Phil 4:8": ["A"], "Phil 4:21": ["A"],
    # 1 Thessalonians
    "1Thess 1:4": ["A"], "1Thess 2:1": ["A"], "1Thess 2:9": ["A"],
    "1Thess 2:14": ["A"], "1Thess 2:17": ["A"], "1Thess 3:2": ["A"],
    "1Thess 3:7": ["A"], "1Thess 4:1": ["A"], "1Thess 4:6": ["A"],
    "1Thess 4:9": ["A"],         # philadelphias
    "1Thess 4:10": ["A", "A"], "1Thess 4:13": ["A"], "1Thess 5:1": ["A"],
    "1Thess 5:4": ["A"], "1Thess 5:12": ["A"], "1Thess 5:14": ["A"],
    "1Thess 5:25": ["A"], "1Thess 5:26": ["A"], "1Thess 5:27": ["A"],
    # Philemon
    "Phlm 1:1": ["A"], "Phlm 1:2": ["A"], "Phlm 1:7": ["A"],
    "Phlm 1:16": ["A"], "Phlm 1:20": ["A"],
}

ADELPH = re.compile(r'\w*λφ\w*', re.UNICODE)
# SBLGNT editorial sigla — strip for readability
SIGLA = re.compile(r'[⸀⸁⸂⸃⸄⸅⸆⸇⸈⸉⸊⸋⸌⸍⸎⸏]')

def process_verse(ref: str, greek: str) -> str:
    greek = SIGLA.sub('', greek).strip()
    if ref not in CLASSIFICATIONS:
        return greek
    classes = CLASSIFICATIONS[ref]
    matches = list(ADELPH.finditer(greek))
    if len(matches) != len(classes):
        raise ValueError(
            f"{ref}: expected {len(classes)} adelph- tokens, found {len(matches)}: "
            f"{[m.group() for m in matches]}"
        )
    out_parts = []
    prev_end = 0
    for m, cls in zip(matches, classes):
        out_parts.append(greek[prev_end:m.start()])
        out_parts.append(f'\\ade{cls}{{{m.group()}}}')
        prev_end = m.end()
    out_parts.append(greek[prev_end:])
    return ''.join(out_parts)

def parse_line(line: str):
    """Parse one SBLGNT line. Return (book, ch, vs, greek) or None."""
    line = line.rstrip()
    if not line or '\t' not in line:
        return None
    ref, greek = line.split('\t', 1)
    # ref format: "Rom 1:1" or "1Cor 1:1"
    parts = ref.rsplit(' ', 1)
    if len(parts) != 2 or ':' not in parts[1]:
        return None
    book = parts[0]
    ch, vs = parts[1].split(':')
    return (book, int(ch), int(vs), greek)

def build_body() -> str:
    sbldir = SBL_DIR
    out = []
    for code, eng, grk in BOOKS:
        out.append(f'\\booksection{{{eng}}}{{{grk}}}')
        txt = (sbldir / f'{code}.txt').read_text(encoding='utf-8')
        current_ch = None
        for line in txt.splitlines():
            parsed = parse_line(line)
            if parsed is None:
                continue
            book, ch, vs, greek = parsed
            ref = f'{book} {ch}:{vs}'
            try:
                processed = process_verse(ref, greek)
            except ValueError as e:
                print(f'WARN: {e}')
                processed = SIGLA.sub('', greek).strip()
            if ch != current_ch:
                out.append(f'\n\\chapheader{{{ch}}}')
                current_ch = ch
            out.append(f'\\vs{{{vs}}}~{processed}')
        out.append('')
    return '\n'.join(out)

if __name__ == '__main__':
    body = build_body()
    # Normalise the SBLGNT right-single-quotation variant (U+02BC) to the
    # standard typographic apostrophe so XeLaTeX renders it cleanly.
    body = body.replace('\u02bc', '\u2019')
    OUTPUT.write_text(body, encoding='utf-8')
    print(f'Wrote {OUTPUT} ({len(body)} chars)')
