import pandas as pd
import matplotlib.pyplot as plt

from config import (
    DATA_PROCESSED_DIR,
    CHARTS_DIR
)


def generate_charts():

    # =========================
    # Load datasets
    # =========================
    indicators_df = pd.read_csv(
        DATA_PROCESSED_DIR / "spy_indicators.csv"
    )

    macro_df = pd.read_csv(
        DATA_PROCESSED_DIR / "macro_signals.csv"
    )

    indicators_df["date"] = pd.to_datetime(indicators_df["date"])
    macro_df["date"] = pd.to_datetime(macro_df["date"])

    # =========================
    # Chart 1: SPY vs 200DMA
    # =========================
    plt.figure(figsize=(12, 6))

    plt.plot(
        indicators_df["date"],
        indicators_df["close"],
        label="SPY Close"
    )

    plt.plot(
        indicators_df["date"],
        indicators_df["200dma"],
        label="200DMA"
    )

    plt.title("SPY vs 200-Day Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()

    plt.savefig(CHARTS_DIR / "spy_vs_200dma.png")
    plt.close()

    # =========================
    # Chart 2: 30D Volatility
    # =========================
    plt.figure(figsize=(12, 6))

    plt.plot(
        indicators_df["date"],
        indicators_df["30d_volatility"]
    )

    plt.title("30-Day Realized Volatility")
    plt.xlabel("Date")
    plt.ylabel("Volatility (%)")

    plt.savefig(CHARTS_DIR / "30d_volatility.png")
    plt.close()

    # =========================
    # Chart 3: Yield Spread
    # =========================
    plt.figure(figsize=(12, 6))

    plt.plot(
        macro_df["date"],
        macro_df["yield_spread_10y_3m"]
    )

    plt.axhline(0, linestyle="--")

    plt.title("10Y - 3M Yield Spread")
    plt.xlabel("Date")
    plt.ylabel("Spread (%)")

    plt.savefig(CHARTS_DIR / "yield_spread.png")
    plt.close()

    # =========================
    # Chart 4: Unemployment
    # =========================
    plt.figure(figsize=(12, 6))

    plt.plot(
        macro_df["date"],
        macro_df["unemployment_rate"],
        label="Unemployment Rate"
    )

    plt.plot(
        macro_df["date"],
        macro_df["unemployment_3m_avg"],
        label="3M Average"
    )

    plt.title("Unemployment Trend")
    plt.xlabel("Date")
    plt.ylabel("Rate (%)")
    plt.legend()

    plt.savefig(CHARTS_DIR / "unemployment_trend.png")
    plt.close()

    print("\nCharts generated successfully.\n")


if __name__ == "__main__":
    generate_charts()
