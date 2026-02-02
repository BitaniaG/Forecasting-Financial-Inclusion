import pandas as pd

def pre_post_indicator_change(df, indicator_code, pre_start, event_date, post_end):
    """
    [cite_start]Calculates the change in an indicator before and after an event[cite: 37, 221].
    """
    indicator_data = df[df["indicator_code"] == indicator_code].copy()
    indicator_data["observation_date"] = pd.to_datetime(indicator_data["observation_date"])

    pre_val = indicator_data[(indicator_data["observation_date"] >= pre_start) & 
                             (indicator_data["observation_date"] < event_date)]["value_numeric"].mean()
    
    post_val = indicator_data[(indicator_data["observation_date"] >= event_date) & 
                              (indicator_data["observation_date"] <= post_end)]["value_numeric"].mean()

    if pd.isna(pre_val) or pd.isna(post_val):
        return None

    return {
        "pre_value": pre_val,
        "post_value": post_val,
        "absolute_change": post_val - pre_val
    }