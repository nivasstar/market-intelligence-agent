
# Market Intelligence Agent

An autonomous analytics pipeline that pulls market and macroeconomic data, computes risk signals, generates charts, scores market conditions, and produces weekly intelligence reports.

## Project Purpose

This project demonstrates how data engineering, analytics, automation, and agent-style orchestration can be combined to create a repeatable market intelligence workflow.

## v1 Scope

### Market Indicators

- SPY close price
- 200-day moving average
- Distance from 200DMA
- 30-day realized volatility
- 52-week drawdown

### Macro Signals

- 10Y minus 3M Treasury yield spread
- Unemployment rate
- 3-month unemployment trend

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
