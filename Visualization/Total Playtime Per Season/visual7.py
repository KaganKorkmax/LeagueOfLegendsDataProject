import pandas as pd
import matplotlib.pyplot as plt

file_path = "match_data_20250110_154758.txt"

seasons = {
    "Season 1": 0,
    "Season 2": 0,
    "Season 3": 0
}

with open(file_path, "r", encoding="utf-8") as f:
    next(f)
    for line in f:
        parts = line.strip().split(",")
        if len(parts) < 6 or "N/A" in line:
            continue

        try:
            date_info = parts[0].strip()

            if "2 ay önce" in date_info:
                season_key = "Season 1"
            elif "bir ay önce" in date_info:
                season_key = "Season 2"
            elif "gün önce" in date_info:
                season_key = "Season 3"
            else:
                continue

            seasons[season_key] += 1
        except Exception as e:
            print(f"[ERROR] Line could not be processed: {line.strip()} - Error: {e}")

match_duration_hours = 40 / 60
season_playtimes = {season: round(count * match_duration_hours, 2) for season, count in seasons.items()}

plt.figure(figsize=(10, 6))
x_labels = list(season_playtimes.keys())
y_values = list(season_playtimes.values())

plt.bar(x_labels, y_values, color="skyblue", alpha=0.8)

for i, hours in enumerate(y_values):
    plt.text(i, hours + 0.5, f"{hours} hours", ha="center", fontsize=12)

plt.title("Total Playtime Per Season (Hours)", fontsize=14)
plt.xlabel("Seasons", fontsize=12)
plt.ylabel("Playtime (Hours)", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

print("Total Playtime Per Season:")
for season, hours in season_playtimes.items():
    print(f"{season}: {hours} hours")
