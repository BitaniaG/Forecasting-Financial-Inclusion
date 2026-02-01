import pandas as pd
from pathlib import Path

def load_csv(path: str, parse_dates=None) -> pd.DataFrame:
    """
    Load a CSV file with basic validation.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path)
    
    if parse_dates:
        for col in parse_dates:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors="coerce")

    return df
