from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('12-20_chapters_projects/data_visualization/weather_data/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

paath = Path('12-20_chapters_projects/data_visualization/weather_data/death_valley_2021_simple.csv')
liines = paath.read_text(encoding='utf-8').splitlines()
reeader = csv.reader(liines)
heeader_row = next(reeader)

# Extraxt dates, and high and low temperatures
dates, highs, lows, prcps = [], [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = int(row[7])
        low = int(row[8])
        prcp = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        prcps.append(prcp)

# Extraxt dates, and high and low temperatures
daates, hiighs, loows = [], [], []
for row in reeader:
    cuurrent_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        hiigh = int(row[3])
        loow = int(row[4])
    except ValueError:
        print(f"Missing data for {cuurrent_date}")
    else:
        daates.append(cuurrent_date)
        hiighs.append(hiigh)
        loows.append(loow)




# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(daates, hiighs, color='yellow', alpha=0.5)
ax.plot(daates, loows, color='purple', alpha=0.5)
ax.fill_between(daates, hiighs, loows, facecolor='purple', alpha=0.1)
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
# ax.plot(dates, prcps, color='green', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily High and Low temperatures, 2021", fontsize=24)
ax.set_xlabel('Death_valley(High_yellow, Low_purple)\nSitka(High_red, Low_blue)', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.savefig('plot_1.png', bbox_inches='tight')
# plt.show()

