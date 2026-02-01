import pandas as pd
from datetime import date

def add_enriched_observations(df: pd.DataFrame) -> pd.DataFrame:
    enriched_records = [
        {
            "record_id": "REC_ENR_001",
            "record_type": "observation",
            "pillar": "ACCESS",
            "indicator": "Mobile Phone Penetration",
            "indicator_code": "ACC_MOBILE_PEN",
            "indicator_direction": "higher_better",
            "value_numeric": 55.0,
            "value_type": "percentage",
            "observation_date": date(2025, 12, 31),
            "collected_by": "Bitaniya",
            "confidence": "medium",
            "notes": "Proxy for population access to mobile-based financial services"
        }
    ]

    enriched_df = pd.DataFrame(enriched_records)
    return pd.concat([df, enriched_df], ignore_index=True)
