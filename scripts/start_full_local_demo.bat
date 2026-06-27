@echo off
cd /d C:\projects\enterprise\payment-fraud-monitoring-platform

echo Activating virtual environment...
call venv\Scripts\activate

echo Starting FastAPI...
start "FastAPI Server" cmd /k "cd /d C:\projects\enterprise\payment-fraud-monitoring-platform && call venv\Scripts\activate && uvicorn app.main:app --reload"

timeout /t 5

echo Starting Streamlit Dashboard...
start "Streamlit Dashboard" cmd /k "cd /d C:\projects\enterprise\payment-fraud-monitoring-platform && call venv\Scripts\activate && streamlit run dashboard/app.py"

timeout /t 8

echo Opening Swagger and Dashboard...
start http://127.0.0.1:8000/docs
start http://localhost:8501

echo Demo environment started.
pause