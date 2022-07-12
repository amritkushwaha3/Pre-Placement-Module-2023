/* Creating a Table*/
CREATE TABLE employee
(EmpId int, Name varchar(100), City varchar(50), DeptId int);
DESCRIBE employee;

/*Inserting values in table employee*/
INSERT INTO employee VALUES(1,'Ajay Singh','Mayur Vihar',3),(2,'Aditya Singh','Noida',2),(3,'Abhay Singh','Mayur Vihar',4),(4,'Alok Kumar','Gopal Vihar',3);

/*Select query in SQL*/
SELECT * FROM employee;
SELECT Name FROM employee WHERE City='Mayur Vihar';

/*Update query in SQL*/
UPDATE employee SET DeptId=1 WHERE EmpId=3;

/*Delete query in SQL*/
DELETE FROM employee WHERE EmpId=2;

/*Creating another table salary*/
CREATE TABLE salary(DeptId int, Salary int);


/*Inserting values in table salary*/
INSERT INTO salary VALUES(1,25000),(2,28000),(3,30000);

SELECT * FROM salary;

/*Using Join query to join the two tables employee and salary*/
SELECT employee.Name,salary.Salary
FROM employee
INNER JOIN salary
ON employee.DeptId=salary.DeptId;