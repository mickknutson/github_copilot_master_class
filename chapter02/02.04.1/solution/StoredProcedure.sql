# Description: Create a stored procedure that returns the total number of employees in the employees table.

DELIMITER $$
CREATE PROCEDURE GetEmployeeCount()
BEGIN
    SELECT COUNT(*) AS 'Total Employees' FROM employees;
END $$
DELIMITER ;
