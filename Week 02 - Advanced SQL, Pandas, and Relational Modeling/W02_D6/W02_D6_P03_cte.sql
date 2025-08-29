--3. Use CTE (Common Table Expressions)
--Examples:
--	• Titanic → first select passengers over 30 in the CTE, and then calculate the average age from this set.
--	• Netflix → make a CTE with a filter of "only Movies", and then calculate the TOP-5 genres inside it.
--	• Sales → make a CTE with revenue calculation by category, and then select only those with > 10000.

-- This is my database
USE MyTestBase;
GO

-- First select passengers over 30 in the CTE, and then average age from this set in the Titanic dataset
WITH 
	PassengersOver30 AS (
		SELECT
			*
		FROM
			[dbo].[Titanic]
		WHERE
			Age > 30
)
SELECT
	CAST(AVG(Age) AS int) AS [AvgAge]
FROM
	PassengersOver30;

-- Make a CTE with a filter of "only Movies", and then calculate the TOP-5 genres inside it in the Netflix dataset
WITH
	[MoviesOnly] AS (
		SELECT
			*
		FROM
			[dbo].[Netflix_Movies_and_TV_Shows]
		WHERE
			[Type] = 'Movie'
	)
SELECT TOP 5
	[listed_in]
	,COUNT([show_id]) AS [ShowsCount]
FROM
	[MoviesOnly]
GROUP BY
	[listed_in]
ORDER BY
	[ShowsCount] DESC;

-- Make a CTE with revenue calculation by category, and then select only those with > 10000 in the Superstore dataset
WITH
	RevenueByCategory AS (
		SELECT
			[Category]
			,CAST(SUM([Sales]) AS decimal(20,2)) AS [SalesOverall]
		FROM
			[dbo].[Superstore_Dataset]
		GROUP BY
			[Category]
)
SELECT
	*
FROM
	RevenueByCategory
WHERE
	[SalesOverall] > 10000
ORDER BY
	[Category];