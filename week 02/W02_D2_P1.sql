-- Practice:
--      • Take a table of orders.
--      • For each customer, number the orders by date.
--      • Find orders made on two consecutive days (LAG()).

-- My solution for SQL Server with Northwind database (I used the existing tables):
USE NORTHWND;
GO

SELECT
	CustomerID -- Customer Identifier
	,OrderID -- Order Identifier
	,FORMAT(OrderDate, 'yyyy/MM/dd') AS [OrderDate] -- Formatted Order Date
	,ROW_NUMBER() OVER (PARTITION BY CustomerID ORDER BY OrderDate) AS [RowNumPerCustomer] -- Order Number per Customer
	,CASE -- Check for Consecutive Orders
		WHEN
			DATEDIFF(day,
				OrderDate, -- Current Order Date
				LEAD(OrderDate) OVER (PARTITION BY CustomerID ORDER BY OrderDate)) = 1 -- Next Order Date
			OR 
			DATEDIFF(day,
				LAG(OrderDate) OVER (PARTITION BY CustomerID ORDER BY OrderDate), -- Previous Order Date
				OrderDate) = 1 -- Current Order Date
		THEN 'Yes' -- Consecutive Orders
		ELSE 'No' -- Not Consecutive Orders
	END AS [ConsecutiveOrders]
FROM
	[dbo].[Orders]
ORDER BY
	CustomerID -- Order by CustomerID