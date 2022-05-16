# Shopify-2022-Data Science-Challenge

## Question 1: 

Given some sample data, write a program to answer the following: click here to access the required data set

On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 

1. Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 
2. What metric would you report for this dataset?
3. What is its value?

## Answer
1. There are a couple things that are likely going wrong with the calculation. Firstly, the calculation does not consider the quantity of shoes ordered in an order. It possibly just sums up the order amount and divides it by the total count of orders made in 30 days, instead, the summation of order amount should be divided by the summation of total items ordered. Secondly, the calculation includes the outliers which should be omitted out because the outliers do not represent the correct data and it therefor yeilds the wrong AOV.

2. The correct AOV should be caluculated by firstly cleaning up the data by removing all the outliers (extremely expensive shoes). An average shoe price was determined for each order by dividing the order_amount by total_items for each order. Then all the orders which had an average shoes price of more than a $1000 were removed from the dataset. $1000 is still extremely expensive for a shoe but I was a bit lenient. Lastly, after filtering the dataset, the average shoe price was summed up and divided by the total amount of orders.

3. The AOV = $152.48
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




