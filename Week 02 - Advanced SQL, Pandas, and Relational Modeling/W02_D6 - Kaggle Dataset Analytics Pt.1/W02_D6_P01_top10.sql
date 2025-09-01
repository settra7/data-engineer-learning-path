--1.TOP-10 by metric
--Examples:
--	• Titanic → TOP-10 oldest passengers.
--	• Netflix → TOP-10 countries with the largest number of films.
--	• Sales → TOP-10 products by total revenue.

-- This is my database
USE MyTestBase;
GO

--- TOP-10 oldest passengers in the Titanic dataset
SELECT TOP 10
	[Name],
	[Age]
FROM
	[dbo].[Titanic]
ORDER BY
	Age DESC;

--- TOP-10 countries with the largest number of films in the Netflix dataset
SELECT
	[country]
	,COUNT(show_id) AS [ShowsCount]
FROM
	[dbo].[Netflix_Movies_and_TV_Shows]
WHERE
	[country] IS NOT NULL
GROUP BY
	[country]
ORDER BY
	COUNT(show_id) DESC;

--- TOP-10 products by total revenue in the Superstore dataset
SELECT TOP 10
	[Product Name]
	,SUM([Sales]) AS [TotalSales]
FROM
	[dbo].[Superstore_Dataset]
GROUP BY
	[Product Name]
ORDER BY
	[TotalSales] DESC;