from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_RAW_DIR = BASE_DIR / "data" / "raw"
DATA_PROCESSED_DIR = BASE_DIR / "data" / "processed"
CHARTS_DIR = BASE_DIR / "charts"
REPORTS_DIR = BASE_DIR / "reports"

TICKER = "SPY"
START_DATE = "2010-01-01"

FRED_SERIES = {
    "ten_year_treasury": "DGS10",
    "three_month_treasury": "DGS3MO",
    "unemployment_rate": "UNRATE",
}

for folder in [DATA_RAW_DIR, DATA_PROCESSED_DIR, CHARTS_DIR, REPORTS_DIR]:
    folder.mkdir(parents=True, exist_ok=True)
