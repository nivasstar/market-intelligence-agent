import pandas as pd

from config import DATA_RAW_DIR, DATA_PROCESSED_DIR


def calculate_macro_signals():
    file_path = DATA_RAW_DIR / "fred_macro_data.csv"

    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])

    df = df.sort_values("date")

    # Forward-fill because FRED series have different frequencies
    df[["ten_year_treasury", "three_month_treasury", "unemployment_rate"]] = (
        df[["ten_year_treasury", "three_month_treasury", "unemployment_rate"]]
        .ffill()
    )

    # 10Y - 3M yield spread
    df["yield_spread_10y_3m"] = (
        df["ten_year_treasury"] - df["three_month_treasury"]
    )

    # Unemployment 3-month moving average
    df["unemployment_3m_avg"] = df["unemployment_rate"].rolling(window=3).mean()

    # Compare latest 3-month avg vs previous 3-month avg
    df["unemployment_3m_change"] = df["unemployment_3m_avg"].diff(3)

    output_path = DATA_PROCESSED_DIR / "macro_signals.csv"
    df.to_csv(output_path, index=False)

    latest = df.dropna().iloc[-1]

    summary = {
        "yield_spread_10y_3m": round(float(latest["yield_spread_10y_3m"]), 2),
        "unemployment_rate": round(float(latest["unemployment_rate"]), 2),
        "unemployment_3m_avg": round(float(latest["unemployment_3m_avg"]), 2),
        "unemployment_3m_change": round(float(latest["unemployment_3m_change"]), 2),
    }

    return summary


if __name__ == "__main__":
    summary = calculate_macro_signals()

    print("\nMacro Signal Summary\n")
    print(summary)
