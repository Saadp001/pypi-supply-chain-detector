from popular_packages import POPULAR_PACKAGES
from similarity_analysis import is_typosquat
from risk_scoring import compute_risk
from data_collector import get_package_info
import json

# Example suspicious candidates (simulated)
candidates = [
    "requesrs",
    "reqeusts",
    "flsak",
    "djagno"
]

results = []

for popular in POPULAR_PACKAGES:
    for candidate in candidates:
        is_suspicious, score = is_typosquat(candidate, popular)
        if is_suspicious:
            info = get_package_info(candidate)
            if info:
                risk = compute_risk(score, info["upload_time"])
                results.append({
                    "package": candidate,
                    "similar_to": popular,
                    "similarity": score,
                    "risk_score": risk
                })

with open("flagged_packages.json", "w") as f:
    json.dump(results, f, indent=2)

print("Analysis complete. Check flagged_packages.json")
