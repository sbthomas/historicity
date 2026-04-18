# Stylometric Analysis of Undisputed Paul

## Method

Function-word frequency vector comparison using cosine similarity
and Euclidean distance against the overall Pauline profile.
Function-word set of ~80 high-frequency Koine Greek words
(conjunctions, particles, articles, pronouns, prepositions, common verbs)
chosen for stylometric rather than thematic discrimination.

Higher distance / lower similarity = more stylometrically distinctive
from the overall Pauline baseline.

## Per-letter distance from global Pauline profile

| Letter | Cosine similarity | Euclidean distance |
|---|---|---|
| Rom | 0.9810 | 0.0149 |
| 1Cor | 0.9731 | 0.0178 |
| 2Cor | 0.9770 | 0.0174 |
| Gal | 0.9614 | 0.0213 |
| Phil | 0.9174 | 0.0375 |
| 1Thess | 0.9176 | 0.0395 |
| Phlm | 0.8207 | 0.0511 |

Interpretation: all 7 letters should cluster tightly with the profile.
Distances here establish the baseline intra-Pauline variation.

## Specific passage analysis

Compares small passage-level feature vectors (less reliable for
short passages; included for illustration).

| Passage | Tokens | Cosine sim | Euclidean dist |
|---|---|---|---|
| 1 Thess 2:14-16 (suspected interpolation) | 75 | 0.6855 | 0.1026 |
| 1 Cor 14:34-35 (suspected interpolation) | 36 | 0.6544 | 0.1013 |
| Phil 2:5-11 (pre-Pauline Christ hymn) | 85 | 0.7846 | 0.0696 |
| Rom 1:3-4 (pre-Pauline creedal fragment) | 28 | 0.3395 | 0.1687 |
| 1 Cor 15:3-5 (pre-Pauline creed, narrow) | 38 | 0.5915 | 0.1555 |
| 1 Cor 15:3-8 (pre-Pauline creed + witness list) | 69 | 0.6524 | 0.0851 |
| Gal 1:19 (brother of the Lord) | 13 | 0.4020 | 0.1864 |
| Gal 1:18-20 (Gal 1:19 in context) | 39 | 0.6026 | 0.0918 |
| 1 Cor 9:5 (brothers of the Lord) | 19 | 0.5637 | 0.1909 |
| 1 Cor 9:4-6 (1 Cor 9:5 in context) | 36 | 0.5337 | 0.1843 |
| Gal 4:4 (born of a woman) | 19 | 0.3783 | 0.1311 |
| Gal 4:3-5 (Gal 4:4 in context) | 41 | 0.4428 | 0.1135 |

## Top 20 outlier windows (80-token sliding window)

| Rank | Book | From | To | Cosine sim | Euclidean dist |
|---|---|---|---|---|---|
| 1 | 2Cor | 2Cor 6:2 | 2Cor 6:7 | 0.4332 | 0.2421 |
| 2 | 2Cor | 2Cor 6:3 | 2Cor 6:9 | 0.5134 | 0.2327 |
| 3 | 2Cor | 2Cor 6:4 | 2Cor 6:10 | 0.5948 | 0.2105 |
| 4 | 2Cor | 2Cor 5:21 | 2Cor 6:6 | 0.5357 | 0.1676 |
| 5 | 1Cor | 1Cor 12:28 | 1Cor 13:2 | 0.4417 | 0.1509 |
| 6 | Rom | Rom 12:6 | Rom 12:13 | 0.4442 | 0.1422 |
| 7 | Phil | Phil 4:8 | Phil 4:13 | 0.7649 | 0.1381 |
| 8 | 1Cor | 1Cor 7:27 | 1Cor 7:31 | 0.5816 | 0.1376 |
| 9 | 1Cor | 1Cor 13:12 | 1Cor 14:5 | 0.5375 | 0.1366 |
| 10 | Rom | Rom 3:9 | Rom 3:18 | 0.4391 | 0.1365 |
| 11 | 2Cor | 2Cor 11:21 | 2Cor 11:27 | 0.4248 | 0.1364 |
| 12 | 1Cor | 1Cor 12:27 | 1Cor 13:1 | 0.3964 | 0.1360 |
| 13 | 2Cor | 2Cor 11:23 | 2Cor 11:28 | 0.5206 | 0.1347 |
| 14 | 2Cor | 2Cor 6:7 | 2Cor 6:13 | 0.6466 | 0.1344 |
| 15 | Rom | Rom 16:7 | Rom 16:13 | 0.5283 | 0.1336 |
| 16 | 1Cor | 1Cor 9:20 | 1Cor 9:24 | 0.3057 | 0.1334 |
| 17 | 1Cor | 1Cor 9:18 | 1Cor 9:23 | 0.3335 | 0.1327 |
| 18 | 2Cor | 2Cor 6:6 | 2Cor 6:11 | 0.6714 | 0.1323 |
| 19 | Rom | Rom 12:5 | Rom 12:11 | 0.5471 | 0.1297 |
| 20 | Rom | Rom 13:12 | Rom 14:4 | 0.6090 | 0.1283 |

## Caveats

- Short passages (1-3 verses, <50 tokens) produce noisy vectors;
  feature-vector similarity at that scale is unreliable.
- Function-word frequency alone misses higher-order syntactic
  features that would be captured by dependency parsing or
  character-n-gram analysis (future work).
- A single-coder function-word list is a methodological choice;
  replication with a different function-word inventory would
  improve robustness.
- The analysis is best read as exploratory: it identifies
  *candidate* outliers rather than proving interpolation.