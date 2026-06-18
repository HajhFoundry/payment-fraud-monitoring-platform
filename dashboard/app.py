import pandas as pd
import streamlit as st
import plotly.express as px
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

cases_df = pd.read_sql("SELECT * FROM fraud_cases", engine)

open_cases = len(cases_df[cases_df["case_status"] == "OPEN"])
investigating_cases = len(cases_df[cases_df["case_status"] == "INVESTIGATING"])
closed_cases = len(cases_df[cases_df["case_status"] == "CLOSED"])

col4, col5, col6 = st.columns(3)

col4.metric("Open Cases", open_cases)
col5.metric("Investigating Cases", investigating_cases)
col6.metric("Closed Cases", closed_cases)

st.subheader("Fraud Alerts by Severity")
severity_df = alerts_df.groupby("severity").size().reset_index(name="count")

fig_severity = px.pie(
    severity_df,
    names="severity",
    values="count",
    title="Fraud Alerts by Severity"
)

st.plotly_chart(fig_severity, use_container_width=True)


st.subheader("Fraud Alerts by Rule")
rule_df = alerts_df.groupby("rule_name").size().reset_index(name="count")

fig_rules = px.bar(
    rule_df.sort_values("count", ascending=True),
    x="count",
    y="rule_name",
    orientation="h",
    title="Fraud Alerts by Rule"
)

st.plotly_chart(fig_rules, use_container_width=True)

st.subheader("Recent Transactions")
st.dataframe(transactions_df.sort_values("transaction_time", ascending=False).head(20))

st.subheader("Recent Fraud Alerts")
st.dataframe(alerts_df.sort_values("created_at", ascending=False).head(20))

st.subheader("Transaction Fraud vs Login Fraud")

transaction_fraud_count = len(alerts_df[alerts_df["transaction_id"].notna()])
login_fraud_count = len(alerts_df[alerts_df["transaction_id"].isna()])

fraud_type_df = pd.DataFrame({
    "Fraud Type": ["Transaction Fraud", "Login / Security Fraud"],
    "Count": [transaction_fraud_count, login_fraud_count]
})

fig_fraud_type = px.pie(
    fraud_type_df,
    names="Fraud Type",
    values="Count",
    title="Transaction Fraud vs Login/Security Fraud"
)

st.plotly_chart(fig_fraud_type, use_container_width=True)

st.subheader("Fraud Cases by Status")

if not cases_df.empty:
    case_status_df = cases_df.groupby("case_status").size().reset_index(name="count")
    
    fig_cases = px.bar(
        case_status_df,
        x="case_status",
        y="count",
        title="Fraud Cases by Status"
    )

    st.plotly_chart(fig_cases, use_container_width=True)
else:
    st.info("No fraud cases found.")

st.subheader("Top Customers by Fraud Alerts")

top_customers_query = """
SELECT
    c.first_name,
    c.last_name,
    COUNT(f.alert_id) AS total_alerts
FROM customers c
JOIN accounts a
    ON c.customer_id = a.customer_id
JOIN transactions t
    ON a.account_id = t.account_id
JOIN fraud_alerts f
    ON t.transaction_id = f.transaction_id
GROUP BY c.first_name, c.last_name
ORDER BY total_alerts DESC;
"""

top_customers_df = pd.read_sql(top_customers_query, engine)

if not top_customers_df.empty:
    top_customers_df["customer_name"] = (
        top_customers_df["first_name"] + " " + top_customers_df["last_name"]
    )
    fig_customers = px.bar(
        top_customers_df,
        x="customer_name",
        y="total_alerts",
        title="Top Customers by Fraud Alerts"
    )

    st.plotly_chart(fig_customers, use_container_width=True)

else:
    st.info("No customer fraud alert data found.")

st.subheader("Recent Fraud Cases")

recent_cases_df = cases_df.sort_values("updated_at", ascending=False).head(20)

st.dataframe(
    recent_cases_df[
        [
            "case_id",
            "alert_id",
            "assigned_to",
            "case_status",
            "notes",
            "updated_at"
        ]
    ],
    use_container_width=True
)

st.subheader("Recent Login Events")

login_events_df = pd.read_sql("SELECT * FROM login_events", engine)

recent_login_df = login_events_df.sort_values("login_time", ascending=False).head(20)

st.dataframe(
    recent_login_df[
        [
            "login_id",
            "customer_id",
            "device_type",
            "browser",
            "country",
            "login_status",
            "otp_status",
            "login_time"
        ]
    ],
    use_container_width=True
)

st.subheader("High Risk Transactions")

high_risk_txn_df = transactions_df[transactions_df["amount"] >= 5000].sort_values(
    "amount",
    ascending=False
)

st.dataframe(
    high_risk_txn_df[
        [
            "transaction_id",
            "account_id",
            "merchant_name",
            "merchant_category",
            "amount",
            "country",
            "status",
            "transaction_time"
        ]
    ],
    use_container_width=True
)

payment_events_df = pd.read_sql("SELECT * FROM payment_events", engine)

st.subheader("Payment Events by Status")

if not payment_events_df.empty:
    payment_status_df = payment_events_df.groupby("payment_status").size().reset_index(name="count")

    fig_payment_status = px.bar(
        payment_status_df,
        x="payment_status",
        y="count",
        title="Payment Events by Status"
    )

    st.plotly_chart(fig_payment_status, use_container_width=True)
else:
    st.info("No payment events found.")

st.subheader("Recent Payment Events")

if not payment_events_df.empty:
    recent_payment_events_df = payment_events_df.sort_values(
        "created_at",
        ascending=False
    ).head(20)

    st.dataframe(
        recent_payment_events_df[
            [
                "payment_event_id",
                "transaction_id",
                "event_type",
                "payment_status",
                "amount",
                "provider",
                "created_at"
            ]
        ],
        use_container_width=True
    )
else:
    st.info("No payment events found.")

