-- Create Database (skip if using SQLite)
CREATE DATABASE ecommerce;
USE ecommerce;

-- Customers Table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    country VARCHAR(50)
);

-- Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name VARCHAR(100)
);

-- Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    ship_date DATE,
    region VARCHAR(50),
    sales_amount FLOAT,
    discount FLOAT,
    profit FLOAT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO customers VALUES
(1, 'Alice Johnson', 'Consumer', 'India'),
(2, 'Bob Smith', 'Corporate', 'USA'),
(3, 'Chitra Patel', 'Home Office', 'India'),
(4, 'David Lee', 'Consumer', 'UK'),
(5, 'Emma Brown', 'Corporate', 'Canada');

INSERT INTO products VALUES
(101, 'Technology', 'Phones', 'iPhone 14'),
(102, 'Technology', 'Laptops', 'Dell XPS 15'),
(103, 'Furniture', 'Chairs', 'Ergonomic Chair'),
(104, 'Office Supplies', 'Paper', 'A4 Printing Paper'),
(105, 'Furniture', 'Tables', 'Wooden Dining Table');

INSERT INTO orders VALUES
(1001, 1, 101, '2024-01-15', '2024-01-18', 'Asia', 90000, 0.10, 12000),
(1002, 2, 102, '2024-02-05', '2024-02-10', 'North America', 150000, 0.15, 25000),
(1003, 3, 103, '2024-02-20', '2024-02-22', 'Asia', 20000, 0.05, 5000),
(1004, 4, 104, '2024-03-01', '2024-03-03', 'Europe', 2000, 0.00, 500),
(1005, 5, 105, '2024-03-10', '2024-03-15', 'North America', 40000, 0.20, 8000),
(1006, 1, 103, '2024-04-12', '2024-04-15', 'Asia', 25000, 0.10, 6000),
(1007, 2, 101, '2024-04-20', '2024-04-23', 'North America', 85000, 0.05, 15000),
(1008, 3, 104, '2024-05-05', '2024-05-07', 'Asia', 3000, 0.00, 700);

CREATE VIEW high_value_customers AS
SELECT c.customer_name, SUM(o.sales_amount) AS total_sales
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_name
HAVING total_sales > 50000;

-- Top 10 customers by total purchase
SELECT c.customer_name, SUM(o.sales_amount) AS total_sales
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_sales DESC
LIMIT 10;

-- Monthly Revenue
SELECT strftime('%Y-%m', order_date) AS month, SUM(sales_amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;

-- Most profitable product categories
SELECT p.category, SUM(o.profit) AS total_profit
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY total_profit DESC;

-- Region with highest sales per order
SELECT region, AVG(sales_amount) AS avg_sales
FROM orders
GROUP BY region
ORDER BY avg_sales DESC;

-- Customer with 5+ orders
SELECT c.customer_name, COUNT(o.order_id) AS order_count
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE strftime('%Y', order_date) = '2024'
GROUP BY c.customer_name
HAVING COUNT(o.order_id) > 5;

