REQUIRED_COLUMNS = {
    "record_id",
    "record_type",
    "indicator_code",
    "value_type",
    "observation_date"
}

VALID_RECORD_TYPES = {"observation", "event", "impact_link", "target"}

def validate_schema(df):
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    invalid_types = set(df["record_type"]) - VALID_RECORD_TYPES
    if invalid_types:
        raise ValueError(f"Invalid record_type values: {invalid_types}")

    return True
