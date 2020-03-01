##  Scooters in Austin Data Analysis 

This Repository demonstrates serving a Flask Web App for City of Austin's Open Data about Shared Mobility 311 Complaints and the Shared Mobility API.
The Web app was deployed with Heroku. 

Submitted by: Sheetal Bongale 

Find the deployed web application [HERE.](https://atx-sharedmobility.herokuapp.com/)

Find the data analysis repository [HERE.](https://github.com/sheetalbongale/Scooters-In-Austin-Data-Analysis)


### Data Set:
---
* City of Austin 311 OpenData: https://data.austintexas.gov/City-Government/311-Unified-Data-Test-Site-2019/i26j-ai4z

`API Endpoint: https://data.austintexas.gov/resource/i26j-ai4z.json`
    
* Austin Shared Mobility API: https://data.austintexas.gov/Transportation-and-Mobility/Shared-Micromobility-Vehicle-Trips/7d8e-dm7r

`API Endpoint: https://data.austintexas.gov/resource/7d8e-dm7r.json`

### Notebooks:
---
- [311_data_wrangling.ipynb](https://github.com/sheetalbongale/Scooters_In_Austin_Data_Analysis/blob/master/notebooks/311_complaints_data_analysis/311_data_wrangling.ipynb): Data munging and generates clean data CSV file for the 311 Complaints API Data. 
- [311_data_story.ipynb](https://github.com/sheetalbongale/Scooters_In_Austin_Data_Analysis/blob/master/notebooks/311_complaints_data_analysis/311_data_story.ipynb): Data Visualization for 311 data.
- [shared_mobility_data_wrangling.ipynb](https://github.com/sheetalbongale/Scooters_In_Austin_Data_Analysis/blob/master/notebooks/shared_mobility_data_analysis/shared_mobility_data_wrangling.ipynb): Data munging and generates clean data CSV file for the Shared Mobility API Data. Also contains script to merge zipcodes to census tracts. The final merged CSV file is what we use for further analysis and visualization.
- [shared_mobility_data_story.ipynb](https://github.com/sheetalbongale/Scooters_In_Austin_Data_Analysis/blob/master/notebooks/shared_mobility_data_analysis/shared_mobility_data_story.ipynb): Data Visualization for shared mobility showing deep insights about the datasets.