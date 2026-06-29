@echo off
cd /d C:\projects\enterprise\payment-fraud-monitoring-platform
call venv\Scripts\activate

echo Running Selenium UI tests...
pytest tests/ui

pause