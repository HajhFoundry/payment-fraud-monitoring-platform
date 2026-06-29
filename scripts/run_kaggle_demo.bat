@echo off
cd /d C:\projects\enterprise\payment-fraud-monitoring-platform
call venv\Scripts\activate

echo Running Kaggle batch import demo...
python -m app.importers.kaggle_importer

pause