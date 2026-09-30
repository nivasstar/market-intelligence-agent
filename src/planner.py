from datetime import datetime


def create_plan():
    today = datetime.today()

    plan = {
        "run_date": today.strftime("%Y-%m-%d"),
        "tasks": [
            "fetch_data",
            "calculate_indicators",
            "calculate_macro",
            "calculate_scores",
            "generate_charts",
            "build_report",
            "publish"
        ]
    }

    return plan

