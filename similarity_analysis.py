import Levenshtein

def similarity_score(pkg1, pkg2):
    return Levenshtein.ratio(pkg1.lower(), pkg2.lower())

def is_typosquat(pkg, popular_pkg, threshold=0.8):
    score = similarity_score(pkg, popular_pkg)
    return score >= threshold, score
