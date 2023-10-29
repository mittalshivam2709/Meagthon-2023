# by this file we are creating the graph for paddy and non paddy crops and then analysing it using observational method, in accordance to the definition of NDVI. NVDI chnages with change in vegetation,
# so on observing pattern for paddy crops we observe a specific pattern for paddy crops and also values for each season is approxiamted and taken mean to get a threshold for the padddy crops, once we get any crop NDVI betwee that range, we will classify it as paddy crops,
# else they all are non-paddy crops. 
# approximation is done using excel sheet. 
# for a paddy crop in telangana the avg value for each point have been specified in EXCEL SHEET which will be used. and then for any other crop we will download its csv and test if the pattern is followed by them, if followed they are paddy crops else they are non- paddy crops. 
# we are also using these graphs for stage identification of crops that is for the specific stages of crop cycle, we have approximated a mean for a region, and then we will check it by the same values. 
# we have saved all these values in excel sheet. 
 
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file with the specified format
data = pd.read_csv('1.csv', header=None, names=['Date', 'Value'], parse_dates=['Date'], date_parser=lambda x: pd.to_datetime(x, format='%b %d, %Y'))

# Filter data for a 5-month period (adjust start and end dates accordingly)
start_date = pd.to_datetime('2023-01-01')
end_date = pd.to_datetime('2023-05-31')
filtered_data = data

# Plot the time series data
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['Date'], filtered_data['Value'], label='Value')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Data for 5 Months')
plt.legend()
plt.grid()
plt.show()
