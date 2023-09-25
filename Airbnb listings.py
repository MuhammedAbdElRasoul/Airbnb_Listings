# Importing some important libraries which will help us in analyzing the dataset
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 

# Read the csv file 
airbnb = pd.read_csv("listings.csv")

# Check the content of the DataFrame
print(airbnb.head())

# Show some information about the DataFrame
print(airbnb.shape)



# Data Wrangling (Cleaning & Manipulation)

# Drop unnecessary features 
airbnb = airbnb.loc[: , ["name" , "host_name" , "host_neighbourhood"  , "latitude" ,"longitude" , "room_type" , "price" , 'minimum_nights' , 'maximum_nights' , "availability_365" , "number_of_reviews" , "review_scores_rating" , "reviews_per_month"] ]

# Save the CSV file 
airbnb.to_csv("airbnb.csv")

# some info about the selected features 
print(airbnb.head(20))
print(airbnb.shape)

# Descriptive statistics
numerical_features = ["price", "minimum_nights", "maximum_nights", "availability_365", "number_of_reviews", "review_scores_rating", "reviews_per_month"]
categorical_features = ["room_type"]

# Calculate descriptive statistics for numeric features
numerical_stats = airbnb[numerical_features].describe()
print(numerical_stats)

# Count unique values for categorical features
categorical_counts = airbnb[categorical_features].nunique()

# Are There any missing / duplicated values 
airbnb.isna().sum()
airbnb.duplicated().sum()

# # Drop Duplicates of the DataFrame
airbnb = airbnb.drop_duplicates()


# Data Analysis & Visulaization (EDA & Statistical Analysis)

# Converting the format of the price
print(airbnb["price"].dtype)  
airbnb['price'] = airbnb['price'].str.replace('$' , '').str.replace(',','').astype(float)


# what is the average , highest and the lowest of the prices ?
print(airbnb["price"].mean())
print(airbnb["price"].max())
print(airbnb["price"].min()) 


# Grouping the dataset by categorical columns like room_type and calculate aggregate statistics such as average price for each group 
average_price_by_property_type = airbnb.groupby("room_type")["price"].mean()


# Calculate correlation coefficient between price and review_scores_rating
correlation = airbnb['price'].corr(airbnb['review_scores_rating'])
# Print correlation coefficient
print("Correlation between price and review scores:", correlation)

# what is the average of the availability ?
print(airbnb["availability_365"].mean())

# Grouping the dataset by categorical columns like room_type and calculate aggregate statistics such as average price for each group 
average_avl_by_property_type = airbnb.groupby("room_type")["availability_365"].mean().sort_values()

# Determine most popular room types based on number of listings
popular_room_types = airbnb["room_type"].value_counts().idxmax()
print("Most Popular Room Type:", popular_room_types)


# Identify neighborhoods with highest average review scores
top_neighborhoods = airbnb.groupby("host_neighbourhood")["review_scores_rating"].mean().nlargest(5)
print("Top Neighborhoods by Average Review Scores:")
print(top_neighborhoods)




                                                  # Insights #

# 1 - The most frequent room type is (Entire room/apt) and the second one is (private room)
# 2 - The prices mean need to book per night equals 255$ , the minimum price for a night equals 18$ and the maximum price equals 27857$ per night.  
# 3 - The prices mean of  Entire room/apt is the highest one 278$ and the lowest one is  Shared room 144$.
# 4 - There is no correlation between prices and review ratings, not all the highest price hotels have a good review rating and vice verse.
# 5 - The average of days in the year available for guests to book equals 83 day. 
# 6 - The highest room_type available in year to book is (hotel room) its mean = 186 day and the lowest one is (Entire home/apt) its mean = 66 day.
# 7 - I noticed that Entire room/apt is the most room type occupied throughout the year. 
# 8 - The most 5 rating host neighbourhood are Brockley, Corvin-Negyed, Józsefváros - District VIII.Merkaz HaIr, Woodley Park and Slotermeer-Zuidwest, their rating = 5             




 # Data Visualizations

# Correlation analysis
correlation_matrix = airbnb.corr()
# Visualize the correlation matrix using a heatmap
plt.figure(figsize = (10 , 8))
sns.heatmap(correlation_matrix , annot = True , cmap = "coolwarm")
plt.show()

# Insight: The correlation matrix helps us to know that there are no correlations between features 


# Example 1: Price Distribution (Histogram)
plt.hist(airbnb['price'])
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Price Distribution')
plt.show()

# Insight: The majority of listings fall within a certain price range (0,2500), which can inform pricing strategies and competitive analysis.


# Bar plot of room type 
count_types = airbnb["room_type"].value_counts()
plt.figure(figsize = (8,6))
plt.bar(count_types.index , count_types.values)
plt.xlabel("Room Type")
plt.ylabel("Count")
plt.title("Number of Listings by Room Type")
plt.show()

# Insight: The most popular room type is Entire room/apt then private room, and the least popular is shared room


# Scatter plot of latitude and longitude
plt.figure(figsize = (8,6))
plt.scatter(airbnb["longitude"] , airbnb['latitude'] , alpha=0.02)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Geographical Distribution Of Listings")
plt.show()

# Benefit: This plot visualizes the geographical distribution of Airbnb listings.
# Insights: The majority of points in the scatter plot of longitude and latitude fall in a specific area the range of this area for longitude is from 4.85 to 4.93 and latitude from 52.34 to 52.39


# Scatter plot of price and availability 
plt.figure(figsize=(7,7))
plt.scatter(airbnb['availability_365'] ,airbnb['price'] , alpha=0.02)
plt.title("The Availability vs The Price")
plt.xlabel("The Availability")
plt.ylabel("The price")
plt.legend()
plt.grid()
plt.show()

# Insight: This scatter plot tells us that is no correlation between the price and the availability. This means that the availabilty of listings is static even if the price is increased or not.

