
--Q1

SELECT count(*) FROM Shippers 
INNER JOIN ORDERS ON Shippers.ShipperID = Orders.ShipperID
WHERE ShipperName = "Speedy Express"
;
--Ans: 54

--Q2

WITH temp_table(EID, Freq)
AS(	
Select EmployeeID, Count(*) AS Frequency 
FROM Orders
Group By EmployeeID
ORDER BY Count(*) DESC
LIMIT 1
)
SELECT LastName From temp_table
INNER JOIN Employees ON temp_table.EID = Employees.EmployeeID;
--Ans: Peacock

--Q3
SELECT Products.ProductID, Products.ProductName, Country, SUM(OrderDetails.Quantity) AS Total_Q_Ordered 
FROM Orders 
JOIN Customers ON Customers.CustomerID = Orders.CustomerID
JOIN OrderDetails ON OrderDetails.OrderID = Orders.OrderID
JOIN Products ON Products.ProductID = OrderDetails.ProductID 
Where Customers.Country = "Germany"
GROUP BY Products.ProductID
ORDER BY SUM(OrderDetails.Quantity) DESC
LIMIT 1
;

--Ans: Boston Crab Meat 160
