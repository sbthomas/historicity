#!/usr/bin/env python3
"""Pre-rotate every other page 180° to compensate for broken HP-driver duplex.

Some HP multifunction printers on Linux (including the Color LaserJet
Pro MFP 3301 series) render every even page with an unwanted 180°
rotation when duplex printing is enabled, regardless of whether
DuplexNoTumble (long-edge) or DuplexTumble (short-edge) is selected.
Single-sided printing is unaffected.

The workaround is to pre-rotate even pages in the PDF itself, so the
driver's unwanted rotation cancels the PDF's pre-rotation and pages
come out right-side up.

Usage:
    python3 scripts/pre_rotate_for_duplex.py historicity-feature.pdf

Writes historicity-feature-duplex.pdf next to the input. Print that
file with either duplex mode; the driver's mis-rotation will cancel.

This file is ONLY for printing to a printer with the broken duplex
behavior. Viewing it on screen will show even pages upside-down —
that is intentional.
"""

import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def pre_rotate(src_path: Path, dst_path: Path) -> None:
    r = PdfReader(str(src_path))
    w = PdfWriter()

    for i, page in enumerate(r.pages):
        # Page indexing: humans say "page 1" is the first. In Python
        # that's index 0. We rotate the *even* printed pages — pages
        # 2, 4, 6... — which are indices 1, 3, 5...
        page_number = i + 1  # human numbering
        if page_number % 2 == 0:
            page.rotate(180)
        w.add_page(page)

    with dst_path.open('wb') as f:
        w.write(f)

    print(f'  {src_path.name} → {dst_path.name}')
    print(f'    {len(r.pages)} pages total; '
          f'even pages ({", ".join(str(i) for i in range(2, len(r.pages)+1, 2))}) '
          f'pre-rotated 180°')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    for arg in sys.argv[1:]:
        src = Path(arg)
        if not src.exists():
            print(f'  {src}: not found, skipping')
            continue
        dst = src.with_name(src.stem + '-duplex' + src.suffix)
        pre_rotate(src, dst)
