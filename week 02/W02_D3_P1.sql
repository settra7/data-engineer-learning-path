-- Practice:
--	• Use CTE to find customers with an average order value > 100.

-- My solution for SQL Server with Northwind database (I used the existing tables):
USE NORTHWND;
GO

WITH OrdersWithSums AS ( -- CTE to calculate order sums
	SELECT
		o.CustomerID
		,o.OrderID
		,SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) AS [OrderSum] -- Total Order Value
	FROM
		[dbo].[Orders] o
		INNER JOIN [dbo].[Order Details] od
		ON o.OrderID = od.OrderID
	GROUP BY
		o.CustomerID
		,o.OrderID
	)
SELECT -- Final selection of customers with average order value
	CustomerID
	,CAST(AVG([OrderSum]) AS decimal(20,2)) AS [AvgOrderSum] -- Average Order Value
	,COUNT(OrderID) AS [OrderCount] -- Number of Orders
FROM
	OrdersWithSums
GROUP BY
	CustomerID
HAVING
	AVG([OrderSum]) > 100 -- Filter for Average Order Value
ORDER BY
	AvgOrderSum DESC -- Order by Average Order Value