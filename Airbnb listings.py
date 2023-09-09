# Importing some important libraries which will help us in analyzing the dataset
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 

# Read the csv file 
airbnb = pd.read_csv("listings.csv")

# Check the content of the DataFrame
# print(airbnb.head())

# Show some information about the DataFrame
# print(airbnb.shape)
# print(airbnb.info())



# Data Wrangling (Cleaning & Manipulation)

# Drop unnecessary features 
airbnb = airbnb.loc[: , ["name" , "host_name" , "host_neighbourhood"  , "latitude" ,"longitude" , "room_type" , "price" , 'minimum_nights' , 'maximum_nights' , "availability_365" , "number_of_reviews" , "review_scores_rating" , "reviews_per_month"] ]

# some info about the selected features 
print(airbnb.head(20))
print(airbnb.shape)

# Descriptive statistics
numeric_features = ["price", "minimum_nights", "maximum_nights", "availability_365", "number_of_reviews", "review_scores_rating", "reviews_per_month"]
categorical_features = ["room_type"]

# Calculate descriptive statistics for numeric features
numeric_stats = airbnb[numeric_features].describe()

# Count unique values for categorical features
categorical_counts = airbnb[categorical_features].nunique()

# Correlation analysis
correlation_matrix = airbnb.corr()

# Are There any missing / duplicated values 
airbnb.isna().sum()
airbnb.duplicated().sum()

# Drop Duplicates of the DataFrame
airbnb = airbnb.drop_duplicates()


# Data Analysis & Visulaization (EDA & Statistical Analysis)
# Converting the format of the price
print(airbnb["price"].dtype)  
airbnb['price'] = airbnb['price'].str.replace('$' , '').str.replace(',','').astype(float)

# what is the average of the prices ?
print(airbnb["price"].mean())

# # what are the highest and the lowest prices ? 
print(airbnb["price"].max())
print(airbnb["price"].min()) 


# The naxt block of code will recommend the best accomdation for 4 days in terms of price , review and availability for the middle-income category and the low-income category

# The mean for minimum number of nights 
print(airbnb['minimum_nights'].mean())

# Adding a new column
airbnb['booking_availability'] = np.where(airbnb["availability_365"] >= 4 , "available for 4 days" , "not available") 

available_4_days = airbnb[airbnb["booking_availability"] == "available for 4 days"]

# The average price for 4 days accomdation
prices_avail_4_days = available_4_days['price'].mean()
print(prices_avail_4_days)
# The minimum price for 4 days accomdation
min_price_avail_4_days = available_4_days['price'].min()
print(min_price_avail_4_days)


# Correlation analysis
correlation_matrix = airbnb.corr()
# Visualize the correlation matrix using a heatmap
plt.figure(figsize = (10 , 8))
sns.heatmap(correlation_matrix , annot = True , cmap = "coolwarm")
plt.title(correlation_matrix)
plt.show()

# Decisions making 
# Determine most popular room types based on number of listings
popular_room_types = airbnb["room_type"].value_counts().idxmax()
print("Most Popular Room Type:", popular_room_types)

# Identify neighborhoods with highest average review scores
top_neighborhoods = airbnb.groupby("host_neighbourhood")["review_scores_rating"].mean().nlargest(5)
print("Top Neighborhoods by Average Review Scores:")
print(top_neighborhoods)


# Data Visualizations
# Scatter plot of latitude and longitude
plt.figure(figsize = (8,6))
plt.scatter(airbnb["longitude"] , airbnb['latitude'])
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Geographical Distribution Of Listings")
plt.show()

# Histogram plot of price 
plt.figure(figsize = (8,6))
plt.hist(airbnb['price'] , bins = 20)
plt.xlabel("Prices")
plt.ylabel("Frequancies of prices")
plt.title("Distribution of prices")
plt.show()

# Bar plot of room type 
count_types = airbnb["room_type"].value_counts()
plt.figure(figsize = (8,6))
plt.bar(count_types.index , count_types.values)
plt.xlabel("Room Type")
plt.ylabel("Count")
plt.title("Number of Listings by Room Type")
plt.show()





#                                          # Bar chart # 
                                       
# def approxiamation(row) :
#     if row != "NaN" :
#         return round(row)
# # Filling the NaN values of the column with the mean of the rest of values -----> 'review_scores_rating'
# airbnb['review_scores_rating'].fillna(airbnb['review_scores_rating'].mean()  , inplace=True)   
# airbnb['review_scores_rating'] = airbnb['review_scores_rating'].apply(approxiamation) 
# # print(airbnb['review_scores_rating'])

# # Count the values of this features 
# count = airbnb['review_scores_rating'].value_counts() # print(count)
# review_count_df = pd.DataFrame(count)
# plt.bar(review_count_df.T.columns , count , edgecolor="black")
# plt.xlabel("Review_Scores")
# plt.ylabel("Counts of Review_scores")
# plt.grid()
# plt.show()

#                                                      # Scatter Plot
# plt.figure(figsize=(7,7))
# plt.scatter(airbnb['availability_365'] ,airbnb['price'] , alpha=0.02)
# plt.title("The Availability vs The Price")
# plt.xlabel("The Availability")
# plt.ylabel("The price")
# plt.legend()
# plt.grid()
# plt.show()

# from the preceding scatter plot we can say that the relationship between the availability and the price is a linear relationship 
# the prices of bookings do not affect by the availability  


