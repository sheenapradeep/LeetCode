SELECT a.id 
FROM Weather a 
JOIN Weather b ON a.recordDate = DATEADD(Day,1,b.recordDate) 
WHERE a.temperature > b.temperature;
