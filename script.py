import pandas as pd

df = pd.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv")
print(df.order_amount.describe())



