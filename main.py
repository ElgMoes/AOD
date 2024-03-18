import numpy as np
import xarray as xr
import datetime
import json
import matplotlib.pyplot as plt
import cartopy
from icecream import ic

# JSON openen voor data 
with open('TrAtlDrifter.json') as fp:
    drifter: list = json.load(fp)

# Data splitsen in juiste lijsten
N: int = len(drifter)
lon: list = [drifter[i][2] for i in range(N)]
lat: list = [drifter[i][1] for i in range(N)]
time: list = [np.datetime64(drifter[i][0]) for i in range(N)]

# Slice maken om stukken van de lijsten te selecteren
begin: int = 1500
eind: int = 2500

I: slice = slice(begin, eind)

# Tijdsverschil berekenen
tijd_begin: str = time[begin]
tijd_eind: str = time[eind]
tijd_verschil = tijd_eind - tijd_begin

# We gebruiken hieronder de PlateCarree projectie;
# op de Cartopy website kun je ook andere projecties vinden als je daar meet wilt spelen
projection: object = cartopy.crs.PlateCarree()

# initialisatie van de figuur
fig: object = plt.figure(figsize=(12, 5))
ax: object = fig.add_subplot(1, 1, 1, projection=projection)

# plot de kustlijnen en maak het land beige
ax.coastlines(resolution='50m')
ax.add_feature(cartopy.feature.LAND)

# plot het traject, let op dat we een transformatie moeten gebruiken naar cartopy.crs.PlateCarree(),
# ook als je hierboven de projectie hebt veranderd
ax.plot(lon[I], lat[I], transform=cartopy.crs.PlateCarree())

# de code hieronder plot lichtgrijze lijnen voor het longitude/latitude grid en zorgt voor goede formatiing van de labels
gl: object = ax.gridlines(crs=cartopy.crs.PlateCarree(), draw_labels=True, linewidth=0.5,
              color='gray', alpha=0.5, linestyle='--')
gl.top_labels = False
gl.right_labels = False
gl.xformatter = cartopy.mpl.gridliner.LONGITUDE_FORMATTER
gl.yformatter = cartopy.mpl.gridliner.LATITUDE_FORMATTER

plt.show()