import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def trend_forecast(df, indicator, start_year, end_year):
    # Filter data for the specific indicator
    data = df[df["indicator_code"] == indicator].dropna(subset=["value_numeric"])
    
    if data.empty:
        return pd.DataFrame(columns=["year", "forecast_value"])

    data["year"] = pd.to_datetime(data["observation_date"]).dt.year
    
    # Simple Linear Regression
    X = data[["year"]].values
    y = data["value_numeric"].values
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Generate future years
    future_years = np.array(range(start_year, end_year + 1)).reshape(-1, 1)
    predictions = model.predict(future_years)
    
    return pd.DataFrame({
        "year": future_years.flatten(),
        "forecast_value": predictions
    })