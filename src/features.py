"""
Feature Engineering Module
Handles creation and transformation of features for analysis.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def create_time_features(df: pd.DataFrame, date_column: str) -> pd.DataFrame:
    """
    Create time-based features from a date column.
    
    Args:
        df: Input DataFrame
        date_column: Name of the date column
        
    Returns:
        pd.DataFrame: DataFrame with new time features
    """
    df_features = df.copy()
    
    if date_column in df_features.columns:
        df_features[date_column] = pd.to_datetime(df_features[date_column])
        
        df_features['year'] = df_features[date_column].dt.year
        df_features['month'] = df_features[date_column].dt.month
        df_features['day'] = df_features[date_column].dt.day
        df_features['quarter'] = df_features[date_column].dt.quarter
        df_features['day_of_week'] = df_features[date_column].dt.dayofweek
        df_features['week_of_year'] = df_features[date_column].dt.isocalendar().week
    
    return df_features


def create_rolling_statistics(df: pd.DataFrame, column: str, window: int = 7) -> pd.DataFrame:
    """
    Create rolling statistics for a given column.
    
    Args:
        df: Input DataFrame
        column: Column name to calculate rolling statistics
        window: Window size for rolling calculation
        
    Returns:
        pd.DataFrame: DataFrame with rolling statistics
    """
    df_features = df.copy()
    
    if column in df_features.columns:
        df_features[f'{column}_rolling_mean'] = df_features[column].rolling(window=window).mean()
        df_features[f'{column}_rolling_std'] = df_features[column].rolling(window=window).std()
        df_features[f'{column}_rolling_sum'] = df_features[column].rolling(window=window).sum()
    
    return df_features


def create_percentage_change(df: pd.DataFrame, column: str, periods: int = 1) -> pd.DataFrame:
    """
    Create percentage change features.
    
    Args:
        df: Input DataFrame
        column: Column name to calculate percentage change
        periods: Number of periods for percentage change calculation
        
    Returns:
        pd.DataFrame: DataFrame with percentage change features
    """
    df_features = df.copy()
    
    if column in df_features.columns:
        df_features[f'{column}_pct_change'] = df_features[column].pct_change(periods=periods) * 100
    
    return df_features


def create_binned_features(df: pd.DataFrame, column: str, bins: int = 5, labels: list = None) -> pd.DataFrame:
    """
    Create binned categorical features from continuous variables.
    
    Args:
        df: Input DataFrame
        column: Column name to bin
        bins: Number of bins
        labels: Custom labels for bins
        
    Returns:
        pd.DataFrame: DataFrame with binned features
    """
    df_features = df.copy()
    
    if column in df_features.columns:
        df_features[f'{column}_binned'] = pd.cut(df_features[column], bins=bins, labels=labels)
    
    return df_features


def normalize_column(df: pd.DataFrame, column: str, method: str = 'minmax') -> pd.DataFrame:
    """
    Normalize a column using different methods.
    
    Args:
        df: Input DataFrame
        column: Column name to normalize
        method: 'minmax' or 'zscore'
        
    Returns:
        pd.DataFrame: DataFrame with normalized column
    """
    df_features = df.copy()
    
    if column in df_features.columns:
        if method == 'minmax':
            min_val = df_features[column].min()
            max_val = df_features[column].max()
            df_features[f'{column}_normalized'] = (df_features[column] - min_val) / (max_val - min_val)
        elif method == 'zscore':
            mean_val = df_features[column].mean()
            std_val = df_features[column].std()
            df_features[f'{column}_normalized'] = (df_features[column] - mean_val) / std_val
    
    return df_features
