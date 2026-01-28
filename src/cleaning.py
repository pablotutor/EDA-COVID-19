"""
Data Cleaning Module
Handles data cleaning, validation, and preprocessing operations.
"""

import pandas as pd
import numpy as np


def remove_duplicates(df: pd.DataFrame, subset: list = None) -> pd.DataFrame:
    """
    Remove duplicate rows from DataFrame.
    
    Args:
        df: Input DataFrame
        subset: List of columns to consider for duplicates
        
    Returns:
        pd.DataFrame: DataFrame with duplicates removed
    """
    initial_shape = df.shape[0]
    df_clean = df.drop_duplicates(subset=subset)
    removed = initial_shape - df_clean.shape[0]
    print(f"Removed {removed} duplicate rows")
    return df_clean


def handle_missing_values(df: pd.DataFrame, method: str = "drop", threshold: float = 0.5) -> pd.DataFrame:
    """
    Handle missing values in DataFrame.
    
    Args:
        df: Input DataFrame
        method: 'drop' to remove rows/cols with missing values, 'fill' to fill with strategy
        threshold: Threshold for dropping columns (% of missing values)
        
    Returns:
        pd.DataFrame: Cleaned DataFrame
    """
    df_clean = df.copy()
    
    # Drop columns with missing values above threshold
    missing_pct = df_clean.isnull().sum() / len(df_clean)
    cols_to_drop = missing_pct[missing_pct > threshold].index
    df_clean = df_clean.drop(columns=cols_to_drop)
    
    if method == "drop":
        df_clean = df_clean.dropna()
    elif method == "fill":
        df_clean = df_clean.fillna(df_clean.mean(numeric_only=True))
    
    print(f"Missing values handled. Final shape: {df_clean.shape}")
    return df_clean


def remove_outliers(df: pd.DataFrame, columns: list = None, method: str = "iqr") -> pd.DataFrame:
    """
    Remove outliers from specified columns.
    
    Args:
        df: Input DataFrame
        columns: List of columns to check for outliers
        method: 'iqr' or 'zscore'
        
    Returns:
        pd.DataFrame: DataFrame with outliers removed
    """
    df_clean = df.copy()
    
    if columns is None:
        columns = df_clean.select_dtypes(include=[np.number]).columns
    
    if method == "iqr":
        for col in columns:
            Q1 = df_clean[col].quantile(0.25)
            Q3 = df_clean[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df_clean = df_clean[(df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)]
    
    return df_clean


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names to lowercase with underscores.
    
    Args:
        df: Input DataFrame
        
    Returns:
        pd.DataFrame: DataFrame with standardized column names
    """
    df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace("-", "_")
    return df


def convert_data_types(df: pd.DataFrame, dtype_map: dict = None) -> pd.DataFrame:
    """
    Convert data types in DataFrame.
    
    Args:
        df: Input DataFrame
        dtype_map: Dictionary mapping column names to desired data types
        
    Returns:
        pd.DataFrame: DataFrame with converted data types
    """
    df_clean = df.copy()
    
    if dtype_map:
        for col, dtype in dtype_map.items():
            if col in df_clean.columns:
                try:
                    df_clean[col] = df_clean[col].astype(dtype)
                except Exception as e:
                    print(f"Error converting {col} to {dtype}: {e}")
    
    return df_clean
