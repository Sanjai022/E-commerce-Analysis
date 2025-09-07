import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")

query = """
SELECT c.segment, SUM(o.sales_amount) AS total_sales, COUNT(o.order_id) AS orders
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.segment;
"""
df = pd.read_sql(query, conn)
print(df)

conn.close()