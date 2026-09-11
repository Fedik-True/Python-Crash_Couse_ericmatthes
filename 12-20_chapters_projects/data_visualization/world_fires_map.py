from pathlib import Path
import csv
import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('12-20_chapters_projects/data_visualization/eq_data/world_fires_1_day.csv')
contents = path.read_text(encoding='utf-8')
reader = csv.reader(contents.splitlines())
header_roww = next(reader)

# Examine all earthquakes in the dataset.

lats, lons, brights = [], [], []
for row in reader:
    lat = float(row[0])
    lon = float(row[1])
    bright = float(row[2])

    lats.append(lat)
    lons.append(lon)
    brights.append(bright)


title = "World Fires in 1 Day"
fig = px.scatter_geo(lat=lats,
                     lon=lons,
                     size=brights,
                     title=title,
                     color=brights,
                     color_continuous_scale='agsunset',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     )
fig.show()

