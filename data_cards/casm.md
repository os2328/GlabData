# CASM Soil Moisture

Skulovich, Olya;   Gentine, Pierre

The Consistent Artificial Intelligence (AI)-based Soil Moisture (CASM) dataset is a global, consistent, and long-term, remote sensing soil moisture (SM) dataset created using machine learning. It is based on the NASA Soil Moisture Active Passive (SMAP) satellite mission SM data as a target and is aimed at extrapolating SMAP-like quality SM data back in time with previous satellite microwave platforms. Machine learning approach, such as neural network (NN) has the advantage of being both nonlinear, and state-dependent, and naturally imposing a global distribution matching between the source and the target data. Utilizing this, the new CASM dataset was created using high-quality SMAP SM as a target and Soil Moisture and Ocean Salinity (SMOS) or Advanced Microwave Scanning Radiometer - Earth Observing System (AMSR-E/2) brightness temperature as a source, which allowed extrapolating SM data 13 years back from before SMAP mission launch. CASM represents SM in the top soil layer, defined on a global 25 km EASE-2 grid and covers 2002-2020 with a 3-day temporal resolution. The resulting dataset exhibits excellent spatial and temporal homogeneity, without compromising the interannual variability, and is in excellent agreement with the SMAP data (with a mean correlation of 0.97 between the SMAP and CASM SM for the period when the two overlap). Moreover, the input and target datasets were divided into seasonal cycle and residuals, with the NN trained on the residuals. This approach ensures that the high performance does not mask a simple seasonal cycle matching but rather exemplifies the skill targeted at predicting extremes; with the NN achieving a correlation of 0.75 on the test data for the residuals. Comparison to 367 global in-situ SM monitoring sites shows a SMAP-like median correlation of 0.66 between station SM and CASM SM from the corresponding grid cell. Additionally, the SM product uncertainty was assessed, and both aleatoric and epistemic uncertainties were estimated and included in the dataset. Mean epistemic uncertainty, related to the NN model structure, ranges from 0.007 m3/m3 to 0.014 m3/m3 and on average is close to a desired SM product stability threshold of 0.01 m3/m3 per year. Aleatoric uncertainty, defined as input noise propagated through the system, depends on the introduced level of noise. With 10% noise applied to the residuals, the resulting mean standard deviation of the model outputs rises from 0.005 to 0.007 m3/m3.   



| Parameter     | Description |
| ---      | ---       |
| Variables            |    Soil Moisture      |
| Temporal resolution  |    3-day      |
| Spatial resolution   |   25 km                  |
| Temporal coverage    |    2002-2020                 |
| Spatial coverage     |     Global                |
| Projection           |     EASE-2                |
| URL                  |    [Zenodo](https://zenodo.org/record/7072512#.Y01cQi-B2-u); [Pangeo](https://pangeo-forge.org/dashboard/feedstock/85)                 |
| Avaliable downloaded |   /burg/glab/users/os2328/data/casm_dataset.pkl 24Gb; /burg/glab/users/os2328/data/casm_xr.zarr                  |
| Size                 |   19 yearly .nc files, 1.3-2.6 Gb each                  |
| File format          |     netCDF, zarr                |
| Good for             |   relatively long-term SM                  |
| Bad because          |   1) satellite-based - not good in regions with dense vegetation, high elevations; 2) a new dataset - might be not known to scientific community                    |



**Relevant scripts**




**Relevant publications**

1. O. Skulovich, P. Gentine, 2022, "CASM: A long-term Consistent AI-based Soil Moisture dataset based on machine learning and remote sensing" Manuscript submitted for publication. 
