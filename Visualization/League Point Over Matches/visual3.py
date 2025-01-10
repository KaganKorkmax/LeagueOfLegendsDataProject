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
    "Gold 4", "Gold 3", "Gold 2", "Gold 1"
]

data = []
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) < 6:
            continue
        try:
            lig = parts[-1].strip()
            if " " in lig:
                tier, division = lig.split(" ")
                division = int(division) if division.isdigit() else 0
                numeric_level = tier_mapping[tier] + (5 - division)
                data.append(numeric_level)
            else:
                data.append(None)
        except Exception as e:
            print(f"[ERROR] Line could not be processed: {line} - Error: {e}")

match_numbers = list(range(1, len(data) + 1))

plt.figure(figsize=(12, 6))
plt.plot(match_numbers, data, marker="o", linestyle="-", color="b", alpha=0.7)
plt.title("League Point Over Matches (From Past to Present)", fontsize=14)
plt.xlabel("Match Number (From Past to Present)", fontsize=12)
plt.ylabel("League Point", fontsize=12)
plt.yticks(
    range(1, len(tier_labels) + 1),
    tier_labels
)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
