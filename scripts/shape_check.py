import pandas as pd
import matplotlib.pyplot as plt
import requests
import numpy as np
shapes = pd.read_csv('~/Downloads/buses/israel-public-transportation/shapes.txt', sep=',')
shapes = shapes[shapes['shape_id']==163544]
short_name = 277
json_url = 'https://open-bus-stride-api.hasadna.org.il/route_timetable/list?line_refs=11537&planned_start_time_date_from=2026-06-16T15:48:49%2B02:00&planned_start_time_date_to=2026-06-17T15:48:49%2B02:00&limit=100'
timetable = requests.get(json_url).json()
latlon = []
for ii in range(len(timetable)):
    latlon.append([timetable[ii]['lat'],timetable[ii]['lon']])
latlon = np.array(latlon)   
plt.figure()
plt.plot(shapes['shape_pt_lon'],shapes['shape_pt_lat'],'k')
plt.plot(latlon[:,1],latlon[:,0],'ob')
plt.grid()
plt.axis('equal')

