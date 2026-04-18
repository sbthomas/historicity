#!/usr/bin/env python3
"""Rolling stylometric analysis of the undisputed Pauline corpus.

Computes function-word frequency profiles in sliding windows across
Paul's letters and identifies statistical outliers. Validates against
known interpolations (1 Thess 2:14-16, 1 Cor 14:34-35) and tests
the status of the contested historicity-relevant clauses
(Gal 1:19, Rom 1:3-4, 1 Cor 15:3-8, Gal 4:4).

Output: stylometry_report.md with per-passage outlier scores and
verse-level analysis.
"""

import re
import math
from pathlib import Path
from collections import Counter

SCRIPT_DIR = Path(__file__).resolve().parent
SBL_DIR = SCRIPT_DIR / 'sblgnt'
OUTPUT = SCRIPT_DIR.parent / 'baseline' / 'stylometry_report.md'

BOOKS = ['Rom', '1Cor', '2Cor', 'Gal', 'Phil', '1Thess', 'Phlm']

# SBLGNT editorial sigla to strip
SIGLA = re.compile(r'[⸀⸁⸂⸃⸄⸅⸆⸇⸈⸉⸊⸋⸌⸍⸎⸏]')
PUNCT = re.compile(r'[.,;:·]')

# Koine Greek function words chosen for stylometric discrimination.
# These are the most frequent non-semantic words that vary by author style.
FUNCTION_WORDS = [
    'καί', 'δέ', 'γάρ', 'οὖν', 'μέν', 'τε', 'ἀλλά', 'εἰ', 'ἐάν',
    'ὅτι', 'ἵνα', 'ὥστε', 'ὡς', 'ὅπως', 'πρός', 'εἰς', 'ἐν',
    'ἐπί', 'διά', 'ὑπό', 'περί', 'κατά', 'μετά', 'ἀπό', 'ἐκ',
    'παρά', 'σύν', 'ὑπέρ', 'ἄν', 'οὐ', 'οὐκ', 'οὐχ', 'μή',
    'οὐδέ', 'μηδέ', 'οὐδείς', 'πᾶς', 'πάς', 'πάντα', 'πάντες',
    'ὁ', 'τοῦ', 'τῷ', 'τόν', 'τήν', 'τῆς', 'τῇ', 'τήν',
    'οἱ', 'τούς', 'τῶν', 'τοῖς', 'τάς', 'ταῖς',
    'αὐτός', 'αὐτοῦ', 'αὐτῷ', 'αὐτόν', 'αὐτή', 'αὐτήν', 'αὐτῆς',
    'αὐτοί', 'αὐτῶν', 'αὐτοῖς', 'αὐτούς',
    'ἐγώ', 'ἐμοί', 'ἐμέ', 'μου', 'μοι', 'με',
    'σύ', 'σοί', 'σέ', 'σου', 'σοι', 'ὑμεῖς', 'ὑμῶν',
    'ἡμεῖς', 'ἡμῶν', 'ἡμῖν', 'ἡμᾶς',
    'εἰμί', 'ἐστίν', 'ἐστί', 'εἰσίν', 'ἦν', 'ἦσαν',
    'λέγω', 'λέγει', 'εἶπεν', 'εἶπον',
    'ἔχω', 'ἔχει', 'ἔχομεν',
]

# Strip accents for robust matching
def strip_accents(s):
    import unicodedata
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

FUNCTION_WORDS_NORM = set(strip_accents(w).lower() for w in FUNCTION_WORDS)


def load_book(book):
    """Return list of (ref, tokens) tuples for the book."""
    txt = (SBL_DIR / f'{book}.txt').read_text(encoding='utf-8')
    verses = []
    for line in txt.splitlines():
        line = line.strip()
        if not line or '\t' not in line:
            continue
        ref, greek = line.split('\t', 1)
        greek = SIGLA.sub('', greek)
        greek = PUNCT.sub(' ', greek)
        tokens = greek.split()
        if tokens:
            verses.append((ref, tokens))
    return verses


def compute_feature_vector(tokens):
    """Compute normalized function-word frequency vector for a token list."""
    if not tokens:
        return None
    total = len(tokens)
    counts = Counter()
    for t in tokens:
        t_norm = strip_accents(t).lower()
        if t_norm in FUNCTION_WORDS_NORM:
            counts[t_norm] += 1
    # Return relative frequencies
    return {w: counts.get(w, 0) / total for w in FUNCTION_WORDS_NORM}


def cosine_similarity(v1, v2):
    """Cosine similarity between two feature-vectors (as dicts)."""
    keys = set(v1.keys()) | set(v2.keys())
    dot = sum(v1.get(k, 0) * v2.get(k, 0) for k in keys)
    n1 = math.sqrt(sum(v1.get(k, 0) ** 2 for k in keys))
    n2 = math.sqrt(sum(v2.get(k, 0) ** 2 for k in keys))
    if n1 == 0 or n2 == 0:
        return 0.0
    return dot / (n1 * n2)


def euclidean_distance(v1, v2):
    keys = set(v1.keys()) | set(v2.keys())
    return math.sqrt(sum((v1.get(k, 0) - v2.get(k, 0)) ** 2 for k in keys))


def rolling_windows(all_verses, window_size=100):
    """Yield (start_ref, end_ref, token_window) for a sliding token window."""
    # Flatten to (ref, token) list
    flat = []
    for ref, tokens in all_verses:
        for t in tokens:
            flat.append((ref, t))
    # Slide
    for i in range(0, len(flat) - window_size + 1, 20):  # step 20 for overlap
        window = flat[i:i+window_size]
        start_ref = window[0][0]
        end_ref = window[-1][0]
        tokens_only = [t for _, t in window]
        yield start_ref, end_ref, tokens_only


def analyze_paul():
    """Main analysis: compute Pauline baseline, find outlier windows."""
    # Load all 7 letters
    all_verses = {}
    for book in BOOKS:
        all_verses[book] = load_book(book)

    # Compute overall Pauline profile
    all_tokens = []
    for book in BOOKS:
        for ref, toks in all_verses[book]:
            all_tokens.extend(toks)
    paul_profile = compute_feature_vector(all_tokens)

    # Also compute per-letter profiles (for comparison)
    per_letter_profiles = {}
    for book in BOOKS:
        tokens = []
        for ref, toks in all_verses[book]:
            tokens.extend(toks)
        per_letter_profiles[book] = compute_feature_vector(tokens)

    # Rolling-window outlier detection
    window_results = []
    for book in BOOKS:
        for start, end, window_tokens in rolling_windows(all_verses[book], window_size=80):
            vec = compute_feature_vector(window_tokens)
            sim = cosine_similarity(vec, paul_profile)
            dist = euclidean_distance(vec, paul_profile)
            window_results.append((book, start, end, sim, dist))

    # Rank windows by distance
    window_results.sort(key=lambda x: x[4], reverse=True)
    return paul_profile, per_letter_profiles, window_results


def analyze_specific_passages(all_verses, paul_profile):
    """Analyze specific contested and control passages."""
    passages = {
        # Known interpolations (control — should show as outliers)
        '1 Thess 2:14-16 (suspected interpolation)':
            [('1Thess', '2:14'), ('1Thess', '2:15'), ('1Thess', '2:16')],
        '1 Cor 14:34-35 (suspected interpolation)':
            [('1Cor', '14:34'), ('1Cor', '14:35')],
        # Pre-Pauline creedal fragments (should also differ stylistically)
        'Phil 2:5-11 (pre-Pauline Christ hymn)':
            [('Phil', '2:5'), ('Phil', '2:6'), ('Phil', '2:7'),
             ('Phil', '2:8'), ('Phil', '2:9'), ('Phil', '2:10'), ('Phil', '2:11')],
        'Rom 1:3-4 (pre-Pauline creedal fragment)':
            [('Rom', '1:3'), ('Rom', '1:4')],
        '1 Cor 15:3-5 (pre-Pauline creed, narrow)':
            [('1Cor', '15:3'), ('1Cor', '15:4'), ('1Cor', '15:5')],
        '1 Cor 15:3-8 (pre-Pauline creed + witness list)':
            [('1Cor', f'15:{i}') for i in range(3, 9)],
        # Historicity-relevant contested passages
        'Gal 1:19 (brother of the Lord)':
            [('Gal', '1:19')],
        'Gal 1:18-20 (Gal 1:19 in context)':
            [('Gal', '1:18'), ('Gal', '1:19'), ('Gal', '1:20')],
        '1 Cor 9:5 (brothers of the Lord)':
            [('1Cor', '9:5')],
        '1 Cor 9:4-6 (1 Cor 9:5 in context)':
            [('1Cor', '9:4'), ('1Cor', '9:5'), ('1Cor', '9:6')],
        'Gal 4:4 (born of a woman)':
            [('Gal', '4:4')],
        'Gal 4:3-5 (Gal 4:4 in context)':
            [('Gal', '4:3'), ('Gal', '4:4'), ('Gal', '4:5')],
    }

    results = []
    for name, verses in passages.items():
        tokens = []
        for book, vs in verses:
            for ref, toks in all_verses[book]:
                _, refvs = ref.rsplit(' ', 1)
                if refvs == vs:
                    tokens.extend(toks)
        if tokens:
            vec = compute_feature_vector(tokens)
            sim = cosine_similarity(vec, paul_profile)
            dist = euclidean_distance(vec, paul_profile)
            results.append((name, len(tokens), sim, dist))
    return results


def main():
    print("Running stylometric analysis of undisputed Paul...")
    paul_profile, per_letter_profiles, windows = analyze_paul()

    # Load all verses for passage analysis
    all_verses = {book: load_book(book) for book in BOOKS}

    passage_results = analyze_specific_passages(all_verses, paul_profile)

    # Write report
    lines = []
    lines.append("# Stylometric Analysis of Undisputed Paul")
    lines.append("")
    lines.append("## Method")
    lines.append("")
    lines.append("Function-word frequency vector comparison using cosine similarity")
    lines.append("and Euclidean distance against the overall Pauline profile.")
    lines.append("Function-word set of ~80 high-frequency Koine Greek words")
    lines.append("(conjunctions, particles, articles, pronouns, prepositions, common verbs)")
    lines.append("chosen for stylometric rather than thematic discrimination.")
    lines.append("")
    lines.append("Higher distance / lower similarity = more stylometrically distinctive")
    lines.append("from the overall Pauline baseline.")
    lines.append("")
    lines.append("## Per-letter distance from global Pauline profile")
    lines.append("")
    lines.append("| Letter | Cosine similarity | Euclidean distance |")
    lines.append("|---|---|---|")
    for book in BOOKS:
        sim = cosine_similarity(per_letter_profiles[book], paul_profile)
        dist = euclidean_distance(per_letter_profiles[book], paul_profile)
        lines.append(f"| {book} | {sim:.4f} | {dist:.4f} |")
    lines.append("")
    lines.append("Interpretation: all 7 letters should cluster tightly with the profile.")
    lines.append("Distances here establish the baseline intra-Pauline variation.")
    lines.append("")
    lines.append("## Specific passage analysis")
    lines.append("")
    lines.append("Compares small passage-level feature vectors (less reliable for")
    lines.append("short passages; included for illustration).")
    lines.append("")
    lines.append("| Passage | Tokens | Cosine sim | Euclidean dist |")
    lines.append("|---|---|---|---|")
    for name, ntoks, sim, dist in passage_results:
        lines.append(f"| {name} | {ntoks} | {sim:.4f} | {dist:.4f} |")
    lines.append("")
    lines.append("## Top 20 outlier windows (80-token sliding window)")
    lines.append("")
    lines.append("| Rank | Book | From | To | Cosine sim | Euclidean dist |")
    lines.append("|---|---|---|---|---|---|")
    for i, (book, start, end, sim, dist) in enumerate(windows[:20], 1):
        lines.append(f"| {i} | {book} | {start} | {end} | {sim:.4f} | {dist:.4f} |")
    lines.append("")
    lines.append("## Caveats")
    lines.append("")
    lines.append("- Short passages (1-3 verses, <50 tokens) produce noisy vectors;")
    lines.append("  feature-vector similarity at that scale is unreliable.")
    lines.append("- Function-word frequency alone misses higher-order syntactic")
    lines.append("  features that would be captured by dependency parsing or")
    lines.append("  character-n-gram analysis (future work).")
    lines.append("- A single-coder function-word list is a methodological choice;")
    lines.append("  replication with a different function-word inventory would")
    lines.append("  improve robustness.")
    lines.append("- The analysis is best read as exploratory: it identifies")
    lines.append("  *candidate* outliers rather than proving interpolation.")

    OUTPUT.write_text('\n'.join(lines), encoding='utf-8')
    print(f"Wrote {OUTPUT}")

    # Also print summary to stderr
    import sys
    print("\nPer-letter distances from Pauline baseline:", file=sys.stderr)
    for book in BOOKS:
        d = euclidean_distance(per_letter_profiles[book], paul_profile)
        print(f"  {book}: {d:.4f}", file=sys.stderr)

    print("\nSpecific passages:", file=sys.stderr)
    for name, ntoks, sim, dist in passage_results:
        print(f"  [{ntoks:3d} tok] dist={dist:.4f} sim={sim:.4f}  {name}", file=sys.stderr)

    print(f"\nTop 10 outlier 80-token windows:", file=sys.stderr)
    for i, (book, start, end, sim, dist) in enumerate(windows[:10], 1):
        print(f"  {i}. {book} {start.split(' ',1)[1]} -> {end.split(' ',1)[1]}  dist={dist:.4f}", file=sys.stderr)


if __name__ == '__main__':
    main()
