@echo off
cd /d C:\projects\enterprise\payment-fraud-monitoring-platform
call venv\Scripts\activate
python -m app.importers.kaggle_importer
pause