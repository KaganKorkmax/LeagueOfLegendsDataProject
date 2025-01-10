import pandas as pd
import matplotlib.pyplot as plt

file_path = "match_data_20250110_154758.txt"

tier_mapping = {
    "Bronze": 0,
    "Silver": 4,
    "Gold": 8,
    "Platinum": 12,
    "Diamond": 16,
    "Master": 20,
    "Grandmaster": 24,
    "Challenger": 28
}

tier_labels = [
    "Bronze 4", "Bronze 3", "Bronze 2", "Bronze 1",
    "Silver 4", "Silver 3", "Silver 2", "Silver 1",
    "Gold 4", "Gold 3", "Gold 2", "Gold 1",
    "Platinum 4", "Platinum 3", "Platinum 2", "Platinum 1",
    "Diamond 4", "Diamond 3", "Diamond 2", "Diamond 1",
    "Master", "Grandmaster", "Challenger"
]

seasons = {
    "Season 1": [],
    "Season 2": [],
    "Season 3": []
}

with open(file_path, "r", encoding="utf-8") as f:
    next(f)
    for line in f:
        parts = line.strip().split(",")
        if len(parts) < 6 or "N/A" in line:
            continue

        try:
            date_info = parts[0].strip()
            lig_info = parts[-1].strip()

            if "2 ay önce" in date_info:
                season_key = "Season 1"
            elif "bir ay önce" in date_info:
                season_key = "Season 2"
            elif "gün önce" in date_info:
                season_key = "Season 3"
            else:
                continue

            if " " in lig_info:
                tier, division = lig_info.split(" ")
                division = int(division) if division.isdigit() else 0
                numeric_level = tier_mapping[tier] + (5 - division)
                seasons[season_key].append(numeric_level)
        except Exception as e:
            print(f"[ERROR] Line could not be processed: {line.strip()} - Error: {e}")

avg_tiers = {}
for season, levels in seasons.items():
    if levels:
        avg_tier = sum(levels) / len(levels)
        avg_tiers[season] = avg_tier
    else:
        avg_tiers[season] = 0

avg_tier_labels = {
    season: tier_labels[round(avg)]
    for season, avg in avg_tiers.items()
}

plt.figure(figsize=(10, 6))
x_labels = list(avg_tiers.keys())
y_values = list(avg_tiers.values())

plt.bar(x_labels, y_values, color="skyblue", alpha=0.8)

for i, avg_tier in enumerate(y_values):
    if avg_tier > 0:
        plt.text(i, avg_tier + 0.2, avg_tier_labels[x_labels[i]], ha="center", fontsize=12)

plt.title("Average League Level Per Season", fontsize=14)
plt.xlabel("Seasons", fontsize=12)
plt.ylabel("Average League Level", fontsize=12)
plt.yticks(range(len(tier_labels)), tier_labels)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

print("Average League Levels Per Season:")
for season, avg_tier in avg_tiers.items():
    label = avg_tier_labels[season]
    if avg_tier > 0:
        print(f"{season}: Average League Level = {label}")
