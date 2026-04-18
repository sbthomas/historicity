# The Evidentiary Status of the Historical Jesus

**A Critical Assessment**

Stan Thomas — Independent Researcher, St.\ George, Utah
ORCID: [0000-0002-8828-7856](https://orcid.org/0000-0002-8828-7856)

---

## Summary

This paper subjects the mainstream scholarly consensus on the historicity of Jesus of Nazareth to an evidence-first examination, evaluating each category of source material on its own terms: the Pauline epistles, the canonical Gospels, non-canonical Christian texts, the non-Christian references in Josephus and Tacitus, and the archaeological and administrative record.

The argument, in brief:

1. The Pauline corpus primarily describes a revelatory, celestial soteriological figure, though a small number of passages admit historical readings that any mythicist model must address.
2. The Gospel narratives are demonstrably constructed from Hebrew Bible templates and Hellenistic mythological conventions.
3. Non-Christian attestation is weaker than typically claimed, though it confirms the early existence of Christian traditions about a historical founder.
4. The conspicuous absence of contemporaneous documentation across multiple independent traditions constitutes disconfirming evidence.
5. The source trajectory runs from mythic to historical — the reverse of what the standard model predicts.
6. The single passage most frequently cited as decisive for historicity — Galatians 1:19, "James the brother of the Lord" — is more ambiguous than the consensus acknowledges when read in its full Pauline context.

The responsible conclusion is that the evidence does not establish the historicity of Jesus with the confidence the consensus claims, that the mythicist hypothesis is a serious alternative that survives scrutiny of its own weaknesses (Galatians 4:4, Romans 1:3, the 1 Corinthians 15 witness list, the speed of euhemerization), and that the prevailing consensus is sustained partly by institutional and methodological inertia rather than by evidential weight alone.

**Keywords:** historical Jesus, mythicism, Pauline epistles, Gospel sources, criterion of embarrassment, dying-and-rising gods, Josephus, *adelphos tou kyriou*, euhemerization, historiography.

## Repository contents

| File | Description |
|---|---|
| `historicity.tex` | LaTeX source of the main paper |
| `historicity.bib` | BibTeX bibliography (~60 entries) |
| `historicity.pdf` | Compiled PDF of the current draft |
| `historicity-supplement.tex` | Supplement 1: Pauline occurrences (XeLaTeX) |
| `historicity-supplement.pdf` | Compiled: colour-coded *adelph-* occurrences in the seven undisputed letters |
| `supplement_body.tex` | Generated body of supplement 1 (full Greek text with markup) |
| `historicity-baseline.tex` | Supplement 2: corpus-linguistic baseline (XeLaTeX) |
| `historicity-baseline.pdf` | Compiled: *adelph-* in contemporary non-Christian Greek (base rate for Bayesian prior) |
| `scripts/build_supplement.py` | Generator that produces `supplement_body.tex` from SBLGNT |
| `scripts/sblgnt/` | SBL Greek New Testament text of the seven letters (CC BY 4.0) |
| `baseline/` | Corpus-linguistic baseline study: classified samples (212 tokens across six non-Christian corpora), Wilson-CI statistics script, classification scheme |

## Building from source

### Main paper

Standard pdfLaTeX toolchain — any recent TeX Live or MacTeX distribution will work.

```bash
pdflatex historicity
bibtex   historicity
pdflatex historicity
pdflatex historicity
```

Or with `latexmk`:

```bash
latexmk -pdf historicity
```

### Supplements

Both supplements require **XeLaTeX** (for Unicode Greek text) and the
**STIX Two Text** font (ships with macOS; available via `texlive-fonts-extra`
on Linux or directly from <https://github.com/stipub/stixfonts>).

```bash
# Supplement 1: Pauline adelph- occurrences, colour-coded
xelatex historicity-supplement
xelatex historicity-supplement

# Supplement 2: contemporary-Greek baseline study
xelatex historicity-baseline
xelatex historicity-baseline
```

To regenerate `supplement_body.tex` from the SBLGNT source (normally only
needed if the classification table in `scripts/build_supplement.py` changes):

```bash
python3 scripts/build_supplement.py
```

To recompute the baseline statistics (per-bucket A/B/C/D/E proportions with
Wilson 95% CIs):

```bash
python3 baseline/aggregate_stats.py
```

### Package requirements

The main-paper preamble uses `natbib`, `hyperref`, `titlesec`, `fancyhdr`, `setspace`, `booktabs`, `enumitem`, `xcolor`, `amsmath`, `amssymb`, and `geometry` (all standard). Three further packages — `csquotes`, `epigraph`, and `textgreek` — are used if available and transparently fall back to built-in equivalents if not, so the document compiles on minimal TeX installations. The supplement additionally needs `fontspec` (XeLaTeX-only).

## Citing this paper

```bibtex
@unpublished{Thomas2026Historicity,
  author = {Stan Thomas},
  title  = {The Evidentiary Status of the Historical Jesus: A Critical Assessment},
  year   = {2026},
  note   = {Draft. ORCID: 0000-0002-8828-7856},
  url    = {https://github.com/sbthomas/historicity}
}
```

## License

This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/). See [`LICENSE`](LICENSE) for the full text. You are free to share and adapt the material with appropriate attribution; commercial use is not permitted.

## Acknowledgments

This paper benefited from extensive critical dialogue conducted with Claude (Anthropic), which served as adversarial interlocutor and peer reviewer throughout the analytical process. The arguments and conclusions are the author's own.
