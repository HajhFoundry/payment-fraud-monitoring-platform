@echo off
cd /d C:\projects\enterprise\payment-fraud-monitoring-platform

echo ==========================================
echo Payment Fraud Monitoring Platform Demo
echo ==========================================

echo.
echo Activating virtual environment...
call venv\Scripts\activate

echo.
echo Starting FastAPI server...
start "FastAPI Server" cmd /k "cd /d C:\projects\enterprise\payment-fraud-monitoring-platform && call venv\Scripts\activate && uvicorn app.main:app --reload"

timeout /t 6

echo.
echo Starting Streamlit dashboard...
start "Streamlit Dashboard" cmd /k "cd /d C:\projects\enterprise\payment-fraud-monitoring-platform && call venv\Scripts\activate && streamlit run dashboard/app.py"

timeout /t 8

echo.
echo Opening browser pages...
start http://127.0.0.1:8000/docs
start http://localhost:8501
start https://github.com/HajhFoundry/payment-fraud-monitoring-platform

echo.
echo ==========================================
echo Demo Started
echo ==========================================
echo.
echo Open Postman manually and use:
echo http://127.0.0.1:8000
echo.
echo Suggested demo order:
echo 1. Show GitHub README
echo 2. Show Swagger/FastAPI
echo 3. Create customer/account/transaction
echo 4. Show fraud alerts
echo 5. Show Streamlit dashboard
echo 6. Run Selenium test if needed
echo 7. Show Docker and CI/CD
echo.
pause