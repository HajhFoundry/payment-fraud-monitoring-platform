@echo off
cd /d C:\projects\enterprise\payment-fraud-monitoring-platform
call venv\Scripts\activate
streamlit run dashboard/app.py
pause