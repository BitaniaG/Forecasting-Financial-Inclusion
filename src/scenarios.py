def apply_event_adjustment(forecast_df, adjustment_rate):
    """
    Apply event-based uplift or downside.
    """
    if forecast_df.empty:
        return forecast_df
        
    adjusted = forecast_df.copy()
    # Changed "forecast" to "forecast_value" to match trend_forecast output
    adjusted["forecast_value"] = (
        adjusted["forecast_value"] * (1 + adjustment_rate)
    )
    return adjusted