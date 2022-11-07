SELECT a.name AS 'Employee' FROM Employee AS a, Employee AS b 
WHERE a.ManagerId = b.ID AND a.Salary > b.Salary;
