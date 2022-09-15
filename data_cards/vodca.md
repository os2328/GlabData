# VODCA

**Short description**

Vegetation optical depth (VOD) describes the attenuation of radiation by plants. VOD a function of frequency as well as vegetation water content, and by extension biomass. VOD has many possible applications in studies of the biosphere, such as biomass monitoring, drought monitoring, phenology analyzes or fire risk management.

We merged VOD observations from various spaceborne sensors (SSM/I, TMI, AMSR-E, AMSR2, WindSat) to create global long-term vod time series. Prior to aggregation the data has been rescaled to AMSR-E, removing systematic differences between them.

There is a product for C-band (~6.9 GHz, 2002 - 2018), X-band (10.7 GHz, 1997 - 2018) and Ku-band (~19 GHz, 1987 - 2017). The data is global sampled on a regular 0.25 degrees grid. Each product is available as daily global netcdf4 files.

 

Currently there is an issue with opening the file using ESA SNAP. As an alternative Panoply can be used to quickly visualize the data. 

An update of VODCA, addressing this issue and potentially including an extension of the dataset, is foreseen to be published on Zenodo early 2020.



| Parameter     | Description |
| ---      | ---       |
| Variables            |    VOD      |
| Temporal resolution  |    daily      |
| Spatial resolution   |   0.25 degrees grid                  |
| Temporal coverage    |      C-band - 2002-2018; X-band - 1997-2018, Ku-band - 1987-2017               |
| Spatial coverage     |      global               |
| Projection           |                     |
| URL                  |    [zenodo storage](https://zenodo.org/record/2575599#.YyM6TC-B2MI)                 |
| Avaliable downloaded |     /burg/glab/users/os2328/data/VODCA-related/vodca/VODCA_C-band_2002-2018_v01.0.0.zip  4.3G; <br> /burg/glab/users/os2328/data/VODCA-related/vodca20022014monthly.pkl   772Mb monthly mean, global            |
| Size                 |   C-band - 140 GB unzipped; X-band - 180 GB unzipped; Ku-band - 270 GB unzipped                  |
| File format          |      netcdf4               |
| Good for             |                     |
| Bad because          |                     |



**Relevant scripts**

- [Monthly mean, 1 .pkl file from all .nc files](scripts/vodca_nc2pkl.py)
- [Closest data to a given location](scripts/vodca_slice_point.py)


**Relevant publications**

1. Moesinger, L., Dorigo, W., de Jeu, R., van der Schalie, R., Scanlon, T., Teubner, I. and Forkel, M., 2020. The global long-term microwave vegetation optical depth climate archive (VODCA). Earth System Science Data, 12(1), pp.177-196. [doi](https://doi.org/10.5194/essd-12-177-2020)
2. Wild, B., Teubner, I., Moesinger, L., Zotta, R.M., Forkel, M., van der Schalie, R., Sitch, S. and Dorigo, W., 2022. VODCA2GPP–a new, global, long-term (1988–2020) gross primary production dataset from microwave remote sensing. Earth System Science Data, 14(3), pp.1063-1085.[doi](https://doi.org/10.5194/essd-14-1063-2022)
3. Teubner, I.E., Forkel, M., Wild, B., Mösinger, L. and Dorigo, W., 2021. Impact of temperature and water availability on microwave-derived gross primary production. Biogeosciences, 18(11), pp.3285-3308.[doi](https://doi.org/10.5194/bg-18-3285-2021)
4. Schmidt, L., Forkel, M., Zotta, R.-M., Scherrer, S., Dorigo, W. A., Kuhn-Régnier, A., van der Schalie, R., and Yebra, M.: Assessing the sensitivity of multi-frequency passive microwave vegetation optical depth to vegetation properties, Biogeosciences Discuss. preprint, [doi](https://doi.org/10.5194/bg-2022-85), in review, 2022.



