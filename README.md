# Shopify-2022-Data Science-Challenge

## Question 1: 

Given some sample data, write a program to answer the following: click here to access the required data set

On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 

1. Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 
2. What metric would you report for this dataset?
3. What is its value?

## Answer
1. One of the main things that seems wrong is not filtering the data. Store 78 sells a pair of shoes for more than $25000. This is a clear case of it being an outlier that skews up the results. Store 78 causes the mean to be high. The correct AOV should be caluculated by firstly cleaning up the data by removing the outliers (store 78). After filtering the data we should use the median as the reference point for the AOV because it is more indicative of the actual AOV. The median is relatively closer to the values at the 25th and the 75th percentile. 

2. The median
3. The AOV = $284
## Question 2:

For this question you’ll need to use SQL. Follow this link to access the data set required for the challenge. Please use queries to answer the following questions. Paste your queries along with your final numerical answers below.

1. How many orders were shipped by Speedy Express in total?
2. What is the last name of the employee with the most orders?
3. What product was ordered the most by customers in Germany?

## Answer

1. 54
2. Peacock
3. Boston Crab Meat

The querries can be found here: [q2.sql](https://github.com/AhmadSiddiqi158/Shopify-2022-Data-Science-Challenge/blob/main/q2.sql)




