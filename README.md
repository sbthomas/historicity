# The Evidentiary Status of the Historical Jesus

**A Critical Assessment**

Stan Thomas — Independent Researcher, St. George, Utah
ORCID: [0000-0002-8828-7856](https://orcid.org/0000-0002-8828-7856)

---

## Summary

This paper subjects the mainstream scholarly consensus on the
historicity of Jesus of Nazareth to an evidence-first examination.
It evaluates each category of source material on its own terms — the
Pauline epistles, the canonical Gospels, non-canonical Christian
texts, the non-Christian references in Josephus and Tacitus, the
rabbinic and Mandaean traditions, the archaeological record, and the
documentary traditions that should contain references but do not.

The argument, in brief:

1. **The Pauline corpus** primarily describes a revelatory celestial
   figure assembled from pre-Christian Jewish apocalyptic-mystical
   sources (the Danielic Son of Man, Philo's Logos, angelomorphic
   mediators, the Suffering Servant). The revelatory mechanism Paul
   himself claims — *apokalypsis* plus scriptural exegesis — is the
   attested method of Second Temple Jewish mystical-visionary
   communities and does not require a recent historical subject. A
   small number of Pauline passages (Gal 4:4, Rom 1:3, 1 Cor 15
   witness list) admit historical readings that any mythic-origin
   scenario must address.
2. **The Gospel narratives** are demonstrably constructed from
   Hebrew Bible templates. This establishes that the Gospels are
   *not* independent historical testimony — it does not prove the
   non-existence of any historical subject, but it shifts the
   evidentiary burden entirely to non-Gospel sources.
3. **Non-Christian attestation** is weaker than typically claimed.
   The *Testimonium Flavianum* is partially or wholly interpolated.
   The Josephan James passage is widely accepted but contested. The
   rabbinic and Mandaean traditions post-date and depend on the
   Christian narrative. Tacitus almost certainly derives from
   Christian informants.
4. **Cumulative silence** across multiple independent documentary
   channels (Philo, Justus of Tiberias, Mishnah, Roman records)
   constitutes qualitatively real disconfirming evidence, though
   difficult to quantify precisely.
5. **The source trajectory** runs from mythic to historical — from
   Paul's cosmic Christ through Mark's minimal narrative to the
   elaborated biographies. The *speed* of the Pauline-to-Markan
   transition remains a genuine challenge for mythic-origin scenarios.
6. **The *adelphos tou kyriou* passages** (Gal 1:19, 1 Cor 9:5) are
   more ambiguous than the consensus acknowledges. Within Paul's own
   corpus, *adelphos* designates a fellow community-member in 117 of
   121 occurrences and zero clearly-biological uses outside these
   two contested phrases. Greek religious-associative inscriptions
   attest *adelphoi tou* [patron figure] as a well-formed community-
   title construction (Harland 2005, Kloppenborg-Ascough 2011), making
   the community-title reading the formally normal reading for this
   construction.

The considered conclusion is that the evidence does not establish the
historicity of Jesus with the confidence the consensus claims, that
the mythic-origin hypothesis — particularly in its Jewish-apocalyptic
rather than pagan-mystery-cult form — is a serious alternative that
survives scrutiny of its weaknesses, and that the scholarly consensus
is sustained partly by institutional and methodological inertia. A
Bayesian sensitivity analysis included as supplementary material
suggests that under plausible point estimates and a neutral prior,
the posterior probability of historicity lands in the open-question
range (0.23–0.39).

**Keywords:** historical Jesus, mythicism, Pauline epistles,
corpus linguistics, *adelphos tou kyriou*, Jewish apocalyptic
mysticism, Greek religious associations, Bayesian historiography.

---

## Document structure

The project consists of a main paper and two supplementary documents,
plus reproducible computational artefacts.

### Main paper

`historicity.tex` / `historicity.pdf` (~84 pages). Twelve sections:

1. Introduction: the question and its stakes
2. Methodological preliminaries (Bayesian framework, silence principle,
   criteria of authenticity, comparative existence-question cases)
3. The Pauline corpus (dating, interpolation, text-critical and
   stylometric analysis, *adelphos tou kyriou*)
4. The Gospel sources (literary construction, scriptural templating)
5. Non-canonical Christian sources
6. Non-Christian attestation (Josephus, Tacitus, Pliny-Suetonius,
   rabbinic tradition, Mandaean tradition, archaeological substrate)
7. The argument from silence
8. Prior sources: the Jewish-apocalyptic matrix (Danielic Son of Man,
   Philo's Logos, revelatory-ascent mechanism, Davidic messianism,
   Hellenistic resonances as secondary context)
9. Source trajectory: from mythic to historical
10. Sociology of the consensus
11. A constructive mythic-origin scenario
12. Conclusion

### Supplement 1: Pauline *adelph-* occurrences

`historicity-supplement.tex` / `historicity-supplement.pdf` (~41
pages). Reproduces the full SBLGNT Greek text of the seven undisputed
Pauline letters with every occurrence of *adelphos*, *adelphē*,
*pseudadelphos*, and *philadelphia* colour-coded by classification
(A = community / B = biological / C = disputed / D = ethnic-covenantal
/ E = metaphorical). Total: 121 tokens, 117 A / 0 B / 3 C / 1 D / 0 E.

### Supplement 2: Corpus-linguistic baseline

`historicity-baseline.tex` / `historicity-baseline.pdf` (~10 pages).
Establishes the baseline rate of community-sense *adelphos* in
contemporary non-Christian Greek by random sampling 405 tokens across
six corpora (papyri 100 BCE – 70 CE, LXX, Philo, Josephus, pre-Pauline
literary, Hellenistic literary). The three literary buckets were
expanded to n=100 each in the n=100 expansion pass; papyri, LXX, and
Josephus remain at n=35 pending external re-sampling. Baseline A-rate
is 0.7% (95% Wilson CI [0.3%, 2.2%]). Includes an appendix of 25 Greek
inscriptions from voluntary religious associations where *adelphoi*
explicitly designates fellow members (compiled from Harland's
Associations in the Greco-Roman World database).

### Journal-length version

`historicity-journal.tex` / `historicity-journal.pdf` (~20 pages, ~5K
words). A compressed presentation of the core argument, suitable for
submission to venues such as *Journal for the Study of the Historical
Jesus*, *History of Religions*, *The Journal of Religion*, or *Method
& Theory in the Study of Religion*. References the full-length paper
and supplements for detailed evidence.

---

## Repository contents

| Path | Description |
|---|---|
| `historicity.tex` / `.pdf` / `.bib` | Main paper and bibliography |
| `historicity-journal.tex` / `.pdf` | Journal-length compressed version (~5K words, 20 pp) |
| `historicity-supplement.tex` / `.pdf` | Pauline *adelph-* supplement |
| `supplement_body.tex` | Generated Greek body of supplement 1 |
| `historicity-baseline.tex` / `.pdf` | Baseline + inscriptional appendix |
| `scripts/build_supplement.py` | Generator for supplement 1 |
| `scripts/sblgnt/` | SBLGNT Greek text, seven letters (CC BY 4.0) |
| `scripts/stylometry.py` | Rolling function-word stylometric analysis |
| `scripts/bayesian_sensitivity.py` | Bayesian sensitivity computation |
| `baseline/` | Classified samples, aggregate statistics, analytical reports |
| `baseline/stylometry_report.md` | Stylometric analysis output |
| `baseline/bayesian_report.md` | Bayesian sensitivity output |
| `TODO.md` | Comprehensive research-directions inventory |
| `GLOSSARY.md` | Technical terms, Greek transliterations, and classification scheme |
| `RESPONSES.md` | Anticipated reviewer critiques with cross-referenced responses |
| `FALSIFICATION.md` | Explicit falsification conditions in both directions |
| `PRESENTATION.md` | Slide-format summary (Pandoc-convertible) |
| `LICENSE` | CC BY-NC 4.0 |

---

## Building from source

### Main paper

Standard pdfLaTeX toolchain (TeX Live or MacTeX):

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

Both supplements require **XeLaTeX** for Unicode Greek text and the
**STIX Two Text** font (ships with macOS; available via
`texlive-fonts-extra` on Linux or directly from
<https://github.com/stipub/stixfonts>).

```bash
xelatex historicity-supplement && xelatex historicity-supplement
xelatex historicity-baseline   && xelatex historicity-baseline
```

### Reproducing the empirical analyses

```bash
# Regenerate the Pauline supplement body from SBLGNT
python3 scripts/build_supplement.py

# Recompute baseline A/B/C/D/E proportions with Wilson 95% CIs
python3 baseline/aggregate_stats.py

# Run the stylometric analysis on Paul
python3 scripts/stylometry.py

# Run the Bayesian sensitivity analysis
python3 scripts/bayesian_sensitivity.py
```

All four produce deterministic output files under `baseline/` that
are checked into the repository.

### Package requirements

The main-paper preamble uses `natbib`, `hyperref`, `titlesec`,
`fancyhdr`, `setspace`, `booktabs`, `enumitem`, `xcolor`, `amsmath`,
`amssymb`, `geometry`. Three further packages — `csquotes`,
`epigraph`, `textgreek` — are used if available and gracefully fall
back to built-in equivalents if not. The supplements additionally
need `fontspec` (XeLaTeX-only).

---

## Engagement with the scholarly literature

The paper explicitly engages with recent work in the field:

- **Mainstream historicist**: Ehrman, Allison, Fredriksen, Bond,
  Crossley & Keith, Wright, Meier, Crossan, Sanders, Dunn.
- **Recent Paul-skeptical**: Vinzent 2023, Klinghardt 2015,
  BeDuhn 2013, Livesey 2024, Detering 1995.
- **Associations / *adelphoi***: Harland 2003, 2005;
  Kloppenborg & Ascough 2011–2020.
- **Mythicist / minimalist**: Carrier, Doherty, Lataster, Price,
  Brodie.
- **Jewish apocalyptic / mystical**: Scholem, Morton Smith, Rowland,
  Segal, Gruenwald, Schäfer, Elior, Collins, Knohl, Boyarin.
- **Second Temple / Septuagint context**: Philo commentators
  (Sterling), comparative religious-studies (Fredriksen,
  Thompson, Finkelstein & Silberman).
- **Philosophy of history**: Tucker 2004 on independence in
  Bayesian historical inference.
- **Comparative existence questions**: Beard, Wiseman, Higham,
  Finkelberg, West, Graham, Cartledge, Dever, Riedweg.

The bibliography now has ~110 entries.

---

## Outstanding work and future research

See [`TODO.md`](TODO.md) for a comprehensive inventory of directions
for future work. Items completed during the current development pass
include:

- Epigraphic *adelphoi* study (via Harland corpus)
- Comparative existence-question case studies (§2.5)
- Jewish mystical-ascent engagement (§8.2)
- Text-critical cluster analysis of contested passages (§3.1)
- Stylometric analysis of Paul (§3.1 + `scripts/stylometry.py`)
- Rabbinic counter-narrative engagement (§6.5)
- Mandaean tradition engagement (§6.6)
- Archaeological substrate analysis (§6.7)
- Bayesian sensitivity analysis (§2.2 + `scripts/bayesian_sensitivity.py`)

Items remaining that primarily require external collaboration:

- Inter-rater agreement for the A/B/C/D/E classification
- External expert review (ideally Harland, Allison, Fredriksen on
  the historicist side; Carrier, Lataster on the mythicist side)
- Preprint deposit and DOI assignment
- A compressed journal-length version (~8–12K words)
- Random-sampled inscriptional baseline (complement to Harland-curated)

---

## Citing this paper

```bibtex
@unpublished{Thomas2026Historicity,
  author = {Stan Thomas},
  title  = {The Evidentiary Status of the Historical Jesus:
            A Critical Assessment},
  year   = {2026},
  note   = {Draft. ORCID: 0000-0002-8828-7856},
  url    = {https://github.com/sbthomas/historicity}
}
```

---

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial 4.0 International
License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).
See [`LICENSE`](LICENSE) for the full text. You are free to share and
adapt the material with appropriate attribution; commercial use is
not permitted.

---

## Acknowledgments

This paper benefited from extensive critical dialogue conducted with
Claude (Anthropic), which served as adversarial interlocutor and peer
reviewer throughout the analytical process. The arguments and
conclusions are the author's own.
