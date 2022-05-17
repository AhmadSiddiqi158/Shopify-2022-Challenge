import pandas as pd
pd.set_option("display.max_rows", None)
df = pd.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv")
rows = df.shape[0] #num of rows
total_order_amount = df["order_amount"].sum()
print("Incorrect AOV: $" + str(total_order_amount/rows))

#getting the average shoe price per order
for row in df:
    df["Average_shoe_price"] = df["order_amount"]/df["total_items"]

df = df.sort_values(["Average_shoe_price"], ascending=[False]) #ordering the data in a descending order of average shoe price (ASP)
df = df[df.shop_id != 78] #filtering out the shop_id 78 

print(df.order_amount.describe())



