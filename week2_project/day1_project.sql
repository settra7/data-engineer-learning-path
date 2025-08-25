-- Practice:
--      • Take a database (PostgreSQL or SQL Server).
--      • Create tables Customers, Orders, Products.
-- Try queries:
--      • Find all customers with orders > 3.
--      • Calculate the total amount of orders for each customer.

-- My solution for SQL Server with Northwind database (I used the existing tables):
USE NORTHWND;
GO

SELECT
	c.CustomerID, -- Customer Identifier
	COUNT(o.OrderID) AS [CountOfOrders], -- Number of Orders
	CAST(SUM(od.[UnitPrice] * od.[Quantity] * (1 - [Discount])) AS decimal(20,2)) AS [TotalSumOrdered] -- Total Amount of Orders
FROM
	[dbo].[Customers] c
	INNER JOIN [dbo].[Orders] o
	ON c.CustomerID = o.CustomerID
	INNER JOIN [dbo].[Order Details] od
	ON o.OrderID = od.OrderID
GROUP BY
	c.CustomerID -- Grouping by CustomerID
HAVING
	COUNT(o.OrderID) > 3 -- Customers with more than 3 orders
ORDER BY
	COUNT(o.OrderID) DESC -- Order by number of orders in descending order