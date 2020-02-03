SELECT organization_id, organization_name, AVG(score) AS Average_Score
FROM Phq9 s
LEFT JOIN providors p
ON p.providor_id = s.providor_id
GROUP BY organization_id, organization_name
ORDER BY Average_Score DESC
LIMIT 5
