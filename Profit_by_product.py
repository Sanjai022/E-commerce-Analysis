import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")

query = """
SELECT p.category, SUM(o.profit) AS total_profit
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY total_profit DESC;
"""
df = pd.read_sql(query, conn)

df.plot(kind="bar", x="category", y="total_profit", legend=False, color="orange")
plt.title("Profit by Product Category")
plt.ylabel("Profit")
plt.show()


conn.close()