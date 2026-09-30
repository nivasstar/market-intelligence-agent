import pandas as pd

from config import DATA_RAW_DIR, DATA_PROCESSED_DIR


def calculate_macro_signals():
    df = pd.read_csv(DATA_RAW_DIR / "fred_macro_data.csv")
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").set_index("date")

    # Calculate labor trends from monthly observations before forward-filling.
    unemployment = df["unemployment_rate"].dropna()
    monthly = unemployment.resample("MS").last().dropna()

    labor = pd.DataFrame({"unemployment_rate": monthly})
    labor["unemployment_3m_avg"] = monthly.rolling(3).mean()
    labor["unemployment_3m_change"] = (
        labor["unemployment_3m_avg"].diff(3)
    )

    # Align monthly labor signals with daily Treasury observations.
    dates = df.index.union(labor.index).sort_values()
    signals = df[
        ["ten_year_treasury", "three_month_treasury"]
    ].reindex(dates).ffill()
    signals = signals.join(labor.reindex(dates).ffill())
    signals["yield_spread_10y_3m"] = (
        signals["ten_year_treasury"]
        - signals["three_month_treasury"]
    )
    signals.index.name = "date"

    signals.to_csv(DATA_PROCESSED_DIR / "macro_signals.csv")

    fields = [
        "yield_spread_10y_3m",
        "unemployment_rate",
        "unemployment_3m_avg",
        "unemployment_3m_change",
    ]
    valid = signals.dropna(subset=fields)
    if valid.empty:
        raise ValueError("Insufficient data to calculate macro signals.")

    latest = valid.iloc[-1]
    return {
        field: round(float(latest[field]), 2)
        for field in fields
    }


if __name__ == "__main__":
    print("\nMacro Signal Summary\n")
    print(calculate_macro_signals())
