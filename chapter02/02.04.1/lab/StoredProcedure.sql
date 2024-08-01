# Description: Create a stored procedure that returns the total number of employees in the employees table.

DELIMITER $$
CREATE PROCEDURE total_employees()
BEGIN
    SELECT COUNT(*) AS total_employees FROM employees;
END $$
