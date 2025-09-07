import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")

query = "SELECT discount, profit FROM orders;"
df = pd.read_sql(query, conn)

plt.scatter(df['discount'], df['profit'], alpha=0.6)
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.show()

conn.close()