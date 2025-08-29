--2. Use window functions
--Examples:
--	• Titanic → assign each passenger a seat number in age order
--	• Netflix → rank movies by release year
--	• Sales → calculate the cumulative sum of orders for each customer.

-- This is my database
USE MyTestBase;
GO

-- Assign each passenger a seat number in age order in the Titanic dataset
SELECT
	[Name]
	,ROW_NUMBER()
        OVER (
            ORDER BY [Age] ASC
        )
    AS [SeatNumber]
FROM
	[dbo].[Titanic]
ORDER BY
	[Name];

-- Rank movies by release year in the Netflix dataset
SELECT
	[title]
	,[release_year]
	,RANK()
        OVER (
            PARTITION BY [release_year]
            ORDER BY [title]
        )
    AS [RankByYear]
FROM
	[dbo].[Netflix_Movies_and_TV_Shows]
ORDER BY
	[release_year];

-- Calculate the cumulative sum of orders for each customer in the Superstore dataset
SELECT
	[Customer Name]
	,[Order Date]
	,CAST(
            SUM([Sales])
            OVER (
                PARTITION BY [Customer ID]
                ORDER BY [Order Date]
            )
    as decimal(20,2))
    AS [TotalSalesByCustomer]
FROM
	[dbo].[Superstore_Dataset]
ORDER BY
	[Customer Name];