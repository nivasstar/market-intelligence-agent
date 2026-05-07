from datetime import datetime

from scoring import calculate_scores
from config import REPORTS_DIR


def build_report():

    results = calculate_scores()

    today = datetime.today().strftime("%Y-%m-%d")

    report = f"""
# Weekly Market Intelligence Report

Date: {today}

---

# Executive Summary

Current Market Regime: **{results['regime']}**

Total Risk Score: **{results['total_risk_score']}**

---

# Market Indicators

| Indicator | Value |
|---|---|
| SPY Close | {results['indicators']['close']} |
| 200DMA | {results['indicators']['200dma']} |
| Distance from 200DMA | {results['indicators']['distance_from_200dma_pct']}% |
| 30D Volatility | {results['indicators']['30d_volatility']}% |
| Drawdown | {results['indicators']['drawdown_pct']}% |

---

# Macro Signals

| Signal | Value |
|---|---|
| Yield Spread (10Y-3M) | {results['macro']['yield_spread_10y_3m']} |
| Unemployment Rate | {results['macro']['unemployment_rate']}% |
| 3M Avg Unemployment | {results['macro']['unemployment_3m_avg']}% |
| 3M Unemployment Change | {results['macro']['unemployment_3m_change']} |

---

# Risk Scoring Breakdown

## Market Risk

| Component | Score |
|---|---|
| Trend Score | {results['market_scores']['trend_score']} |
| Volatility Score | {results['market_scores']['volatility_score']} |
| Drawdown Score | {results['market_scores']['drawdown_score']} |
| Total Market Risk | {results['market_scores']['market_risk_score']} |

---

## Macro Risk

| Component | Score |
|---|---|
| Yield Spread Score | {results['macro_scores']['yield_spread_score']} |
| Unemployment Score | {results['macro_scores']['unemployment_score']} |
| Total Macro Risk | {results['macro_scores']['macro_risk_score']} |

---

# Charts

## SPY vs 200DMA

![SPY](../charts/spy_vs_200dma.png)

---

## 30D Volatility

![Volatility](../charts/30d_volatility.png)

---

## Yield Spread

![Yield Spread](../charts/yield_spread.png)

---

## Unemployment Trend

![Unemployment](../charts/unemployment_trend.png)

---

# Interpretation

This report evaluates current market conditions using technical and macroeconomic indicators.

The scoring model combines trend, volatility, drawdown, yield curve structure, and labor market dynamics into a unified market regime framework.

---

# Disclaimer

This report is for educational and informational purposes only and does not constitute investment advice.
"""

    output_file = REPORTS_DIR / f"market_report_{today}.md"

    with open(output_file, "w") as f:
        f.write(report)

    print(f"\nReport generated: {output_file}\n")


if __name__ == "__main__":
    build_report()
