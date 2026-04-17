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
| `historicity.tex` | LaTeX source (single-file `article` class) |
| `historicity.bib` | BibTeX bibliography (~60 entries) |
| `historicity.pdf` | Compiled PDF of the current draft |

## Building from source

Standard LaTeX toolchain — any recent TeX Live or MacTeX distribution will work.

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

### Package requirements

The preamble uses `natbib`, `hyperref`, `titlesec`, `fancyhdr`, `setspace`, `booktabs`, `enumitem`, `xcolor`, `amsmath`, `amssymb`, and `geometry` (all standard). Three further packages — `csquotes`, `epigraph`, and `textgreek` — are used if available and transparently fall back to built-in equivalents if not, so the document compiles on minimal TeX installations.

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

## Acknowledgments

This paper benefited from extensive critical dialogue conducted with Claude (Anthropic), which served as adversarial interlocutor and peer reviewer throughout the analytical process. The arguments and conclusions are the author's own.
