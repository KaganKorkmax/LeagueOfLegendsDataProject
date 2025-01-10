import pandas as pd
import matplotlib.pyplot as plt

season_files = ["Sezon_2024_S1.txt", "Sezon_2024_S2.txt", "Sezon_2024_S3.txt"]
data = []

for file in season_files:
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if "Champ=" in line:
                parts = line.split(",")
                try:
                    rank = parts[0].split("=")[1].strip()
                    champ = parts[1].split("=")[1].strip()
                    wins = int(parts[2].split("=")[1].replace("G", "").strip())
                    losses = int(parts[3].split("=")[1].replace("Y", "").strip())
                    ratio = int(parts[4].split("=")[1].replace("%", "").strip()) if "N/A" not in parts[4] else 0
                    data.append({
                        "Rank": rank,
                        "Champion": champ,
                        "Wins": wins,
                        "Losses": losses,
                        "Win Rate": ratio
                    })
                except Exception as e:
                    print(f"[ERROR] Line could not be processed: {line.strip()} - Error: {e}")

all_data = pd.DataFrame(data)

all_data["Total Games"] = all_data["Wins"] + all_data["Losses"]

character_stats = all_data.groupby("Champion").agg(
    Total_Games=("Total Games", "sum"),
    Average_Win_Rate=("Win Rate", "mean")
).reset_index()

top_10_characters = character_stats.nlargest(10, "Total_Games")

print("Top 10 Most Played Champions and Their Average Win Rates:")
print(top_10_characters)

plt.figure(figsize=(12, 6))
plt.bar(top_10_characters["Champion"], top_10_characters["Total_Games"], alpha=0.7, label="Total Games")
plt.plot(
    top_10_characters["Champion"],
    top_10_characters["Average_Win_Rate"],
    color="red",
    marker="o",
    label="Average Win Rate (%)"
)


plt.title("Top 10 Most Played Champions and Their Win Rates", fontsize=14)
plt.xlabel("Champions", fontsize=12)
plt.ylabel("Games Played and Win Rate", fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

top_10_characters.to_csv("top_10_characters_win_rate.csv", index=False, encoding="utf-8")
