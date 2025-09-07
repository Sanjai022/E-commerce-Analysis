import streamlit as st
import sqlite3
import pandas as pd

st.title("📊 E-commerce Sales Dashboard")

conn = sqlite3.connect("ecommerce.db")

query = "SELECT strftime('%Y-%m', order_date) AS month, SUM(sales_amount) AS revenue FROM orders GROUP BY month"
df = pd.read_sql(query, conn)

st.line_chart(df, x="month", y="revenue")

conn.close()
