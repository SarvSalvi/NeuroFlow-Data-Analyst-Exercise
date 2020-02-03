WITH FirstMonth (user_id, ExerciseMonth)
AS (
SELECT user_id, MIN(EXTRACT(MONTH FROM exercise_completion_date)) AS ExerciseMonth 
FROM exercises
GROUP BY user_id
)
SELECT EXTRACT(MONTH FROM created_at) AS CohortMonth, EXTRACT(YEAR FROM created_at) AS CohortYear,  100*(COUNT(CASE WHEN ExerciseMonth = EXTRACT(Month FROM created_at) THEN 1 END)/Count(1)) as Percent
FROM FirstMonth
RIGHT JOIN users u 
ON FirstMonth.user_id = u.user_id
GROUP BY CohortYear, CohortMonth

