create database ustglobal;
use ustglobal;

-- 1.Write an SQL query to display the second highest salary from an Employees table.

SELECT MAX(salary) AS second_highest_salary
FROM Employees
WHERE salary < (SELECT MAX(salary) FROM Employees);


-- 2.Given a table Orders(order_id, customer_id, order_date, amount), write a query to find the total order amount per customer, but display only customers whose total exceeds 50,000.
SELECT customer_id, SUM(amount) AS total_amount
FROM Orders
GROUP BY customer_id
HAVING SUM(amount) > 50000;



-- 3.Write an SQL query to find the number of employees in each department, excluding departments with fewer than 3 employees.
SELECT department_id, COUNT(*) AS emp_count
FROM Employees
GROUP BY department_id
HAVING COUNT(*) >= 3;



-- 4.Given tables Students(student_id, name) and Marks(student_id, subject, marks), write a query to find students who have scored more than 80 in at least two subjects.
SELECT student_id
FROM Marks
WHERE marks > 80
GROUP BY student_id
HAVING COUNT(*) >= 2;



-- 5.Write an SQL query to retrieve the names of employees who earn more than the average salary of their department.
SELECT e.employee_id, e.name, e.salary, e.department_id
FROM Employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM Employees
    WHERE department_id = e.department_id
);



-- 6.Given a table Sales(sale_id, product_id, sale_date, quantity), write a query to find the total quantity sold for each product in the year 2024.
SELECT product_id, SUM(quantity) AS total_quantity
FROM Sales
WHERE YEAR(sale_date) = 2024
GROUP BY product_id;



-- 7.Write an SQL query to display the top 3 highest-paid employees from each department.
SELECT employee_id, name, department_id, salary
FROM (
    SELECT e.*,
           DENSE_RANK() OVER (
               PARTITION BY department_id
               ORDER BY salary DESC
           ) AS rnk
    FROM Employees e
) t
WHERE rnk <= 3;



-- 8.Given a table Customers(customer_id, customer_name, city), write a query to find cities that have more than 5 customers.
SELECT city, COUNT(*) AS customer_count
FROM Customers
GROUP BY city
HAVING COUNT(*) > 5;



-- 9.Write an SQL query to find employees who do not have any records in the Attendance table.
SELECT e.employee_id, e.name
FROM Employees e
LEFT JOIN Attendance a
ON e.employee_id = a.employee_id
WHERE a.employee_id IS NULL;



-- 10.Given a table Employees(employee_id, name, manager_id), write an SQL query to display each employee’s name along with their manager’s name.
SELECT e.name AS employee_name,
       m.name AS manager_name
FROM Employees e
LEFT JOIN Employees m
ON e.manager_id = m.employee_id;






 