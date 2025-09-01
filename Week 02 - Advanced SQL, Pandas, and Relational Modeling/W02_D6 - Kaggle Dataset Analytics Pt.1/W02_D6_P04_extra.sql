--4. Extra (if you have time)
--	• Use LAG()/LEAD() - for example, compare the release date of the current movie with the next one.
--	• Use nested CTEs (one on top of the other).

-- This is my database
USE MyTestBase;
GO

-- Using the Netflix dataset, create a CTE that filters only Movies,
-- and then use a window function to calculate the difference in days between the
-- date_added of each movie and the next movie in the list when ordered by date_added.
WITH
	MoviesOnly AS (
		SELECT
			*
		FROM
			[dbo].[Netflix_Movies_and_TV_Shows]
		WHERE
			[Type] = 'Movie' -- Filter only Movies
	)
	,
	DateAddedDiffs AS (
	SELECT
		[title]
		,[date_added]
		,(
			DATEDIFF(
				day
				,[date_added]
				,(LEAD([date_added]) OVER ( -- Get the date_added of the next movie
					ORDER BY [date_added] ASC
					)
				)
			)
		)
		AS [DaysDiff]
	FROM
		MoviesOnly
	)
SELECT
	*
FROM
	DateAddedDiffs