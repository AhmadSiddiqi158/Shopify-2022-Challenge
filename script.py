import pandas as pd

df = pd.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv")
rows = df.shape[0] #num of rows
total_order_amount = df["order_amount"].sum()
print("Incorrect AOV: $" + str(total_order_amount/rows))

#getting the average shoe price per order
for row in df:
    df["Average_shoe_price"] = df["order_amount"]/df["total_items"]

df = df.sort_values(["Average_shoe_price"], ascending=[False]) #ordering the data in a descending order of average shoe price (ASP)
df = df[df.Average_shoe_price < 1000] #assuming an Average shoe price costs less than $1000 ($1000 too is on the high end side). 
#This way we filter out all the outliers (extremely expensive shoes) that skew up the data
total_average_order = df["Average_shoe_price"].sum() # summing up all the ASP after filtering
newRows = df.shape[0] #getting the new amount of data rows after truncating the outliers
AOV = total_average_order/newRows #calculating the AOV
print("Correct AOV: $" + str(AOV))




