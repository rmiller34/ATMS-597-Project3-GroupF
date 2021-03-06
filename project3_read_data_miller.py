# -*- coding: utf-8 -*-
"""Project3_Read_Data_Miller.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oURKgW72YXF75r_R7RUHgMyRALqK-08S
"""

# Commented out IPython magic to ensure Python compatibility.
#Part 2 of reading in reanalysis data
#Import the packages that we need
# %pylab inline
import pandas as pd
import glob
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
!pip install netCDF4
!pip install pydap
from netCDF4 import Dataset

# Commented out IPython magic to ensure Python compatibility.
#mount google drive to retrieve nc file from part 1
from google.colab import drive
drive.mount('/content/drive')
# %cd /content/drive/My Drive/Project3/Combined

#Read in file into a dataset
Precip_dates_data = xr.open_dataset('DJF.nc')
Precip_dates_data_array = Precip_dates_data['time']
#check a date
Precip_dates_data['time'][Precip_dates_data['time.year'].values == 1996]

# This is where we import the NCEP Reanalysis fields directly from the NOAA THREDDS server. This code segment will only selecte the extreme precipitation days and retrieve those files.
# Create empty datasets for the years 1999-2019
years = np.arange(1996,2020)

datasets_Uwind_250hPa = []
datasets_Vwind_250hPa = []
datasets_GeopHgt_500hPa = []
datasets_Uwind_500hPa = []
datasets_Vwind_500hPa = []
datasets_Omega_500hPa = []
datasets_Uwind_850hPa = []
datasets_Vwind_850hPa = []
datasets_SpecHum_850hPa = []
datasets_AirTemp_850hPa = []
datasets_Uwind_sig995 = []
datasets_Vwind_sig995 = []
datasets_skt_Sfc = []
datasets_pr_wtr = []

# This runs through to check that each year is present to pull files for
for iyr in years:

    print('working on '+str(iyr))

    if len(Precip_dates_data['time'][Precip_dates_data['time.year'].values==iyr]) > 0:
      dates_year = Precip_dates_data['time'][Precip_dates_data['time.year'].values ==iyr]

      #Extract data from the NCEP reanalysis dataset
      # sel(level) allows us to pull out only certian levels of intformation needed. ex: level=250 retrieves the Uwind value at 250hPa
      ds_Uwind_250hPa = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.dailyavgs/pressure/uwnd.'+str(iyr)+'.nc',engine='netcdf4').sel(\
                            level=250, time=dates_year)
      ds_Vwind_250hPa = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.dailyavgs/pressure/vwnd.'+str(iyr)+'.nc',engine='netcdf4').sel(\
                            level=250, time=dates_year)
      ds_GeopHgt_500hPa = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.dailyavgs/pressure/hgt.'+str(iyr)+'.nc',engine='netcdf4').sel(\
                            level=500, time=dates_year)
      ds_Uwind_500hPa = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.dailyavgs/pressure/uwnd.'+str(iyr)+'.nc',engine='netcdf4').sel(\
                            level=500, time=dates_year)
      ds_Vwind_500hPa = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.dailyavgs/pressure/vwnd.'+str(iyr)+'.nc',engine='netcdf4').sel(\
                            level=500, time=dates_year)
      ds_Omega_500hPa = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.dailyavgs/pressure/omega.'+str(iyr)+'.nc',engine='netcdf4').sel(\
                            level=500, time=dates_year)
      ds_Uwind_850hPa = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.dailyavgs/pressure/uwnd.'+str(iyr)+'.nc',engine='netcdf4').sel(\
                            level=850, time=dates_year)
      ds_Vwind_850hPa = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.dailyavgs/pressure/vwnd.'+str(iyr)+'.nc',engine='netcdf4').sel(\
                            level=850, time=dates_year)
      ds_SpecHum_850hPa = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.dailyavgs/pressure/shum.'+str(iyr)+'.nc',engine='netcdf4').sel(\
                            level=850, time=dates_year)
      ds_AirTemp_850hPa = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.dailyavgs/pressure/air.'+str(iyr)+'.nc',engine='netcdf4').sel(\
                            level=850, time=dates_year)
      ds_Uwind_sig995 = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.dailyavgs/surface/uwnd.sig995.'+str(iyr)+'.nc',engine='netcdf4').sel(\
                            time=dates_year)
      ds_Vwind_sig995 = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.dailyavgs/surface/vwnd.sig995.'+str(iyr)+'.nc',engine='netcdf4').sel(\
                            time=dates_year)
      ds_skt_Sfc = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.dailyavgs/surface_gauss/skt.sfc.gauss.'+str(iyr)+'.nc',engine='netcdf4').sel(\
                            time=dates_year)
      ds_pr_wtr = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.dailyavgs/surface/pr_wtr.eatm.'+str(iyr)+'.nc',engine='netcdf4').sel(\
                            time=dates_year)

      #Append data for use later
      datasets_Uwind_250hPa.append(ds_Uwind_250hPa)
      datasets_Vwind_250hPa.append(ds_Vwind_250hPa)
      datasets_GeopHgt_500hPa.append(ds_GeopHgt_500hPa)
      datasets_Uwind_500hPa.append(ds_Uwind_500hPa)
      datasets_Vwind_500hPa.append(ds_Vwind_500hPa)
      datasets_Omega_500hPa.append(ds_Omega_500hPa)
      datasets_Uwind_850hPa.append(ds_Uwind_850hPa)
      datasets_Vwind_850hPa.append(ds_Vwind_850hPa)
      datasets_SpecHum_850hPa.append(ds_SpecHum_850hPa)
      datasets_AirTemp_850hPa.append(ds_AirTemp_850hPa)
      datasets_Uwind_sig995.append(ds_Uwind_sig995)
      datasets_Vwind_sig995.append(ds_Vwind_sig995)
      datasets_skt_Sfc.append(ds_skt_Sfc)
      datasets_pr_wtr.append(ds_pr_wtr)

#This combines the DJF extreme precipitation days from each yearly file into 1 file for plotting
combined_Uwind_250hPa = xr.concat(datasets_Uwind_250hPa, dim='index')
combined_Vwind_250hPa = xr.concat(datasets_Vwind_250hPa, dim='index')
combined_GeopHgt_500hPa = xr.concat(datasets_GeopHgt_500hPa, dim='index')
combined_Uwind_500hPa = xr.concat(datasets_Uwind_500hPa, dim='index')
combined_Vwind_500hPa = xr.concat(datasets_Vwind_500hPa, dim='index')
combined_Omega_500hPa = xr.concat(datasets_Omega_500hPa, dim='index')
combined_Uwind_850hPa = xr.concat(datasets_Uwind_850hPa, dim='index')
combined_Vwind_850hPa = xr.concat(datasets_Vwind_850hPa, dim='index')
combined_SpecHum_850hPa = xr.concat(datasets_SpecHum_850hPa, dim='index')
combined_AirTemp_850hPa = xr.concat(datasets_AirTemp_850hPa, dim='index')
combined_Uwind_sig995 = xr.concat(datasets_Uwind_sig995, dim='index')
combined_Vwind_sig995 = xr.concat(datasets_Vwind_sig995, dim='index')
combined_skt_Sfc = xr.concat(datasets_skt_Sfc, dim='index')
combined_pr_wtr = xr.concat(datasets_pr_wtr, dim='index')

#This then converts those dataset files into a NETCDF 
combined_Uwind_250hPa.to_netcdf('combined_Uwind_250hPa_1996to2019_ExtremePrecipDays.nc')
combined_Vwind_250hPa.to_netcdf('combined_Vwind_250hPa_1996to2019_ExtremePrecipDays.nc')
combined_GeopHgt_500hPa.to_netcdf('combined_GeopHgt_500hPa_1996to2019_ExtremePrecipDays.nc')
combined_Uwind_500hPa.to_netcdf('combined_Uwind_500hPa_1996to2019_ExtremePrecipDays.nc')
combined_Vwind_500hPa.to_netcdf('combined_Vwind_500hPa_1996to2019_ExtremePrecipDays.nc')
combined_Omega_500hPa.to_netcdf('combined_Omega_500hPa_1996to2019_ExtremePrecipDays.nc')
combined_Uwind_850hPa.to_netcdf('combined_Uwind_850hPa_1996to2019_ExtremePrecipDays.nc')
combined_Vwind_850hPa.to_netcdf('combined_Vwind_850hPa_1996to2019_ExtremePrecipDays.nc')
combined_SpecHum_850hPa.to_netcdf('combined_SpecHum_850hPa_1996to2019_ExtremePrecipDays.nc')
combined_AirTemp_850hPa.to_netcdf('combined_AirTemp_850hPa_1996to2019_ExtremePrecipDays.nc')
combined_Uwind_sig995.to_netcdf('combined_Uwind_sig995_1996to2019_ExtremePrecipDays.nc')
combined_Vwind_sig995.to_netcdf('combined_Vwind_sig995_1996to2019_ExtremePrecipDays.nc')
combined_skt_Sfc.to_netcdf('combined_skt_Sfc_1996to2019_ExtremePrecipDays.nc')
combined_pr_wtr.to_netcdf('combined_pr_wtr_1996to2019_ExtremePrecipDays.nc')

# Move the created NETCDF files into your Google Drive
from google.colab import drive
drive.mount('/content/drive')
!mv *.nc "/content/drive/My Drive/Project3/Combined/"

## This section allows the importing of the long-term mean of the NCEP Reanalysis data from 1981-2010, only selecting DJF(which are the months of interest)
# The longterm mean files are in Gregorian time

months = xr.cftime_range(start='0001-01-01', end='0001-12-01', freq='MS', calendar = 'standard') # selecting long-term mean data for 1981-2010 with cftime.DatetimeGregorian format
months = months[(months.month==12)|(months.month==1)|(months.month==2)] # selecting long-term mean data for DJF in 1981-2010

# Extract data
ds_Uwind_250hPa_LTM = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/uwnd.mon.1981-2010.ltm.nc',engine='netcdf4').sel(\
                      level=250, time = months)
ds_Vwind_250hPa_LTM = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/vwnd.mon.1981-2010.ltm.nc',engine='netcdf4').sel(\
                      level=250, time = months)
ds_GeopHgt_500hPa_LTM = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/hgt.mon.1981-2010.ltm.nc',engine='netcdf4').sel(\
                      level=500, time = months)
ds_Uwind_500hPa_LTM = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/uwnd.mon.1981-2010.ltm.nc',engine='netcdf4').sel(\
                      level=500, time = months)
ds_Vwind_500hPa_LTM = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/vwnd.mon.1981-2010.ltm.nc',engine='netcdf4').sel(\
                      level=500, time = months)
ds_Omega_500hPa_LTM = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/omega.mon.1981-2010.ltm.nc',engine='netcdf4').sel(\
                      level=500, time = months)
ds_Uwind_850hPa_LTM = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/uwnd.mon.1981-2010.ltm.nc',engine='netcdf4').sel(\
                      level=850, time = months)
ds_Vwind_850hPa_LTM = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/vwnd.mon.1981-2010.ltm.nc',engine='netcdf4').sel(\
                      level=850, time = months)
ds_SpecHum_850hPa_LTM = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/shum.mon.1981-2010.ltm.nc',engine='netcdf4').sel(\
                      level=850, time = months)
ds_AirTemp_850hPa_LTM = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/air.mon.1981-2010.ltm.nc',engine='netcdf4').sel(\
                      level=850, time = months)
ds_Uwind_sig995_LTM = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/surface/uwnd.sig995.mon.1981-2010.ltm.nc',engine='netcdf4').sel(\
                      time = months)
ds_Vwind_sig995_LTM = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/surface/vwnd.sig995.mon.1981-2010.ltm.nc',engine='netcdf4').sel(\
                      time = months)
ds_skt_Sfc_LTM = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/surface_gauss/skt.sfc.mon.1981-2010.ltm.nc',engine='netcdf4').sel(\
                      time = months)
ds_pr_wtr_LTM = xr.open_dataset('https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/surface/pr_wtr.eatm.mon.1981-2010.ltm.nc',engine='netcdf4').sel(\
                      time = months)

## Read in combined reanalysis netcdf files from google drive. These only contain the extreme precipitation days


from netCDF4 import Dataset

combined_Uwind_250hPa = Dataset('/content/drive/My Drive/Project3/Combined/combined_Uwind_250hPa_1996to2019_ExtremePrecipDays.nc')
combined_Vwind_250hPa = Dataset('/content/drive/My Drive/Project3/Combined/combined_Vwind_250hPa_1996to2019_ExtremePrecipDays.nc')
combined_GeopHgt_500hPa = Dataset('/content/drive/My Drive/Project3/Combined/combined_GeopHgt_500hPa_1996to2019_ExtremePrecipDays.nc')
combined_Uwind_500hPa = Dataset('/content/drive/My Drive/Project3/Combined/combined_Uwind_500hPa_1996to2019_ExtremePrecipDays.nc')
combined_Vwind_500hPa = Dataset('/content/drive/My Drive/Project3/Combined/combined_Vwind_500hPa_1996to2019_ExtremePrecipDays.nc')
combined_Omega_500hPa = Dataset('/content/drive/My Drive/Project3/Combined/combined_Omega_500hPa_1996to2019_ExtremePrecipDays.nc')
combined_Uwind_850hPa = Dataset('/content/drive/My Drive/Project3/Combined/combined_Uwind_850hPa_1996to2019_ExtremePrecipDays.nc')
combined_Vwind_850hPa = Dataset('/content/drive/My Drive/Project3/Combined/combined_Vwind_850hPa_1996to2019_ExtremePrecipDays.nc')
combined_SpecHum_850hPa = Dataset('/content/drive/My Drive/Project3/Combined/combined_SpecHum_850hPa_1996to2019_ExtremePrecipDays.nc')
combined_AirTemp_850hPa = Dataset('/content/drive/My Drive/Project3/Combined/combined_AirTemp_850hPa_1996to2019_ExtremePrecipDays.nc')
combined_Uwind_sig995 = Dataset('/content/drive/My Drive/Project3/Combined/combined_Uwind_sig995_1996to2019_ExtremePrecipDays.nc')
combined_Vwind_sig995 = Dataset('/content/drive/My Drive/Project3/Combined/combined_Vwind_sig995_1996to2019_ExtremePrecipDays.nc')
combined_SkinTemp_Sfc = Dataset('/content/drive/My Drive/Project3/Combined/combined_SkinTemp_Sfc_1996to2019_ExtremePrecipDays.nc')
combined_PrecipWater = Dataset('/content/drive/My Drive/Project3/Combined/combined_PrecipWater_1996to2019_ExtremePrecipDays.nc')


#Data and files are then able to be plotted