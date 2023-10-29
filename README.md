# Usage of Various file in analysis:
# 1 python file and excel sheet
 by the python file we are creating the graph for paddy and non paddy crops and then analysing it using observational method, in accordance to the definition of NDVI. NVDI chnages with change in vegetation,
 so on observing pattern for paddy crops we observe a specific pattern for paddy crops and also values for each season is approxiamted and taken mean to get a threshold for the padddy crops, once we get any crop NDVI betwee that range, we will classify it as paddy crops,
 else they all are non-paddy crops. 
 approximation is done using excel sheet. 
 for a paddy crop in telangana the avg value for each point have been specified in EXCEL SHEET which will be used. and then for any other crop we will download its csv and test if the pattern is followed by them, if followed they are paddy crops else they are non- paddy crops. 
 we are also using these graphs for stage identification of crops that is for the specific stages of crop cycle, we have approximated a mean for a region, and then we will check it by the same values. 
 we have saved all these values in excel sheet.
# 2 txt file 
in this repo we have 2 files which contains the code for google search engine script.  

# Q1 - how can we distinguish a paddy and a non-paddy crop 
for distinguishing between paddy and non paddy crop we will use NDVI and NDWI which are normalised difference vegetation index, normalised difference water index. 

# NDVI
NDVI stands for Normalized Difference Vegetation Index. It is a commonly used vegetation index in remote sensing and is calculated from satellite or aerial imagery. NDVI is used to quantify the amount of live vegetation in an area based on the reflectance of the Earth's surface at specific wavelengths of light. It is a dimensionless index that ranges from -1 to 1, with higher values indicating healthier, more dense vegetation.

NDVI is calculated using the following formula:

NDVI = (NIR - Red) / (NIR + Red)

Where:

NIR (Near-Infrared) is the reflectance in the near-infrared band (usually in the range of 0.7 to 1.3 micrometers).
Red is the reflectance in the red band (usually in the range of 0.6 to 0.7 micrometers).

# NDWI - 
NDWI stands for Normalized Difference Water Index. It is an index used in remote sensing to highlight the presence of water in an area. NDWI is particularly effective for identifying and mapping the extent of surface water bodies, such as rivers, lakes, and ponds, and can also be used for assessing changes in water content in vegetation.

The NDWI formula is calculated using the following equation:

NDWI = (NIR - SWIR) / (NIR + SWIR)
now, according to seasons of india, the sowing season is in june july and harvesting season is in october, november. This plays a very important role for identificaiton of paddy and non paddy crops, paddy crops are most of the time flooded so NDWI will be positive for the paddy crop region most of the time even after harvesting, but here comes the catch, for non paddy crops evn after october NDWI can go negative and we can differentiate between a paddy and non paddy crop by the same. 

by using the definition of NDVI and NDWI, we have done the crop identification and also the stage idenitfication, 
for identifying the fake paddy crops we will again use the both to determine the overall quality of the paddy crop and will give it a rating between 0 to 1, 1 is the best qaulity of the paddy and 0 is damaged paddy. NDVI values for fake paddy will  be lesser than original or high quality paddy crop.
# 3 for online procurment 
we will estimate the total yield of the paddy crop by estimating the areas falling in different regions.so we fill find the area of the paddy crop by finding area of colored region which represents the paddy crop field.