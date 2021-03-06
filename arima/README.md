ARIMA POC
==============================

Summary
==============================
This Analysis is aimed to get comfortable with ARIMA in Python.
Most of the variables will be ignored in favor of the Timestamp and the
Total Orders.

Dataset
==============================
This project will use the dataset available [here](https://archive.ics.uci.edu/ml/datasets/Air+Quality)

This dataset is semi-colon delimited and uses European , decimal point.  It has has
* 9472 observations
* 1 independent variables
* 14 dependent variable
* Uses -200 for missing values

Columns
------------------------------
0 Date	(DD/MM/YYYY) 
1 Time	(HH.MM.SS) 
2 True hourly averaged concentration CO in mg/m^3 (reference analyzer) 
3 PT08.S1 (tin oxide) hourly averaged sensor response (nominally CO targeted)	
4 True hourly averaged overall Non Metanic HydroCarbons concentration in microg/m^3 (reference analyzer) 
5 True hourly averaged Benzene concentration in microg/m^3 (reference analyzer) 
6 PT08.S2 (titania) hourly averaged sensor response (nominally NMHC targeted)	
7 True hourly averaged NOx concentration in ppb (reference analyzer) 
8 PT08.S3 (tungsten oxide) hourly averaged sensor response (nominally NOx targeted) 
9 True hourly averaged NO2 concentration in microg/m^3 (reference analyzer)	
10 PT08.S4 (tungsten oxide) hourly averaged sensor response (nominally NO2 targeted)	
11 PT08.S5 (indium oxide) hourly averaged sensor response (nominally O3 targeted) 
12 Temperature in Â°C	
13 Relative Humidity (%) 
14 AH Absolute Humidity 


Analysis Performed
==============================
This notebook does a simple timeseries analysis of a single time series.  
It's not production level work, but just a look into basic analysis and modeling using 
`statsmodels`.

Future Work
==============================
There are other time series modules worth looking into including,
1. [PyFlux](http://www.pyflux.com/)
2. [Prophet](https://facebook.github.io/prophet/)
3. [tsfresh](https://github.com/blue-yonder/tsfresh)