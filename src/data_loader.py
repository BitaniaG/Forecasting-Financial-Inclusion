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

def load_enriched_data(project_root: Path) -> pd.DataFrame:
    """
    [cite_start]Loads the enriched unified financial inclusion dataset[cite: 43, 118].
    """
    file_path = project_root / "data" / "processed" / "ethiopia_fi_unified_data_enriched.csv"
    return load_csv(file_path, parse_dates=["observation_date", "collection_date"])

def load_reference_codes(project_root: Path) -> pd.DataFrame:
    """
    [cite_start]Loads the reference codes for categorical fields[cite: 50, 98].
    """
    file_path = project_root / "data" / "raw" / "reference_codes.csv"
    return load_csv(file_path)