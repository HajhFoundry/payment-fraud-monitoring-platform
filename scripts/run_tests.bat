@echo off
cd /d C:\projects\enterprise\payment-fraud-monitoring-platform
call venv\Scripts\activate
pytest
pause