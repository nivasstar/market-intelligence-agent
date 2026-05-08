# Market Intelligence Agent

Welcome to the Autonomous Market Intelligence Platform.

## About

This platform automatically:

- Pulls market and macroeconomic data
- Computes technical indicators
- Evaluates macro conditions
- Generates risk scores
- Produces visual analytics reports

## Latest Reports

- [Reports Folder](reports/)

## Architecture

```text
Data Sources
   ↓
fetch_data.py
   ↓
indicators.py + macro.py
   ↓
scoring.py
   ↓
charts.py
   ↓
report_builder.py
   ↓
main.py Orchestrator
