#!/usr/bin/env python3
"""Post-process a PDF to embed a /ViewerPreferences /Duplex hint.

Xdvipdfmx (the PDF driver XeLaTeX uses) does not provide a convenient
high-level knob for setting /ViewerPreferences in the PDF catalog.
This script post-processes a finished PDF and inserts the hint.

The hint tells duplex-capable printers to default to long-edge
binding (standard book orientation), reducing the chance that a
printer's default setting will flip alternate pages upside-down.

Usage:
    python3 scripts/add_duplex_hint.py historicity-feature.pdf
"""

import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, DictionaryObject


def add_hint(pdf_path: Path) -> None:
    r = PdfReader(str(pdf_path))
    w = PdfWriter(clone_from=r)

    vp = DictionaryObject()
    vp[NameObject('/Duplex')] = NameObject('/DuplexFlipLongEdge')
    vp[NameObject('/PickTrayByPDFSize')] = NameObject('/false')

    w._root_object[NameObject('/ViewerPreferences')] = vp

    with pdf_path.open('wb') as f:
        w.write(f)

    # Verify
    r2 = PdfReader(str(pdf_path))
    got = r2.trailer['/Root'].get('/ViewerPreferences', None)
    print(f'  {pdf_path.name}: {dict(got) if got else "NO VIEWER PREFS"}')


if __name__ == '__main__':
    targets = sys.argv[1:]
    if not targets:
        # Default targets
        root = Path(__file__).resolve().parent.parent
        targets = [
            root / 'historicity-feature.pdf',
            root / 'historicity.pdf',
            root / 'historicity-journal.pdf',
            root / 'historicity-supplement.pdf',
            root / 'historicity-baseline.pdf',
        ]
    for t in targets:
        t = Path(t)
        if t.exists():
            add_hint(t)
        else:
            print(f'  {t}: SKIP (not found)')
