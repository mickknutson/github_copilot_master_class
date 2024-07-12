# Description: Create a stored procedure that returns the total number of employees in the employees table.

CREATE PROCEDURE GetEmployeeCount()
BEGIN
    SELECT COUNT(*) AS 'Total Employees' FROM employees;
END;
