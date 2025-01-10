import pandas as pd
import matplotlib.pyplot as plt

season_files = ["Sezon_2024_S1.txt", "Sezon_2024_S2.txt", "Sezon_2024_S3.txt"]

data = []

for season_file in season_files:
    with open(season_file, "r", encoding="utf-8") as f:
        for line in f:
            if "Champ=" in line:
                parts = line.split(",")
                try:
                    champ = parts[1].split("=")[1].strip()
                    wins = int(parts[2].split("=")[1].replace("G", "").strip())
                    losses = int(parts[3].split("=")[1].replace("Y", "").strip())
                    kda = float(parts[5].split("=")[1].replace(":1", "").strip())
                    total_games = wins + losses
                    data.append({"Champion": champ, "Total Games": total_games, "KDA": kda})
                except Exception as e:
                    print(f"[ERROR] Line could not be processed: {line.strip()} - Error: {e}")

df = pd.DataFrame(data)

df_grouped = df.groupby("Champion").agg(
    Total_Games=("Total Games", "sum"),
    Average_KDA=("KDA", "mean")
).reset_index()

top_10 = df_grouped.nlargest(10, "Total_Games").sort_values("Total_Games")

plt.figure(figsize=(12, 6))
plt.bar(top_10["Champion"], top_10["Average_KDA"], color="b", alpha=0.7)

plt.title("Top 10 Most Played Champions and Their KDA Values", fontsize=14)
plt.xlabel("Champions (Sorted by Play Count)", fontsize=12)
plt.ylabel("Average KDA", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

print("Top 10 Most Played Champions and Their KDA Values:")
print(top_10)
