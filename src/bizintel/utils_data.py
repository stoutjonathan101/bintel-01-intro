"""utils_data.py - reusable data loading functions.

WHY: Reading CSV files into DataFrames is the first step
in every BI pipeline.
One shared function keeps this consistent across all modules.
"""

from pathlib import Path

import pandas as pd

from bizintel.utils_logger import LOG

pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 120)


def load_data(filepath: Path, name: str) -> pd.DataFrame:
    """Load one CSV file into a pandas DataFrame.

    Args:
        filepath: Path to the CSV file.
        name: A short name for logging.

    Returns:
        A pandas DataFrame with the file contents.
    """
    LOG.info(f"Loading {name} from {filepath}")
    df: pd.DataFrame = pd.read_csv(filepath)
    LOG.info(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df
