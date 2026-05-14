from fetch_data import fetch_market_data, fetch_fred_data
from scoring import calculate_scores
from charts import generate_charts
from report_builder import build_report


def main():
    print("\nStarting Market Intelligence Agent...\n")

    print("Step 1: Fetching market data...")
    fetch_market_data()

    print("Step 2: Fetching macro data...")
    fetch_fred_data()

    print("Step 3: Calculating indicators, macro signals, and risk scores...")
    results = calculate_scores()

    print("Step 4: Generating charts...")
    generate_charts()

    print("Step 5: Building report...")
    build_report(results)

    print("\nMarket Intelligence Agent completed successfully.\n")


if __name__ == "__main__":
    main()
