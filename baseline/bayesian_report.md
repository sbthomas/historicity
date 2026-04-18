# Bayesian Sensitivity Analysis: Historicity of Jesus

## Method

A simplified Bayesian sensitivity analysis over the principal
evidentiary strands discussed in the main paper. Each evidence
piece is assigned a likelihood ratio P(E|H) / P(E|M) expressed
in decibels (10·log₁₀). Positive = favours historicity (H);
negative = favours mythic-origin (M).

The point estimates below are plausible but **contestable**;
the exercise is to see how the posterior depends on them.
Run `scripts/bayesian_sensitivity.py` with modified values
to explore alternatives.

**Two computations are reported:**

1. **Independence-assumed (Carrier-style).** Multiplies
   likelihood ratios assuming evidence pieces are
   independent. Over-counts when sources share dependence
   (e.g., Tacitus → Christian sources → Paul).

2. **Dependency-aware.** Discounts each piece's contribution
   by 0.5^(number of dependencies) for evidence pieces that
   textually derive from other pieces. This is a heuristic
   approximation of proper Bayesian-network conditioning.

## Evidence table (point estimates)

| Evidence | LR (dB) | Depends on | Favours |
|---|---|---|---|
| Paul's adelphos distribution (0 biological out of 121) | -8.0 | — | M |
| Gal 1:19 "brother of the Lord" considered in isolation | +6.0 | paul_adelphos_distribution | H |
| Rom 1:3 "descended from David kata sarka" | +5.0 | — | H |
| Gal 4:4 "born of a woman, born under the law" | +3.0 | — | H |
| 1 Cor 15:3-5 pre-Pauline creed (narrow) | +2.0 | — | H |
| 1 Cor 15:6-8 witness list (500 brothers, James, apostles) | +4.0 | 1cor_15_creed | H |
| Paul's silence on biographical Jesus details | -5.0 | — | M |
| Paul's revelation-mechanism claim (Gal 1:12-17) | -4.0 | paul_silence_biographical | M |
| Gospel narratives constructed from HB templates | -4.0 | — | M |
| Synoptic dependence (Mark -> Matthew, Luke) | +0.0 | — | neutral |
| Speed of Pauline-to-Markan biographical development | +3.0 | — | H |
| Josephus AJ 20.200 "brother of Jesus called Christ" | +4.0 | — | H |
| Josephus AJ 18.63-64 Testimonium Flavianum | +1.0 | josephus_james | H |
| Tacitus Annals 15.44 on Chrestus/Christus | +1.0 | — | H |
| Pliny, Suetonius, and minor references | +0.5 | tacitus | H |
| Rabbinic Yeshu passages and Toledoth Yeshu | +0.5 | tacitus | H |
| Silence of Philo of Alexandria | -2.5 | — | M |
| Silence of Justus of Tiberias | -3.0 | — | M |
| Silence of the Mishnaic legal tradition | -1.0 | — | M |
| Silence of Roman administrative records | -1.5 | justus_silence | M |
| Pre-Christian Jewish sources for Pauline Christology | -3.0 | — | M |
| Comparative existence-question cases (Pythagoras, Moses, Romulus) | +0.0 | — | neutral |

## Posteriors under different priors

| Prior P(H) | Indep. posterior | Dep-aware posterior |
|---|---|---|
| 0.10 | 0.0655 | 0.0321 |
| 0.25 | 0.1738 | 0.0905 |
| 0.50 | 0.3869 | 0.2299 |
| 0.75 | 0.6543 | 0.4725 |
| 0.90 | 0.8503 | 0.7288 |

## Interpretation

Under the independence assumption, the evidence pieces cancel
substantially. The strongest favouring-H pieces (Josephus James,
1 Cor 15 witnesses, Gal 1:19 surface reading, Rom 1:3) are
balanced by the strongest favouring-M pieces (Paul's adelphos
distribution, Paul's biographical silence, Gospel scriptural
construction, Paul's apokalypsis mechanism, Jewish matrix).

The dependency-aware computation compresses the posteriors
toward the prior, because evidence pieces that textually
depend on others contribute less. This correctly deflates
cumulative-case arguments where sources are not independent.

## Key sensitivities

The posterior depends most on:

1. **Paul's adelphos distribution** (-8 dB favouring M). The
   Harland-corrected baseline analysis. If the true baseline
   A-rate is 15% rather than 1%, this reduces toward -3 dB.

2. **Josephus's James passage** (+4 dB favouring H). Authenticity
   is widely accepted but contested by Carrier. If interpolation
   is accepted, this moves toward 0 dB.

3. **1 Cor 15 witness list** (+4 dB favouring H). Specificity
   of the 500-brothers-and-James list. If the list is taken to
   be substantially pre-Pauline formula the weight is unchanged;
   if taken as Pauline expansion, the specificity carries more
   weight.

4. **Paul's biographical silence** (-5 dB favouring M). If the
   silence is attributable to epistolary genre conventions
   rather than to absence of memory, this reduces toward -2 dB.

## What this analysis does NOT do

- It does not compute a definitive posterior probability.
- It does not claim the point estimates are correct.
- It does not implement a full Bayesian network with explicit
  conditional distributions (future work).
- It does not include every evidence piece in the literature.

## What this analysis DOES

- Makes Carrier's informal Bayesian reasoning explicit and
  auditable.
- Shows how source-dependence (Tacitus → Christian informants,
  Gospels → Mark) should deflate naive cumulative-case claims.
- Provides a framework that readers can edit and re-run with
  their own point estimates.