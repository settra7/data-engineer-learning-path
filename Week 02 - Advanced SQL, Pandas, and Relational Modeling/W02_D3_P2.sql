-- Practice:
--  • Make a PIVOT: count the number of orders by month in a table.

-- My solution for SQL Server with Northwind database (I used the existing tables):
USE NORTHWND;
GO

SELECT
    CustomerID -- Customer Identifier
    ,ISNULL([January], 0) AS [January]
    ,ISNULL([February], 0) AS [February]
    ,ISNULL([March], 0) AS [March]
    ,ISNULL([April], 0) AS [April]
    ,ISNULL([May], 0) AS [May]
    ,ISNULL([June], 0) AS [June]
    ,ISNULL([July], 0) AS [July]
    ,ISNULL([August], 0) AS [August]
    ,ISNULL([September], 0) AS [September]
    ,ISNULL([October], 0) AS [October]
    ,ISNULL([November], 0) AS [November]
    ,ISNULL([December], 0) AS [December]
FROM (
    SELECT
        CustomerID
        ,FORMAT(OrderDate, 'MMMM', 'en-US') AS [Month] -- Month Name
        ,COUNT(OrderID) AS [OrdersCount] -- Number of Orders
    FROM
        [dbo].[Orders]
    GROUP BY
        CustomerID
        ,FORMAT(OrderDate, 'MMMM', 'en-US')
) AS SourceTable
PIVOT (
    SUM(OrdersCount) -- Sum of Orders
    FOR [Month] IN (
        [January], [February], [March],
        [April] ,[May] ,[June],
        [July] ,[August], [September],
        [October] ,[November], [December])
) AS PivotTable
ORDER BY
    CustomerID ASC -- Order by CustomerID