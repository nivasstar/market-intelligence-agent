import pandas as pd
import numpy as np

from config import DATA_RAW_DIR, DATA_PROCESSED_DIR


def calculate_indicators():

    file_path = DATA_RAW_DIR / "spy_prices.csv"

    df = pd.read_csv(file_path)

    df["date"] = pd.to_datetime(df["date"])

    # =========================
    # 200-Day Moving Average
    # =========================
    df["200dma"] = df["close"].rolling(window=200).mean()

    # Distance from 200DMA
    df["distance_from_200dma_pct"] = (
        (df["close"] - df["200dma"]) / df["200dma"]
    ) * 100

    # =========================
    # Daily Returns
    # =========================
    df["daily_return"] = df["close"].pct_change()

    # =========================
    # 30-Day Realized Volatility
    # =========================
    df["30d_volatility"] = (
        df["daily_return"]
        .rolling(window=30)
        .std()
        * np.sqrt(252)
        * 100
    )

    # =========================
    # 52-Week Drawdown
    # =========================
    rolling_max = df["close"].rolling(window=252).max()

    df["drawdown_pct"] = (
        (df["close"] - rolling_max) / rolling_max
    ) * 100

    # Save processed file
    output_path = DATA_PROCESSED_DIR / "spy_indicators.csv"

    df.to_csv(output_path, index=False)

    # Latest values summary
    latest = df.iloc[-1]

    summary = {
        "close": round(latest["close"], 2),
        "200dma": round(latest["200dma"], 2),
        "distance_from_200dma_pct": round(latest["distance_from_200dma_pct"], 2),
        "30d_volatility": round(latest["30d_volatility"], 2),
        "drawdown_pct": round(latest["drawdown_pct"], 2),
    }

    return summary


if __name__ == "__main__":

    summary = calculate_indicators()

    print("\nIndicator Summary\n")
    print(summary)
