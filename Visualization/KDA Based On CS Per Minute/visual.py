import pandas as pd
import matplotlib.pyplot as plt

file_path = "match_data_20250110_154758.txt"

data = pd.read_csv(file_path)

data['CS_Per_Min'] = data['CS'].str.extract(r'\((\d+\.?\d*)\)').astype(float)

def safe_int_conversion(value):
    try:
        return int(value)
    except (ValueError, IndexError):
        return 0

data['Kills'] = data['K/D/A'].apply(lambda x: safe_int_conversion(x.split('/')[0]))
data['Deaths'] = data['K/D/A'].apply(lambda x: safe_int_conversion(x.split('/')[1]))
data['Assists'] = data['K/D/A'].apply(lambda x: safe_int_conversion(x.split('/')[2]))

data['KDA'] = data.apply(lambda row: (row['Kills'] + row['Assists']) / row['Deaths'] if row['Deaths'] > 0 else (row['Kills'] + row['Assists']), axis=1)

sorted_data = data.sort_values('CS_Per_Min')

plt.bar(sorted_data['CS_Per_Min'], sorted_data['KDA'], color='b', alpha=0.7)
plt.title('KDA Based on CS Per Minute')
plt.xlabel('CS Per Minute')
plt.ylabel('KDA')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
