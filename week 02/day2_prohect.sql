-- Practice:
--      • Take a table of orders.
--      • For each customer, number the orders by date.
--      • Find orders made on two consecutive days (LAG()).

-- My solution for SQL Server with Northwind database (I used the existing tables):
USE NORTHWND;
GO

SELECT
	c.CustomerID -- Customer Identifier
	,o.OrderID -- Order Identifier
	,FORMAT(o.OrderDate, 'yyyy/MM/dd') AS [OrderDate] -- Formatted Order Date
	,ROW_NUMBER() OVER (PARTITION BY c.CustomerID ORDER BY o.OrderDate) AS [RowNumPerCustomer] -- Order Number per Customer
	,CASE -- Check for Consecutive Orders
		WHEN
			DATEDIFF(day,
				o.OrderDate, -- Current Order Date
				LEAD(o.OrderDate) OVER (PARTITION BY c.CustomerID ORDER BY o.OrderDate)) = 1 -- Next Order Date
			OR 
			DATEDIFF(day,
				LAG(o.OrderDate) OVER (PARTITION BY c.CustomerID ORDER BY o.OrderDate), -- Previous Order Date
				o.OrderDate) = 1 -- Current Order Date
		THEN 'Yes' -- Consecutive Orders
		ELSE 'No' -- Not Consecutive Orders
	END AS [ConsecutiveOrders]
FROM
	[dbo].[Customers] c
	INNER JOIN [dbo].[Orders] o
	ON c.CustomerID = o.CustomerID
ORDER BY
	c.CustomerID -- Order by CustomerID