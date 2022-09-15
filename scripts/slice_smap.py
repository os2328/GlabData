# this script slices downloaded SMAP SM according to the given box coordinates with an option to choose specific months

import numpy as np
import pandas as pd

data_dir = '/burg/glab/users/os2328/data/'
d =  data_dir + 'smapampm9km_2015_2022.pkl'
data =  pd.read_pickle(d)

data = data[['lat','lon', 'date', 'sm_am']] # taking only SM at AM (morning)

#define your box here
lat_north = 65
lat_south = 25
lon_west = -15
lon_east = 35
dir_to_save = '/burg/glab/users/os2328/data/new_smap_raw/'

months = np.arange(5,8) # May, June, July

europe = data[(data['lat']>= lat_south) & (data['lat']<= lat_north)].copy()
europe = europe[(europe['lon']<=lon_east) & (europe['lon']>=lon_west)]

# save data here if you only needed a box

europe.to_pickle( dir_to_save + 'smap9km_europe.pkl', protocol = 4)

# proceed if you want specific months/average

europe['date'] = pd.to_datetime(europe['date'])

europe['year'] =  europe['date'].dt.year
europe['month'] =  europe['date'].dt.month
europe['doy'] =  europe['date'].dt.dayofyear

box1_m = europe[europe['month'].isin(months)] # only data in the defined months


box1_before22 = box1_m[box1_m['year']<2022]   # data before 2022
box1_22 = box1_m[box1_m['year']==2022]        # data in 2022


box1_gr = box1_22.groupby(['lat', 'lon', 'doy'])['sm_am'].mean()    # average data per location in 2022
box1_ts = box1_before22.groupby(['lat', 'lon', 'doy'])['sm_am'].mean() # average data per location in 2015-2021

box1_gr = box1_gr.reset_index()
box1_ts = box1_ts.reset_index()

ts_std = box1_before22.groupby([ 'lat', 'lon', 'doy'])[ 'sm_am'].std()
ts_std = ts_std.reset_index()
box1_ts= pd.merge(box1_ts, ts_std, on=[ 'lat', 'lon', 'doy'], how = 'outer')

box1_ts['range_m'] = box1_ts['sm_am_x']-box1_ts['sm_am_y']
box1_ts['range_p'] = box1_ts['sm_am_x']+box1_ts['sm_am_y']


box1_ts = pd.merge(box1_gr, box1_ts, on =['lat', 'lon','doy'])

box1_ts['date'] = pd.to_datetime(box1_ts['doy'], format='%j').dt.strftime('%m-%d')

box1_ts = box1_ts.groupby(['doy'])['sm_am', 'sm_am_x', 'range_m', 'range_p'].mean()

box1_ts = box1_ts.reset_index()

box1_ts.to_pickle(dir_to_save + 'box_new_ts.pkl', protocol = 4)




