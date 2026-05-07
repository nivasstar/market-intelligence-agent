from fetch_data import fetch_market_data, fetch_fred_data
from indicators import calculate_indicators
from macro import calculate_macro_signals
from scoring import calculate_scores
from charts import generate_charts
from report_builder import build_report


def main():
    print("\nStarting Market Intelligence Agent...\n")

    print("Step 1: Fetching market data...")
    fetch_market_data()

    print("Step 2: Fetching macro data...")
    fetch_fred_data()

    print("Step 3: Calculating indicators...")
    calculate_indicators()

    print("Step 4: Calculating macro signals...")
    calculate_macro_signals()

    print("Step 5: Calculating risk scores...")
    calculate_scores()

    print("Step 6: Generating charts...")
    generate_charts()

    print("Step 7: Building report...")
    build_report()

    print("\nMarket Intelligence Agent completed successfully.\n")


if __name__ == "__main__":
    main()
