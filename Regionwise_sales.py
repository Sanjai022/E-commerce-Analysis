import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")

query = """
SELECT region, SUM(sales_amount) AS total_sales
FROM orders
GROUP BY region;
"""
df = pd.read_sql(query, conn)

df.plot(kind="bar", x="region", y="total_sales", legend=False, color="green")
plt.title("Sales by Region")
plt.ylabel("Total Sales")
plt.show()

conn.close()