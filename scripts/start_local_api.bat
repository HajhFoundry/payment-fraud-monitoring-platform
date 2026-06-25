@echo off
cd /d C:\projects\enterprise\payment-fraud-monitoring-platform
call venv\Scripts\activate
uvicorn app.main:app --reload
pause