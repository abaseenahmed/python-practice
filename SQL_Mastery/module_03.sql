--================================== Aggregation & Analytical SQL ===========================--
-- Task 01
SELECT count(*) AS total_customers
FROM customers;

-- Task 02
SELECT 
    count(*) AS total_customers,
    count(age) AS customers_with_ages,
    avg(age) AS average_age,
    min(age) AS minimum_age,
    max(age) AS maximum_age
FROM customers;

-- Task 03
SELECT 
    country,
    count(country) AS country_count
FROM customers
GROUP BY country
ORDER BY country_count DESC;

-- Task 04
SELECT 
    country,
    avg(age) AS avg_age_by_country
FROM customers
GROUP BY country
ORDER BY avg_age_by_country DESC;

-- Task 05
SELECT 
    country,
    max(age) AS oldest_age_by_country
FROM customers
GROUP BY country
ORDER BY oldest_age_by_country DESC;

-- Task 06
SELECT 
    country,
    count(*) AS customer_count
FROM customers
GROUP BY country
HAVING count(*) > 2;

-- Task 07
SELECT 
    country,
    count(*) AS customer_count
FROM customers
WHERE age >= 25
GROUP BY country;

-- Task 08
SELECT 
    country,
    count(*) AS customer_count
FROM customers
WHERE age >= 25
GROUP BY country
HAVING count(*) > 2;

-- Task 09
SELECT 
    country,
    AVG(age) AS average_age
FROM customers
GROUP BY country
HAVING AVG(age) > 27;