# ATMS-597-Project3-GroupF
ATMS-597 Project 3 Group F
## Description
This project first uses xarray to organize and reduce Global Precipitation Climatology Project (GPCP) data from 1996-2019. Once downloaded usin wget, the data is merged into one file. The data is subsetted for the grid point closest to Cordoba, Argentina for the months of DJF, and missing data is removed. The days where DJF precipitation met or was greater than the 95th percentile are then subsetted and saved into a new netCDF file for later use. A cumulative distribution function is then plotted of all DJF precipitation days with the 95th percentile value highlighted.

The 95th percentile DJF precipitation data is then used along with NCEP Reanalysis data to compute the global mean fields and seasonal anomaly fields using the 1981-2010 period to calculate the anomalies. This is done for 250 hPa wind speed and vectors, 500 hPa wind speed and vectors, 500 hPa geopotential height, 850 hPa temperature, 850 hPa specific humidity, 850 hPa winds, skin temperature, surface wind vectors, and total atmospheric column water vapor. Finally, maps showing the mean fields for the extreme precipitatin day composites, the long term mean composites for DJF, and the anomaly fields for each variable are created.

## Usage
Without modifications, this script will complete the analysis described above for the grid point closest to Cordoba, Argentina for the months of DJF. The location can be changed within the .sel() command when the data is loaded by specifying a new latitude and longitude. The selected season can be changed by changing the season within the df_winter variable to another 3 month identifier of either 'MAM', 'JJA', or 'SON'. The percentile can be changed by changing the .quantile() value with the DJF_daily_precip_95 variable. The global mean and seasonal anomaly fields will then be calculated and plotted for the new subsetted data and selected percentile.

## Authors and acknowledgment
Group F: Rylan Housenga, Rose Miller, and Michael Sessa


Data Citations:
Pendergrass, Angeline & National Center for Atmospheric Research Staff (Eds). Last modified 01 Jul 2016. "The Climate Data Guide: GPCP (Daily): Global Precipitation Climatology Project." Retrieved from https://climatedataguide.ucar.edu/climate-data/gpcp-daily-global-precipitation-climatology-project.

Kalnay et al. 1996. The NCEP/NCAR 40-year reanalysis project, Bull. Amer. Meteor. Soc., 77, 437-470.

This project is licensed under the MIT License - see the LICENSE.md file for details
