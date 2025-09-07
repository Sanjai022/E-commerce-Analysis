import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect("ecommerce.db")

#Example query
#query = "SELECT * FROM customers"
#df = pd.read_sql(query, conn)
#print(df)

# Top 10 customers by total purchase
query = """
SELECT c.customer_name, SUM(o.sales_amount) AS total_sales
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_sales DESC
LIMIT 10;
"""
df = pd.read_sql(query, conn)
print(df)

# Monthly Revenue
query = """
SELECT strftime('%Y-%m', order_date) AS month, SUM(sales_amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;
"""
df = pd.read_sql(query, conn)
print(df)

# Most Profitable Product Categories 
query = """
SELECT p.category, SUM(o.profit) AS total_profit
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY total_profit DESC;
"""
df = pd.read_sql(query, conn)
print(df)

# Region with highest sales per order
query = """
SELECT region, AVG(sales_amount) AS avg_sales
FROM orders
GROUP BY region
ORDER BY avg_sales DESC;
"""
df = pd.read_sql(query, conn)
print(df)

# Customers with 5+ order in a year
query = """
SELECT c.customer_name, COUNT(o.order_id) AS order_count
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE strftime('%Y', order_date) = '2024'
GROUP BY c.customer_name
HAVING COUNT(o.order_id) > 5;
"""
df = pd.read_sql(query, conn)
print(df)


conn.close()
