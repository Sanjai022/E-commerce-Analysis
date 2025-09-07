import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")
query = """
SELECT c.customer_name, MAX(order_date) AS last_order
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_name
HAVING julianday('2024-12-31') - julianday(MAX(order_date)) > 180;
"""
df = pd.read_sql(query, conn)
#print(df)
df.to_excel("inactive_customer.xlsx", index=False)

conn.close()