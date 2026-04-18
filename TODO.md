# Research TODO

A comprehensive list of lines of work that would extend and strengthen this
study.  Organized by priority and by research-program type.  Each item
notes why it matters, current state, and rough scope estimate.

Legend: **[P1]** = do before next submission attempt; **[P2]** = strengthen
substantially, can follow initial submission; **[P3]** = long-term research
program; **[QA]** = quality assurance / publication-readiness;
**[DONE]** = substantively addressed in current paper and supplements.

## Summary of completion status

Ten of the fifteen substantive items have been addressed in the paper
and supplements. Remaining items require external collaboration or
large-scale mechanical extension.

**Done** (in the paper / supplements / scripts):
- #1 Epigraphic *adelphoi* study (Harland inscriptional appendix)
- #2 Comparative existence-question case-study section (§2.5)
- #3 Jewish mystical-ascent engagement (§8.2)
- #4 Text-critical cluster analysis of contested passages (§3.1)
- #7 Journal-length version (*historicity-journal.tex*)
- #8 Stylometric analysis (*scripts/stylometry.py* + §3.1)
- #9 Rabbinic counter-narrative engagement (§6.5)
- #12 Bayesian network formal model (*scripts/bayesian_sensitivity.py* + §2.2)
- #15 Archaeological substrate analysis (§6.7)
- #17 Mandaean tradition engagement (§6.6)

**Requires external collaboration or process steps**:
- #5 Inter-rater agreement for classification (external coder)
- #10 Stylometric analysis at larger scale (extended feature sets, formal statistical testing)
- #19 Patristic citation-chain analysis (partially covered in §3.1; full survey deferred)
- #20 Expanded baseline sampling to n=100/bucket
- #24 External expert review (Allison, Fredriksen, Harland, Carrier)
- #25 External expert review (continued)
- #26 Preprint deposit and DOI assignment

---

## Part I. Closing gaps in the current paper

### 1. Epigraphic *adelphoi* study **[P1]**
Sample Greek inscriptions systematically for *adelphos/adelphoi* uses to
close the single biggest methodological gap in the baseline supplement.
Currently the supplement excludes inscriptions — which, per Harland 2005,
is precisely where community-sense *adelphoi* concentrates.
- **Sources**: Packard Humanities Institute Greek Inscriptions database;
  Kloppenborg-Ascough *Greco-Roman Associations* (4 vols, 2011-2020);
  Searchable Greek Inscriptions (epigraphy.packhum.org).
- **Target**: n=40-50 random-sampled occurrences; classify A/B/C/D/E.
- **Output**: update to `historicity-baseline.tex`; shift quantitative
  argument from "we disavow 103× because inscriptions are missing" to
  "here are inscriptions, corrected ratio is X."
- **Scope**: 2-4 weeks of focused work.

### 2. Comparative "did X exist?" case-study section **[P1]**
Add a new section (probably §2 or new §10) analyzing the methodological
landscape of existence-questions for other putatively-historical figures:
King Arthur, William Tell, Pythagoras, Lycurgus of Sparta, Moses,
Laozi, Homer, Romulus, the Hebrew patriarchs, Valentinus, Robin Hood,
the Trojan War.
- What diagnostic criteria have been *decisive* in positively resolving
  existence? (Pilate — archaeology.)
- What criteria decisively negative? (Moses — Egyptian silence.)
- Where does Jesus's evidentiary profile land in this landscape?
- **Scope**: 6,000-8,000 words; draws on existing literature (Anthony,
  Thompson, Zecharia Sitchin as counter-example of how NOT to do it).

### 3. Jewish mystical-ascent engagement (*apokalypsis* mechanism) **[P1]**
Add a subsection to §3 or §7.1 on the mechanism by which Paul's Christ-
knowledge was generated: Merkabah and Hekhalot traditions,
*Apocalypse of Abraham*, *Ascension of Isaiah* (already discussed),
2 Corinthians 12:2 ascent language.
- **Key literature**: Gershom Scholem, *Major Trends in Jewish Mysticism*;
  Morton Smith, *Jesus the Magician*; Christopher Rowland, *The Open
  Heaven*; Alan Segal, *Paul the Convert*; Ithamar Gruenwald,
  *Apocalyptic and Merkavah Mysticism*; Rachel Elior; Peter Schäfer.
- **Purpose**: ground the mythic-origin scenario's "revelation +
  scripture" claim in a concrete, well-attested Jewish procedural
  framework.
- **Scope**: 3,000-4,000 words; one new subsection.

### 4. Text-critical cluster analysis of contested passages **[P1]**
For each passage the paper concedes is difficult for mythicism
(Gal 1:19, Rom 1:3, 1 Cor 15:3-8, Gal 4:4), conduct a systematic
manuscript-variant analysis: what do P46, P45, Sinaiticus, Vaticanus,
Alexandrinus, the Old Latin, the Peshitta, and Marcion's reconstructed
text say? Where do variants cluster? What do patristic citations from
the second century attest?
- **Sources**: Nestle-Aland 28 apparatus; Tischendorf; NA28 critical
  apparatus; Metzger/Ehrman *Text of the New Testament*; David Trobisch.
- **Expected finding**: some contested clauses may show variant-distribution
  patterns suggesting late insertion; others are firmly attested.
- **Scope**: 2-3 weeks; supplementary table, narrative discussion
  1,500-2,500 words.

### 5. Inter-rater agreement for classification **[P1]**
Secure at least one external coder (ideally a Greek-literate scholar
who is neutral on historicity) to independently classify a subset
(n=50-100) of the baseline tokens and compute Cohen's κ for inter-rater
agreement.  Currently the baseline supplement explicitly flags
single-coder classification as its principal methodological limitation.
- **Purpose**: answer a certain class of reviewer objection directly.
- **Scope**: 1-2 weeks coordination + whoever the coder is.

### 6. Fact-check all citations against primary sources **[QA]**
Verify every citation in `historicity.bib` against the original source:
correct publisher, correct date, accurate page references where given.
Several entries have previously had year-mismatch issues (now fixed).
- **Scope**: 1 day.

### 7. Draft journal-length version **[P1]**
The current paper is ~65 pages.  Most journals accept 8,000-12,000
words.  Draft a journal-length version that preserves the core argument
while citing the full-length version + supplements as supporting
material.  Likely target: a philosophy-of-history or classical-studies
venue rather than a NT-studies venue.
- **Scope**: 2-3 weeks of careful compression.

---

## Part II. Genuinely novel evidentiary channels

### 8. Mandaean tradition engagement **[P2]**
The Mandaeans are a surviving pre-Christian or early-Christian-era
religious community (now primarily in Iraq/Iran diaspora) centered on
John the Baptist and containing independent traditions about Jesus
(*Ginza Rabba*, *Book of John*, *Canonical Prayerbook*).  They are
almost entirely ignored by the historical-Jesus field.
- **Key scholars**: Kurt Rudolph, *Mandaeism*; Jorunn Jacobsen Buckley,
  *The Mandaeans*; Edmondo Lupieri, *The Mandaeans*; Charles Häberl.
- **Research question**: what do the Mandaean Jesus-references imply
  about a possible independent non-Christian memory of a first-century
  figure?  How are they to be dated?  What is their evidential status?
- **This is the single most underexplored witness the paper has not
  engaged.**
- **Scope**: 4-6 weeks if done seriously; could be a standalone paper.

### 9. Rabbinic counter-narrative engagement **[P2]**
*Toledoth Yeshu* traditions; *Minuth* passages (b.Sanh.43a, 107b;
b.Shab.104b); Celsus's Jewish source in Origen *Contra Celsum*.
- **Recent work**: Peter Schäfer, *Jesus in the Talmud* (2007);
  Meerson & Schäfer (eds.), *Toledot Yeshu: The Life Story of Jesus*
  (Princeton 2014).
- **Research question**: do these traditions preserve independent
  polemical memory, or do they originate as responses to Christian
  claims?  The answer has real implications for the non-Christian
  attestation question (§6).
- **Scope**: 2-3 weeks; one new subsection to §6.

### 10. Stylometric analysis of Pauline interpolation **[P2]**
Modern NLP methods applied to authentic Paul to detect interpolation
layers.  Specifically: does the "brother of the Lord" clause in
Gal 1:19 stylistically cluster with surrounding Pauline text, or with
a different authorial layer?
- **Methods**: burrows delta, rolling stylometry, supervised
  classification.  Tools: R `stylo` package; Python
  `scikit-learn` / `transformers`.
- **Training corpus**: the 7 undisputed Paulines vs. the 6 deutero-
  Paulines (known authorship distinction).
- **Target passages**: Gal 1:19, 1 Thess 2:14-16, 1 Cor 15:3-11,
  Rom 1:3-4, Rom 13:1-7, 1 Cor 14:34-35.
- **Scope**: substantial; possibly a standalone paper.

### 11. Semantic-vector analysis of Pauline registers **[P2]**
Train embeddings on a comprehensive corpus of Koine Greek literature
and locate Paul's vocabulary-space.  Does Paul cluster with Hellenistic-
Jewish (Philo), Stoic-cosmopolitan (Epictetus), documentary-letter
(papyri), religious-associative (inscriptions), or apocalyptic-Jewish
(1 Enoch, Qumran)?
- **Tools**: Classical Language Toolkit (cltk); Ancient Greek word
  embeddings (available from Diorisis, Perseus).
- **Purpose**: directly address the Harland-type critique by giving a
  quantitative answer to "what kind of Greek is Paul writing?"
- **Scope**: possibly a standalone computational-linguistics paper.

### 12. Bayesian network formal model **[P2/P3]**
Construct a formal Bayesian network for the historicity question where
nodes are hypotheses and evidence pieces and edges capture conditional
dependencies (textual dependence, source-dependence, etc.).  Compute
posteriors under alternative edge structures.
- **Motivation**: Carrier's multiplication approach assumes independence
  that doesn't hold; Tucker 2004 notes this explicitly.  A formal
  network would correct it.
- **Tools**: NetworkX, PyMC3 or similar.
- **Scope**: substantial conceptual work on what the edges should be;
  probably a standalone methodological paper.

### 13. Comparative mythography: Raglan and Rank patterns **[P3]**
Lord Raglan's 22-point mythic hero pattern and Otto Rank's
mythic-hero typology have been applied to Jesus informally (Carrier
touches on them).  A rigorous quantitative application: apply the
patterns to a controlled set of known-historical figures
(Alexander, Caesar, Socrates, Augustus) and known-mythic figures
(Romulus, Heracles, Oedipus) and to Jesus, and compute score
distributions.
- **Purpose**: does Jesus's pattern-score match historical or mythic
  figures more closely?  This is a specific, quantifiable comparison.
- **Scope**: several weeks; standalone methodology paper possible.

### 14. Cognitive science of religion application **[P3]**
Apply the Boyer / Atran / Whitehouse framework for how religious
movements form cognitively to the early Christian question.
- **Key literature**: Pascal Boyer, *Religion Explained*; Scott Atran,
  *In Gods We Trust*; Harvey Whitehouse, *Modes of Religiosity*.
- **Research question**: does a movement founded around a recently-
  executed historical figure follow a different cognitive-transmission
  profile than one founded around revelatory visions?
- **The fields (CSR and historical-Jesus studies) essentially don't
  talk to each other.**
- **Scope**: major, probably a standalone paper or dissertation chapter.

---

## Part III. Underutilized primary sources

### 15. Archaeological substrate analysis **[P2]**
Systematic treatment of:
- **Nazareth**: habitation in the first century.  René Salm (negative)
  vs. Ken Dark, Jonathan Reed, James Strange (positive).  What is the
  actual evidence?
- **Sepphoris**: Hellenistic urban center 4 miles from Nazareth; total
  absence from Gospel material despite prominence.
- **Capernaum**: the "house of Peter" tradition and its actual
  archaeological support.
- **Pilate's prefecture**: administrative traces; the 1961 Caesarea
  inscription.
- **Yehohanan ossuary**: the only physical evidence of Roman crucifixion
  in Judea; what does it imply?
- **Scope**: one new subsection in §6.

### 16. Qumran/Essene material cataloging **[P2]**
A systematic audit of what pre-Christian Jewish sectarian literature
(Dead Sea Scrolls, the Therapeutae as reported by Philo, Josephus's
Essenes) contains that is relevant to the Christology Paul develops.
- 4Q521 on messianic deliverance; 11QMelchizedek on heavenly mediator;
  the Self-Glorification Hymn at Qumran; the Teacher of Righteousness
  tradition.
- **Key scholars**: John Collins, *The Scepter and the Star*;
  Israel Knohl, *The Messiah Before Jesus*; Daniel Boyarin.
- **Scope**: 3,000-4,000 words; one subsection in §7.1.

### 17. Slavonic Josephus and Agapius textual witnesses **[P3]**
Alternative textual transmissions of Josephus that may preserve
earlier readings than the Greek: the Slavonic version of *The Jewish
War* (with its unique Jesus passages) and Agapius's Arabic summary
of the *Testimonium Flavianum*.
- Both are contested; both are plausibly independent witnesses to
  pre-Eusebian forms of the text.
- **Key scholars**: Étienne Nodet; Shlomo Pines (1971 edition of
  Agapius).
- **Scope**: 2,000-3,000 words in §6.1.

### 18. Gnostic Christology beyond Nag Hammadi **[P3]**
The *Pistis Sophia*, *Gospel of Mary*, *Gospel of Judas*, *Gospel of
Truth*, *Treatise on the Resurrection* — what Christological assumptions
do they make?  The canonical-Gospel-centric view of early Christianity
is a historiographical artifact; the actual diversity was wider.
- **Scope**: one subsection in §5.

### 19. Patristic citation-chain analysis of Paul **[P2]**
How is Paul cited in the second-century Church Fathers?  Earliest
citations can reveal textual layers and community reception.
- **Ignatius** (c. 110 CE) cites Paul; what does he cite?
- **Polycarp's** *Letter to the Philippians* cites Paul extensively.
- **1 Clement** (c. 95 CE) — extensive Pauline citation.
- **Marcion** (c. 140 CE) — systematic canonical use of Paul.
- What passages are cited, and which are conspicuously absent?
- **Scope**: 2-3 weeks; could strengthen §3.1 substantially.

---

## Part IV. Methodology improvements

### 20. Expand baseline sample to n=100 per bucket **[P2]**
Current n≈35 per bucket gives wide within-bucket CIs.  Expanding to
n=100 would tighten estimates substantially without requiring new
methodology.
- **Scope**: 1 week per bucket of careful random sampling and
  classification; 6 buckets = 6 weeks total.

### 21. Bootstrap CIs with within-author clustering **[P2]**
Current Wilson CIs assume independent sampling.  Tokens from the same
author (e.g., 35 Plutarch tokens from 143 works) are likely correlated.
Compute bootstrap CIs with explicit author-level clustering.
- **Tool**: Python `scipy.stats.bootstrap` with clustered resampling.
- **Purpose**: give statistically-honest uncertainty estimates.
- **Scope**: 1-2 days once infrastructure is set up.

### 22. Sensitivity analysis with alternative coding **[P2]**
Re-classify the baseline and Pauline samples under alternative coding
conventions (stricter A criteria; stricter D criteria; different D/E
boundary).  Report how the aggregate statistics shift.
- **Purpose**: address the "D/E boundary is fuzzy" critique
  quantitatively.
- **Scope**: 1 week.

### 23. Register-proportional aggregation of baseline **[P2]**
The current baseline uses equal weighting across six buckets.  An
alternative weighted by estimated volume of Greek Paul would have
encountered (heavy on papyri and synagogue, lighter on Plutarch) would
give a more ecologically-valid aggregate.
- **Purpose**: reviewer will ask; pre-empt the objection.
- **Scope**: 2-3 days; one new paragraph in baseline supplement.

---

## Part V. Quality assurance and publication

### 24. External expert review — sympathetic **[QA]**
Approach at least one mythicist-sympathetic scholar (Carrier, Lataster,
Price, or Brodie if still reachable) for pre-submission review.
- **Purpose**: sharpen the argument and catch internal weaknesses.
- **Risk**: Carrier in particular has idiosyncratic approach; manage
  expectations.

### 25. External expert review — skeptical **[QA]**
Approach at least one historicist scholar for pre-submission review.
- **First choice**: Dale Allison (methodologically sophisticated, takes
  skepticism seriously).
- **Second choice**: Paula Fredriksen (would challenge the §7 framing
  directly in productive ways).
- **Third choice**: Philip Harland (directly relevant expertise on
  §3.5's associative-brotherhood argument).
- **Purpose**: preempt the strongest legitimate critiques.

### 26. Preprint deposit **[QA]**
Deposit the paper and supplements on preprint servers before journal
submission:
- **Humanities**: SSRN, Humanities Commons, PhilArchive.
- **Biblical studies**: Biblica, Academia.edu (limited utility but
  discoverable).
- **Purpose**: establish priority; generate informal review.

### 27. Identify submission venues **[QA]**
Candidate journals for the main paper or a journal-length version:
- *Journal for the Study of the Historical Jesus* (heterodox tolerant)
- *Journal of Higher Criticism* (explicitly revisionist)
- *History of Religions* (Chicago; comparative, methodologically broad)
- *The Journal of Religion* (interdisciplinary)
- *Religion* (Taylor & Francis; critical)
- *Method & Theory in the Study of Religion*
- *Nova Religio*
- **Humanities Commons** as an open deposit.

### 28. Pre-empt probable reviewer critiques **[QA]**
Prepare response documents (or revisions) to the strongest anticipated
reviewer objections:
- Fredriksen-style: Paul's Jewishness precludes mythicism.
- Ehrman-style: cumulative case; Peter-James-Paul nexus.
- Novenson-style: Davidic messianism is genuinely hard.
- Allison-style: memory-theory explains the gestalt.
- Harland-style: inscriptions are the missing register (now addressed).

### 29. README and documentation update **[QA]**
Update `README.md` to reflect the current 3-document structure (main
paper + 2 supplements) and the data/scripts directory layout.  Add
build instructions for the baseline supplement.  Add a citation
recommendation.

### 30. DOI and persistent identifier **[QA]**
Obtain a DOI for the preprint/repository (via Zenodo-GitHub
integration or similar) for stable citation.

---

## Part VI. Infrastructure / tooling

### 31. Classical Language Toolkit integration
Set up a working CLTK environment for Greek NLP analysis; this is
foundational for items 10, 11, 13, 18.

### 32. Greek inscription scraper
For item 1: a script that pulls from PHI Greek Inscriptions or
epigraphy.packhum.org and formats results for classification.

### 33. Automated reference-checking
A script that extracts all `\cite*` commands from the LaTeX sources,
looks up each in the bib file, flags missing entries and year
mismatches.

### 34. Continuous-integration build
GitHub Actions workflow that compiles the main paper and both
supplements on every commit, so build breakage is caught immediately.

---

## Priorities for the next revision pass

If capacity is limited, the ranked order for maximum impact on the
paper's defensibility is:

1. **Item 1** (epigraphic *adelphoi*) — closes the quantitative baseline gap
2. **Item 2** (comparative case studies) — establishes method generalizability
3. **Item 3** (Jewish mystical-ascent) — grounds §7.1 procedurally
4. **Item 5** (inter-rater agreement) — answers one class of reviewer objection
5. **Item 4** (text-critical cluster) — answers another class of reviewer objection
6. **Item 19** (patristic citation chains) — strengthens §3.1 substantially
7. **Item 8** (Mandaean) — adds a genuinely novel independent witness
8. **Item 7** (journal-length version) — required for any submission

Items 9-18 are the broader research programme; each could be a
standalone paper.  Items 20-34 are methodological/infrastructural.
