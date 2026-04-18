#!/usr/bin/env python3
"""Compute per-bucket A/B/C/D/E proportions with Wilson 95% CIs.

Accepts hand-classified TSVs in baseline/data/ and summary counts for
buckets where agent classifications are used with acknowledged caveats.
"""

from math import sqrt
from pathlib import Path


def wilson_ci(k, n, z=1.96):
    """Wilson score interval for binomial proportion."""
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    denom = 1 + z*z / n
    center = (p + z*z / (2*n)) / denom
    halfwidth = z * sqrt(p*(1-p)/n + z*z/(4*n*n)) / denom
    return (max(0, center - halfwidth), min(1, center + halfwidth))


# Bucket counts: (A, B, C, D, E) — total = sum
#
# The three literary buckets were expanded from n=35/36 to n=100 in an
# n=100 expansion pass (classifications in baseline/data/*_n100.tsv).
# Papyri, LXX, Josephus remain at n=35 pending agent re-sampling.
BUCKETS = {
    # Baseline (contemporary-or-earlier, non-Christian)
    'Papyri (pre-70 CE)':        (0, 35, 0, 0, 0),     # n=35; Ptolemaic sister-wives = biological
    'LXX':                       (0, 24, 2, 9, 0),     # n=35; agent-classified
    'Josephus':                  (0, 21, 2, 12, 0),    # n=35; agent-classified
    'Philo (n=100)':             (1, 63, 11, 5, 20),   # n=100; coder-classified (expansion pass)
    'Hellenistic literary (n=100)': (0, 94, 1, 0, 5),  # n=100; Plutarch+Epictetus+Dio
    'Pre-Pauline literary (n=100)': (2, 96, 0, 1, 1),  # n=100; Polybius+Strabo+Diodorus

    # Downstream (post-Pauline Christian — for contextual comparison, NOT prior)
    '[CONTEXT] NT non-Pauline letters': (33, 1, 1, 0, 0),  # agent-classified
    '[CONTEXT] Gospels + Acts':         (14, 18, 1, 2, 0),  # agent-classified

    # Reference point
    '[REFERENCE] Pauline (undisputed)': (117, 0, 3, 1, 0),  # harmonised A/B/C/D/E (Rom 9:3 → D)
}


def fmt_pct(p):
    return f'{100*p:5.1f}%'


def fmt_ci(lo, hi):
    return f'[{100*lo:4.1f}, {100*hi:4.1f}]'


print('| Bucket | N | A % (95% CI) | B % (95% CI) | C % | D % | E % |')
print('|---|---|---|---|---|---|---|')

# Aggregate the 6 baseline buckets
agg_A = agg_B = agg_C = agg_D = agg_E = agg_N = 0

for name, (a, b, c, d, e) in BUCKETS.items():
    n = a + b + c + d + e
    a_pct = a/n if n else 0
    b_pct = b/n if n else 0
    a_lo, a_hi = wilson_ci(a, n)
    b_lo, b_hi = wilson_ci(b, n)
    c_pct = c/n if n else 0
    d_pct = d/n if n else 0
    e_pct = e/n if n else 0
    print(f'| {name} | {n} | {fmt_pct(a_pct)} {fmt_ci(a_lo,a_hi)} | {fmt_pct(b_pct)} {fmt_ci(b_lo,b_hi)} | {fmt_pct(c_pct)} | {fmt_pct(d_pct)} | {fmt_pct(e_pct)} |')
    if not name.startswith('['):
        agg_A += a; agg_B += b; agg_C += c; agg_D += d; agg_E += e; agg_N += n

print()
print(f'Aggregate baseline (6 non-Christian contemporary-or-earlier buckets): N={agg_N}')
a_lo, a_hi = wilson_ci(agg_A, agg_N)
b_lo, b_hi = wilson_ci(agg_B, agg_N)
print(f'  A (community) = {agg_A}/{agg_N} = {fmt_pct(agg_A/agg_N)} {fmt_ci(a_lo,a_hi)}')
print(f'  B (biological) = {agg_B}/{agg_N} = {fmt_pct(agg_B/agg_N)} {fmt_ci(b_lo,b_hi)}')
print(f'  C (disputed) = {agg_C}/{agg_N} = {fmt_pct(agg_C/agg_N)}')
print(f'  D (ethnic/covenantal) = {agg_D}/{agg_N} = {fmt_pct(agg_D/agg_N)}')
print(f'  E (metaphorical) = {agg_E}/{agg_N} = {fmt_pct(agg_E/agg_N)}')

print()
print('Pauline comparison:')
paul_A, paul_B = 117, 0
paul_total = 121  # 117A + 4C (Rom 9:3, Rom 16:15, 1 Cor 9:5 kyriou, Gal 1:19)
a_lo, a_hi = wilson_ci(paul_A, paul_total)
print(f'  A = {paul_A}/{paul_total} = {fmt_pct(paul_A/paul_total)} {fmt_ci(a_lo,a_hi)}')
print(f'  B = {paul_B}/{paul_total} = {fmt_pct(paul_B/paul_total)}')

print()
# Ratio of A in Paul vs. in baseline — likelihood ratio flavour
baseline_a = agg_A / agg_N if agg_N else 0
paul_a = paul_A / paul_total
print(f'A-rate ratio (Paul / baseline): {paul_a/baseline_a if baseline_a else float("inf"):.1f}x' if baseline_a > 0 else f'A-rate ratio undefined (baseline A = 0); Paul A-rate: {paul_a:.2%}')
