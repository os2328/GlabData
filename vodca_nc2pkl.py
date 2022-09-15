# this script takes netcdf files (in this case - VODCA C-band) and makes one large .pkl file out of them. Then, global *monthly* data is calculated. 
# only VOD variable is taken


data_dir = '/burg/glab/users/os2328/data/vodca/'

data_list_full = [f for f in os.listdir(data_dir) if f.endswith('.nc')]

overlap_all = pd.DataFrame({'lat': [], 'lon': [], 'vod': [],  'date': []})


for h in data_list_full:
    hf = data_dir +h
    dataset = nc.Dataset(hf,'r', maskandscale = True)

    vod = dataset.variables['vod'][:]
    vod = vod[0,:,:]
    vod1 = vod.ravel()
    filt_h = vod1> 0

    data = vod1[filt_h] #only data is taken, not -9999


    lat = dataset.variables['lat']
    lat = lat[:].copy()
    lon = dataset.variables['lon']
    lon = lon[:].copy()
    lat1 = np.broadcast_to(np.matrix(lat).transpose(), (tbh.shape[0], tbh.shape[1]))
    lon1=  np.broadcast_to(lon, (tbh.shape[0], tbh.shape[1]))

    lat1 = lat1.ravel().transpose()
    lon1 = lon1.ravel()
    latitude = lat1[filt_h]
    longitude = lon1[filt_h]
    latitude = np.asarray(latitude).reshape(-1)
    all_data=pd.DataFrame({'lat': latitude, 'lon': longitude, 'vod': data7 })
    
    dataset.close()

    from_name_ = hf.split("/burg/glab/users/os2328/data/vodca/vodca_v01-0_C-band_",1)[1]
    date = from_name_[:10]
    
    all_data['date'] = date
    overlap_all = overlap_all.append(all_data)

print(overlap_all.head())
print(overlap_all.tail())
print(overlap_all.shape)


# at this point, it is the dataset with all VOD data

# now calculating monthly means per location

overlap_all['date'] = pd.to_datetime(overlap_all['date'])
g = overlap_all.groupby([pd.Grouper(key="date", freq="M"), 'lat', 'lon']).mean()
g = g.reset_index()
print(g.head())
print(g.tail())
print(g.shape)

g.to_pickle('/burg/glab/users/os2328/data/vodca20022014monthly.pkl', protocol = 4)

