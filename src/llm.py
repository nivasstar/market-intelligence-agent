import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


def generate_summary(report_context):
    if os.getenv("ENABLE_AI_SUMMARY", "false").lower() != "true":
        return "AI commentary is disabled for this run."

    load_dotenv(Path(__file__).resolve().parents[1] / ".env")

    if not os.getenv("OPENAI_API_KEY"):
        return "AI summary unavailable: API key is not configured."

    try:
        client = OpenAI(timeout=45.0, max_retries=0)
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            store=False,
            instructions=(
                "Write a market report executive summary of 120-160 words "
                "in two short paragraphs. Use only the supplied report. "
                "Preserve its rules-based regime and score exactly. "
                "Distinguish observation dates from report generation date; "
                "unemployment dates are reference months, not release dates. "
                "Explain technical conditions, macro signals, and what to "
                "monitor next. Score thresholds are: below 40 Low Risk; "
                "40 to below 80 Neutral / Watchlist; 80+ Elevated Risk. "
                "These are heuristic scores, not probabilities. "
                "Do not invent news, forecasts, prior readings, causation, "
                "or investment recommendations. No heading or disclaimer."
            ),
            input=report_context,
            max_output_tokens=500,
        )
        summary = response.output_text.strip()
        if response.status != "completed" or not summary:
            raise ValueError("Incomplete or empty summary")
        return summary
    except Exception as error:
        print(
            f"AI summary unavailable: {type(error).__name__}; "
            f"status={getattr(error, 'status_code', None)}; "
            f"code={getattr(error, 'code', None)}"
        )
        return (
            "AI summary unavailable for this run. "
            "The calculated indicators and risk scores are shown below."
        )
