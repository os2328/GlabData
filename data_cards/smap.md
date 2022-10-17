# SMAP Enhanced L3 Radiometer Global and Polar Grid Daily 9 km EASE-Grid Soil Moisture, Version 5 (SPL3SMP_E)

**Short description**

This enhanced Level-3 (L3) soil moisture product provides a composite of daily estimates of global land surface conditions retrieved by the Soil Moisture Active Passive (SMAP) radiometer. This product is a daily composite of SMAP Level-2 (L2) soil moisture which is derived from SMAP Level-1C (L1C) interpolated brightness temperatures. Backus-Gilbert optimal interpolation techniques are used to extract information from SMAP antenna temperatures and convert them to brightness temperatures, which are posted to the 9 km Equal-Area Scalable Earth Grid, Version 2.0 (EASE-Grid 2.0) in a global cylindrical projection. As of 2021, the data are also posted to the Northern Hemisphere EASE-Grid 2.0, an azimuthal equal-area projection.

| Parameter     | Description |
| ---      | ---       |
| Variables            |    Brightness Temperature, Soil Moisture      |
| Temporal resolution  |    daily      |
| Spatial resolution   |    9 km                  |
| Temporal coverage    |   2015-present                  |
| Spatial coverage     |    global                 |
| Projection           |     EASE-Grid 2.0                |
| URL                  | [NSIDC](https://nsidc.org/data/spl3smp_e/versions/5)                    |
| Avaliable downloaded |  /burg/glab/users/os2328/data/smapampm9km_2015_2022.pkl  74Gb                   |
| Size                 |                     |
| File format          |       HDF5              |
| Good for             |   best satellite soil moisture                  |
| Bad because          |   only starts in 2015, satellite-based - so not great for dense vegetation, high elevation, etc.                  |



**Relevant scripts**

[slice data](../scripts/slice_smap.py)


**Relevant publications**

1. [user guide](https://nsidc.org/sites/default/files/spl3smp_e-v005-userguide.pdf)
2. HOW_TO_CITE: O'Neill, P. E., S. Chan, E. G. Njoku, T. Jackson, R. Bindlish, J. Chaubell, and A. Colliander. (2021). SMAP Enhanced L3 Radiometer Global and Polar Grid Daily 9 km EASE-Grid Soil Moisture, Version 5 [Data Set]. Boulder, Colorado USA. NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/4DQ54OUIJ9DL. Date Accessed 09-15-2022.
