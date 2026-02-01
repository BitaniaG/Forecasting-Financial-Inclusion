import pandas as pd

def record_distribution(df, column):
    return (
        df[column]
        .value_counts()
        .reset_index()
        .rename(columns={"index": column, column: "count"})
    )

def temporal_coverage(df):
    df = df.copy()
    df["year"] = df["observation_date"].dt.year
    return df.groupby("year").size()
