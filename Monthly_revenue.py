import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")
query = """
SELECT strftime('%Y-%m', order_date) AS month, SUM(sales_amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;
"""
df = pd.read_sql(query, conn)

plt.figure(figsize=(8,5))
plt.plot(df['month'], df['revenue'], marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

conn.close()