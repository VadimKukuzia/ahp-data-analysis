import os
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def load_dataset(file_path: str) -> pd.DataFrame:
    """Load dataset from CSV file."""
    logging.info(f"Loading dataset: {file_path}")
    return pd.read_csv(file_path, sep=',', encoding='utf8')
