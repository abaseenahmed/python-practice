-- ======================== Subqueries & Common Table Expression (CTE) ================== --
DROP TABLE IF EXISTS performance;
DROP TABLE IF EXISTS employees;

-- CREATING EMPLOYEES TABLE
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name VARCHAR(100),
    department VARCHAR(50),
    salary NUMERIC(10,2),
    hire_date DATE
);

INSERT INTO employees
(employee_id, employee_name, department, salary, hire_date)
VALUES
(1, 'Ali Ahmed', 'Engineering', 85000, '2022-03-15'),
(2, 'Sara Khan', 'Engineering', 72000, '2023-06-10'),
(3, 'John Smith', 'Marketing', 58000, '2021-09-20'),
(4, 'Emma Wilson', 'HR', 52000, '2024-01-15'),
(5, 'Hamza Ali', 'Engineering', 95000, '2020-07-01'),
(6, 'Ayesha Malik', 'Marketing', 64000, '2022-11-05'),
(7, 'David Brown', 'HR', 48000, '2023-08-18'),
(8, 'Daniel Taylor', 'Engineering', 68000, '2024-02-12');

-- CREATING PERFORMENCE TABLE
CREATE TABLE performance (
    performance_id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    performance_score NUMERIC(5,2),
    projects_completed INTEGER,
    review_date DATE
);

INSERT INTO performance
(performance_id, employee_id, performance_score, projects_completed, review_date)
VALUES
(1, 1, 91.5, 8, '2026-06-30'),
(2, 2, 84.0, 6, '2026-06-30'),
(3, 3, 76.5, 5, '2026-06-30'),
(4, 4, 88.0, 7, '2026-06-30'),
(5, 5, 95.5, 10, '2026-06-30'),
(6, 6, 81.0, 6, '2026-06-30'),
(7, 7, 72.5, 4, '2026-06-30'),
(8, 8, 89.0, 7, '2026-06-30');

SELECT * FROM employees;
SELECT * FROM performance;

-- Example 1: Employees earning above average
SELECT
    employee_name,
    department,
    salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
)
ORDER BY salary DESC;

-- Subquery with MAX() MIN()
SELECT
    employee_name,
    salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);

SELECT
    employee_name,
    department,
    salary
FROM employees
WHERE salary = (
    SELECT MIN(salary)
    FROM employees
);

-- Subqueries for Comparison
SELECT
    employee_name,
    department,
    salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department = 'Engineering'
);

-- Subquery in SELECT
SELECT
    employee_name,
    salary,
    (
        SELECT AVG(salary)
        FROM employees
    ) AS company_average_salary
FROM employees;

-- IN with Subqueries
SELECT
    employee_name,
    department,
    salary
FROM employees
WHERE department IN (
    SELECT department
    FROM employees
    GROUP BY department
    HAVING AVG(salary) > 60000
);

-- EXAMPLE OF CTE Common Table Expression
WITH salary_stats AS (
    SELECT AVG(salary) AS average_salary
    FROM employees
)

SELECT
    employee_name,
    salary
FROM employees
WHERE salary > (
    SELECT average_salary
    FROM salary_stats
);

-- Example 02 of CTE
WITH employee_metrics AS (
    SELECT
        employee_id,
        AVG(performance_score) AS avg_score,
        SUM(projects_completed) AS total_projects
    FROM performance
    GROUP BY employee_id
)

SELECT *
FROM employee_metrics;

-- Multiple CTEs
WITH employee_metrics AS (
    SELECT
        employee_id,
        AVG(performance_score) AS avg_score,
        SUM(projects_completed) AS total_projects
    FROM performance
    GROUP BY employee_id
),

high_performers AS (
    SELECT *
    FROM employee_metrics
    WHERE avg_score >= 85
)

SELECT *
FROM high_performers;

-- Task 01
SELECT
    employee_name,
    department,
    salary
FROM employees
WHERE salary > (
    SELECT AVG(salary) 
    FROM employees
)

-- Task 02
SELECT
    employee_id,
    performance_score
FROM performance
WHERE performance_score = (
    SELECT MAX(performance_score)
    FROM performance
);

-- Task 03
SELECT
    employee_name,
    salary
FROM employees
WHERE salary < (
    SELECT AVG(salary)
    FROM employees
);

-- Task 04
SELECT
    employee_name,
    department,
    salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department = 'Engineering'
);

-- Task 05
SELECT
    employee_name,
    department,
    salary
FROM employees
WHERE department IN (
    SELECT department
    FROM employees
    GROUP BY department
    HAVING AVG(salary) > 60000
);

-- Task 06
WITH performance_stats AS (
    SELECT
        employee_id,
        AVG(performance_score) AS avg_score,
        SUM(projects_completed) AS completed_projects
    FROM performance
    GROUP BY employee_id
)
SELECT *
FROM performance_stats;

-- Task 07
WITH medium_scorer AS (
    SELECT 
        employee_id,
        AVG(performance_score) AS average_score
    FROM performance
    GROUP BY employee_id
    HAVING AVG(performance_score) >= 85
)
SELECT *
FROM medium_scorer;

-- Task 08
WITH employee_metrics AS (
    SELECT
        employee_id,
        AVG(performance_score) AS avg_score,
        SUM(projects_completed) AS total_projects
    FROM performance
    GROUP BY employee_id
)

SELECT
    e.employee_name,
    e.department,
    e.salary,
    em.avg_score,
    em.total_projects
FROM employees e
JOIN employee_metrics em
    ON e.employee_id = em.employee_id;
