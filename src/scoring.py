from indicators import calculate_indicators
from macro import calculate_macro_signals


def calculate_market_score(indicators):
    score = 0

    # Trend: distance from 200DMA
    if indicators["distance_from_200dma_pct"] >= 5:
        trend_score = 5
    elif indicators["distance_from_200dma_pct"] >= 0:
        trend_score = 10
    elif indicators["distance_from_200dma_pct"] >= -5:
        trend_score = 25
    else:
        trend_score = 40

    # Volatility
    if indicators["30d_volatility"] < 15:
        vol_score = 5
    elif indicators["30d_volatility"] < 25:
        vol_score = 15
    else:
        vol_score = 30

    # Drawdown
    if indicators["drawdown_pct"] > -5:
        drawdown_score = 5
    elif indicators["drawdown_pct"] > -15:
        drawdown_score = 15
    else:
        drawdown_score = 30

    score = trend_score + vol_score + drawdown_score

    return {
        "trend_score": trend_score,
        "volatility_score": vol_score,
        "drawdown_score": drawdown_score,
        "market_risk_score": score,
    }


def calculate_macro_score(macro):
    # Yield spread score
    if macro["yield_spread_10y_3m"] >= 1:
        yield_score = 5
    elif macro["yield_spread_10y_3m"] >= 0:
        yield_score = 20
    else:
        yield_score = 50

    # Unemployment trend score
    if macro["unemployment_3m_change"] <= 0:
        unemployment_score = 5
    elif macro["unemployment_3m_change"] <= 0.2:
        unemployment_score = 20
    else:
        unemployment_score = 50

    macro_risk_score = yield_score + unemployment_score

    return {
        "yield_spread_score": yield_score,
        "unemployment_score": unemployment_score,
        "macro_risk_score": macro_risk_score,
    }


def classify_risk(total_score):
    if total_score < 40:
        return "Low Risk"
    elif total_score < 80:
        return "Neutral / Watchlist"
    else:
        return "Elevated Risk"


def calculate_scores():
    indicators = calculate_indicators()
    macro = calculate_macro_signals()

    market_scores = calculate_market_score(indicators)
    macro_scores = calculate_macro_score(macro)

    total_score = market_scores["market_risk_score"] + macro_scores["macro_risk_score"]
    regime = classify_risk(total_score)

    return {
        "indicators": indicators,
        "macro": macro,
        "market_scores": market_scores,
        "macro_scores": macro_scores,
        "total_risk_score": total_score,
        "regime": regime,
    }


if __name__ == "__main__":
    results = calculate_scores()

    print("\nRisk Scoring Summary\n")
    print(results)
