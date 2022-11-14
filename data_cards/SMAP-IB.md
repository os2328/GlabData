# SMAP IB VOD and Soil Moisture

**Short description**

A new mono-angle retrieval algorithm (called SMAP-INRAE-BORDEAUX, hereafter SMAP-IB) of SM and L-band VOD (L-VOD) from the dual-channel SMAP radiometric observations. The retrievals are based on the L-MEB (L-band Microwave Emission of the Biosphere) model which is the forward model of SMOS-IC and of the official SMOS retrieval algorithms. The SMAP-IB product aims at providing good performances for both SM and L-VOD while remaining independent of auxiliary data: neither modelled SM data nor optical vegetation indices are used as input in the algorithm. 


| Parameter     | Description |
| ---      | ---       |
| Variables            |    Soil moisture, Vegetation optical depth      |
| Variable name in the dataset and units  |  Soil_Moisture:units = m3/m3; Optical_Thickness_Nad:long_name = Vegetation Optical Thickness at Nadir|
| Temporal resolution  |    daily      |
| Spatial resolution   |    36 by 36 km                 |
| Temporal coverage    |  SM 2015-2021; VOD 2015-2019                   |
| Spatial coverage     |   global                  |
| Projection           |   EASE-Grid 2.0                  |
| URL                  | [Web page](https://ib.remote-sensing.inrae.fr/index.php/2022/02/03/a-new-smap-soil-moisture-and-vegetation-optical-depth-product-smap-ib-is-available/ )                   |
| Avaliable downloaded |  Soil Moisture /burg/glab/users/os2328/data/VOD_project/smap_ib_xr.zarr; VOD /burg/glab/users/os2328/data/VOD_project/VOD-IB/smap_ib_vod_xr.zarr                   |
| Size                 |                     |
| File format          |    netcdf on the website; downloaded and stored as .zarr xarray                 |
| Good for             |   should be very good quality - enhanced SMAP                  |
| Bad because          |  VOD might be noisy (under investigation); very short temporal coverage for VOD                   |



**Relevant scripts**

ask os2328 



**Relevant publications**

1. Li, X., Wigneron, J.P., Fan, L., Frappart, F., Yueh, S.H., Colliander, A., Ebtehaj, A., Gao, L., Fernandez-Moran, R., Liu, X. and Wang, M., 2022. A new SMAP soil moisture and vegetation optical depth product (SMAP-IB): Algorithm, assessment and inter-comparison. Remote Sensing of Environment, 271, p.112921. [[doi](https://doi.org/10.1016/j.rse.2022.112921)](https://www.sciencedirect.com/science/article/pii/S0034425722000359)
