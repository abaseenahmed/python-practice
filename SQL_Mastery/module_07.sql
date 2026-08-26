-- ================================= Module 07: Window Functions =============================== --
-- TABLE 01 FOR THIS MODULE
SELECT * FROM employees;

-- TABLE 02 FOR THIS MODULE
SELECT * FROM performance;

-- Group By Query Before Window Functions
SELECT department, AVG(salary)
FROM employees
GROUP BY department;


-- Calculate the average across the entire result set while keeping every row.
SELECT
    employee_name,
    salary,
    AVG(salary) OVER () AS company_avg_salary
FROM employees;

-- Calculate the average separately for each department, but keep every employee row.
SELECT
    employee_name,
    department,
    salary,
    AVG(salary) OVER (
        PARTITION BY department
    ) AS department_avg_salary
FROM employees;

-- 1 → highest salary 2 → second highest 3 → third highest
SELECT
    employee_name,
    department,
    salary,
    ROW_NUMBER() OVER (
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;

-- Rank employees by salary within their department.
SELECT
    employee_name,
    department,
    salary,
    RANK() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS department_salary_rank
FROM employees;

-- LAG() lets you access a previous row.
SELECT
    employee_name,
    department,
    salary,
    revenue,
    LAG(revenue) OVER (
        ORDER BY revenue DESC
    ) AS prev_revenue
FROM employees;

-- LEAD() is the opposite of LAG()
SELECT
    employee_name,
    department,
    salary,
    revenue,
    LEAD(revenue) OVER (
        ORDER BY revenue DESC
    ) AS next_revenue
FROM employees;

-- Task 01: Company Average
SELECT 
    employee_name,
    salary,
    -- AVG(salary) AS company_avg_salary
    AVG(salary) over () AS company_avg_salary
FROM employees;

-- Task 02: Department Average
SELECT
    employee_name,
    department,
    salary,
    AVG(salary) over (
        PARTITION BY department
    ) AS avg_department_salary
FROM employees;

-- Task 03: Salary Difference
SELECT
    employee_name,
    salary,
    AVG(salary) OVER () AS company_avg_salary,
    salary - AVG(salary) OVER () AS salary_difference
FROM employees;

-- Task 04: Global Salary Ranking
SELECT
    employee_name,
    salary,
    department,
    RANK() OVER (
        ORDER BY salary
    ) AS salary_rank
FROM employees;

-- Task 05: Department Salary Ranking
SELECT
    employee_name,
    department,
    salary,
    RANK() OVER (
        PARTITION BY department
        ORDER BY salary
    ) AS department_rank
FROM employees;

-- Task 06: Performance Ranking
SELECT
    employee_id,
    performance_score,
    DENSE_RANK() OVER (
        ORDER BY performance_score DESC
    ) AS performance_rank
FROM performance;

-- Task 07: Top Performer in Each Department
WITH ranked_employees AS (
    SELECT
        employee_name,
        department,
        salary,
        RANK() OVER (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS department_rank
    FROM employees
)

SELECT
    employee_name,
    department,
    salary
FROM ranked_employees
WHERE department_rank = 1;

-- Task 08: Performance vs Department Average
SELECT
    employees.employee_id,
    performance_score,
    department,
    AVG(performance_score) OVER (
        PARTITION BY department
    ) AS department_average_performance
FROM employees
INNER JOIN performance
ON employees.employee_id = performance.employee_id;

-- Task 09: Employee Performance Position
SELECT 
    employee_name,
    department,
    performance_score,
    AVG(performance_score) OVER (
        PARTITION BY department
    ) AS department_average_score,
    DENSE_RANK() OVER (
        PARTITION BY department
        ORDER BY performance_score DESC
    ) AS performance_rank
FROM employees
INNER JOIN performance
ON employees.employee_id = performance.employee_id;
