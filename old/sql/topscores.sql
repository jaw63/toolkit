WITH TopScores AS (
  SELECT student_name, test_score, date, subject,
         ROW_NUMBER() OVER (PARTITION BY student_name ORDER BY test_score DESC) AS row_num
  FROM Scores
)
SELECT student_name, test_score, date, subject
FROM TopScores
WHERE row_num <= 3
ORDER BY student_name, test_score DESC;
