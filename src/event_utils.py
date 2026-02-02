import pandas as pd

def define_event_window(event_date, window_months=12):
    """
    [cite_start]Defines the pre-event and post-event windows[cite: 37, 220].
    """
    event_dt = pd.to_datetime(event_date)
    pre_start = event_dt - pd.DateOffset(months=window_months)
    post_end = event_dt + pd.DateOffset(months=window_months)
    return pre_start, event_dt, post_end