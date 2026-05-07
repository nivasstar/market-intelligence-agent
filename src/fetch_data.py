import os
import pandas as pd
import yfinance as yf
from fredapi import Fred
from dotenv import load_dotenv

from config import DATA_RAW_DIR, TICKER, START_DATE, FRED_SERIES


def fetch_market_data():
    df = yf.download(TICKER, start=START_DATE, progress=False)

    if df.empty:
        raise ValueError(f"No market data returned for {TICKER}")

    df = df.reset_index()
    df = df[["Date", "Close"]]
    df.columns = ["date", "close"]

    output_path = DATA_RAW_DIR / f"{TICKER.lower()}_prices.csv"
    df.to_csv(output_path, index=False)

    return df


def fetch_fred_data():
    load_dotenv()

    fred_api_key = os.getenv("FRED_API_KEY")
    if not fred_api_key:
        raise ValueError("Missing FRED_API_KEY. Add it to your .env file.")

    fred = Fred(api_key=fred_api_key)

    frames = []
   
    for name, series_id in FRED_SERIES.items():
        print(f"Fetching FRED series: {name} ({series_id})")
        series = fred.get_series(series_id)
        series = series[series.index >= START_DATE]

        temp = series.reset_index()
        temp.columns = ["date", name]
        frames.append(temp)

    macro_df = frames[0]

    for frame in frames[1:]:
        macro_df = macro_df.merge(frame, on="date", how="outer")

    macro_df = macro_df.sort_values("date")

    output_path = DATA_RAW_DIR / "fred_macro_data.csv"
    macro_df.to_csv(output_path, index=False)

    return macro_df


if __name__ == "__main__":
    market = fetch_market_data()
    macro = fetch_fred_data()

    print("Market data rows:", len(market))
    print("Macro data rows:", len(macro))
    print("Data saved to:", DATA_RAW_DIR)
