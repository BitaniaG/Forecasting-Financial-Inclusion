import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_csv

st.set_page_config(
    page_title="Ethiopia Financial Inclusion Forecasts",
    layout="wide"
)

st.title("Ethiopia Financial Inclusion Forecasting Dashboard")

st.markdown("""
This dashboard supports evidence-based decision making
for Ethiopia’s digital financial inclusion strategy.
""")

@st.cache_data
def load_data():
    hist = load_csv(
        "data/processed/ethiopia_fi_unified_data_enriched.csv",
        parse_dates=["observation_date"]
    )
    fc = load_csv("data/forecasts/access_usage_forecasts.csv")
    return hist, fc

hist_df, forecast_df = load_data()

# --- Historical Trends Section ---
st.header("Historical Financial Inclusion Trends")

indicator = st.selectbox(
    "Select Indicator",
    hist_df["indicator"].unique()
)

df_plot = hist_df[
    (hist_df["indicator"] == indicator) &
    (hist_df["record_type"] == "observation")
]

fig = px.line(
    df_plot,
    x="observation_date",
    y="value_numeric",
    title=f"{indicator} – Historical Trend",
    markers=True
)
st.plotly_chart(fig, use_container_width=True)

# --- Event Timeline ---
st.header("Key Events Timeline")
events = hist_df[hist_df["record_type"] == "event"]

if not events.empty:
    fig_evt = px.scatter(
        events,
        x="observation_date",
        y=[1]*len(events),
        text="indicator",
        title="Key Digital Finance Events"
    )
    fig_evt.update_yaxes(visible=False)
    fig_evt.update_traces(textposition="top center")
    st.plotly_chart(fig_evt, use_container_width=True)
else:
    st.info("No events recorded in the dataset.")

# --- Forecasts with Confidence Intervals ---
st.header("Forecasts (2025–2027)")

fc_indicator = st.selectbox(
    "Select Forecast Indicator",
    forecast_df["indicator"].unique()
)

# Use .copy() to avoid SettingWithCopyWarning
df_fc = forecast_df[forecast_df["indicator"] == fc_indicator].copy()

# FIXED: Changed 'forecast' to 'forecast_value'
fig_fc = px.line(
    df_fc,
    x="year",
    y="forecast_value",
    title=f"{fc_indicator} Forecast",
)

fig_fc.add_scatter(
    x=df_fc["year"],
    y=df_fc["lower_ci"],
    mode="lines",
    name="Lower CI",
    line=dict(dash="dash", color="gray")
)

fig_fc.add_scatter(
    x=df_fc["year"],
    y=df_fc["upper_ci"],
    mode="lines",
    name="Upper CI",
    line=dict(dash="dash", color="gray")
)

st.plotly_chart(fig_fc, use_container_width=True)

# --- Scenario Analysis ---
st.header("Scenario Analysis")

scenario = st.slider(
    "Growth Adjustment (%)",
    min_value=-5,
    max_value=10,
    value=0
)

# FIXED: Changed 'forecast' to 'forecast_value'
df_fc["scenario_forecast"] = df_fc["forecast_value"] * (1 + scenario/100)

fig_sc = px.line(
    df_fc,
    x="year",
    y="scenario_forecast",
    title="Scenario-Adjusted Forecast"
)
st.plotly_chart(fig_sc, use_container_width=True)

# --- Key Insights & Limitations ---
st.header("Key Insights & Limitations")
st.markdown("""
### Key Insights
- Access indicators show steady growth through 2027.
- Usage indicators are more sensitive to ecosystem events.
- Post-2021 growth slowdown suggests structural barriers beyond infrastructure.

### Limitations
- Short time series limits model complexity.
- Forecasts assume structural continuity.
- Event impacts are associative, not causal.
""")
# How to use this dashboard
st.markdown("""
### How to Use This Dashboard
- Use the dropdowns to select indicators
- Hover over charts to inspect values
- Adjust scenario sliders to explore alternative futures
- Forecast bands represent uncertainty intervals
""")
