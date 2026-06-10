import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/payment_fraud_db"

engine = create_engine(DATABASE_URL)

st.set_page_config(
    page_title="Payment Fraud Monitoring Dashboard",
    layout="wide"
)

st.title("Payment Fraud Monitoring Dashboard")

transactions_df = pd.read_sql("SELECT * FROM transactions", engine)
alerts_df = pd.read_sql("SELECT * FROM fraud_alerts", engine)

total_transactions = len(transactions_df)
total_alerts = len(alerts_df)
fraud_rate = round((total_alerts / total_transactions) * 100, 2) if total_transactions > 0 else 0

col1, col2, col3 = st.columns(3)

col1.metric("Total Transactions", total_transactions)
col2.metric("Total Fraud Alerts", total_alerts)
col3.metric("Fraud Alert Rate", f"{fraud_rate}%")

st.subheader("Fraud Alerts by Severity")
severity_df = alerts_df.groupby("severity").size().reset_index(name="count")
st.bar_chart(severity_df.set_index("severity"))

st.subheader("Fraud Alerts by Rule")
rule_df = alerts_df.groupby("rule_name").size().reset_index(name="count")
st.bar_chart(rule_df.set_index("rule_name"))

st.subheader("Recent Transactions")
st.dataframe(transactions_df.sort_values("transaction_time", ascending=False).head(20))

st.subheader("Recent Fraud Alerts")
st.dataframe(alerts_df.sort_values("created_at", ascending=False).head(20))