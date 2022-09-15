# this script slices monthly VODCA data saved as 1 .pkl file to get data closest to the given location

import pandas as pd
import numpy as np


file_data = '/burg/glab/users/os2328/data/VODCA-related/vodca20022014monthly.pkl'
vod = pd.read_pickle(file_data)

# fill you data here
loc_name = 'FI-Hyy'
loc_lat = 61.875
loc_lon = 243.375
distance_threshold = 0.1 # do not accept VODCA data if it is farther than this threshold from the location of interest
save_to_dir = '/burg/glab/users/os2328/data/VODCA-related/'


out0 = vod[abs(vod['lat']-loc_lat) < distance_threshold].copy()
ll = out0['lat'].unique()

if len(ll)>1:
  lat_th = min(np.abs(ll-loc_lat))  +0.0001
  out0 = vod[abs(vod['lat']-loc_lat)< lat_th].copy()
  ll = out0['lat'].unique()
  
if len(ll)<1:
  print('there is no VODCA data withing the defined threshold (latitude). Try to increace it')
  quit()

out1 = out0[abs(out0['lon']-loc_lon) < distance_threshold].copy()
ln = out1['lon'].unique()

if len(ln)<1:
  print('there is no VODCA data withing the defined threshold (longitude). Try to increace it')
  quit()
  
if len(ln)>1:
  lon_th = min(np.abs(ln-loc_lon))  +0.0001
  out1 = out0[abs(out0['lon']-loc_lon) < lon_th].copy()
  ln = out1['lon'].unique()
  
print('VODCA data for ' + loc_name + ' is from latitude = ' + ll + ' and longitude = ' + ln)
name_ = 'VODCAvod_' +  loc_name + '.pkl'
out1.to_pickle(save_to_dir + name_, protocol = 4)
  
