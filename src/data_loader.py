"""
Data Loader Module
Handles loading and initial processing of COVID-19 data from various sources.
"""

import pandas as pd
import numpy as np
from pathlib import Path


def load_csv(filepath: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded data
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def load_multiple_files(directory: str, pattern: str = "*.csv") -> dict:
    """
    Load multiple CSV files from a directory.
    
    Args:
        directory: Directory path containing the files
        pattern: File pattern to match (default: "*.csv")
        
    Returns:
        dict: Dictionary with filenames as keys and DataFrames as values
    """
    data_dict = {}
    data_path = Path(directory)
    
    for file in data_path.glob(pattern):
        try:
            data_dict[file.stem] = pd.read_csv(file)
            print(f"Loaded {file.name}")
        except Exception as e:
            print(f"Error loading {file.name}: {e}")
    
    return data_dict


def get_basic_info(df: pd.DataFrame) -> dict:
    """
    Get basic information about the dataset.
    
    Args:
        df: Input DataFrame
        
    Returns:
        dict: Basic statistics about the data
    """
    info = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": df.duplicated().sum(),
    }
    return info
