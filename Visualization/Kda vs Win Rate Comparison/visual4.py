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
                    kda = float(parts[5].split("=")[1].replace(":1", "").strip())
                    win_rate = int(parts[4].split("=")[1].replace("%", "").strip())
                    
                    if win_rate > 0:
                        if win_rate < 100:
                            data.append({"Champion": champ, "KDA": kda, "Win Rate": win_rate})
                except Exception as e:
                    print(f"[ERROR] Line could not be processed: {line.strip()} - Error: {e}")

df = pd.DataFrame(data)

df_grouped = df.groupby("Champion").agg(
    Average_KDA=("KDA", "mean"),
    Average_Win_Rate=("Win Rate", "mean")
).reset_index()

df_grouped = df_grouped.sort_values("Average_KDA")

plt.figure(figsize=(12, 6))
plt.plot(
    df_grouped["Average_KDA"],
    df_grouped["Average_Win_Rate"],
    marker="o",
    linestyle="-",
    color="b",
    alpha=0.7
)

plt.title("KDA vs Win Rate Comparison (0 Win Rate Ignored))", fontsize=14)
plt.xlabel("KDA (Ascending Order)", fontsize=12)
plt.ylabel("Win Rate (%)", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()


print(df_grouped)
