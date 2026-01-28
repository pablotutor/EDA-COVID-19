"""
Visualization Module
Handles creation of plots and visualizations for exploratory data analysis.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def set_style(style: str = "whitegrid", palette: str = "husl") -> None:
    """
    Set the style for matplotlib and seaborn plots.
    
    Args:
        style: Seaborn style (darkgrid, whitegrid, dark, white, ticks)
        palette: Color palette (husl, Set2, pastel, muted)
    """
    sns.set_style(style)
    sns.set_palette(palette)
    plt.rcParams['figure.figsize'] = (12, 6)


def plot_distribution(df: pd.DataFrame, column: str, bins: int = 30, figsize: tuple = (10, 5)) -> None:
    """
    Plot distribution of a numerical column.
    
    Args:
        df: Input DataFrame
        column: Column name to plot
        bins: Number of bins for histogram
        figsize: Figure size
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    df[column].hist(bins=bins, ax=ax, edgecolor='black', alpha=0.7)
    ax.set_title(f'Distribution of {column}', fontsize=14, fontweight='bold')
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def plot_time_series(df: pd.DataFrame, x_col: str, y_col: str, figsize: tuple = (14, 6)) -> None:
    """
    Plot time series data.
    
    Args:
        df: Input DataFrame
        x_col: Column name for x-axis (usually date)
        y_col: Column name for y-axis
        figsize: Figure size
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.plot(df[x_col], df[y_col], linewidth=2, marker='o', markersize=4)
    ax.set_title(f'{y_col} over Time', fontsize=14, fontweight='bold')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()


def plot_correlation_matrix(df: pd.DataFrame, figsize: tuple = (10, 8)) -> None:
    """
    Plot correlation matrix heatmap.
    
    Args:
        df: Input DataFrame with numerical columns
        figsize: Figure size
    """
    numeric_df = df.select_dtypes(include=[np.number])
    correlation = numeric_df.corr()
    
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', center=0, 
                square=True, ax=ax, cbar_kws={'label': 'Correlation'})
    ax.set_title('Correlation Matrix Heatmap', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.show()


def plot_boxplot(df: pd.DataFrame, column: str, by: str = None, figsize: tuple = (10, 6)) -> None:
    """
    Plot boxplot for a numerical column.
    
    Args:
        df: Input DataFrame
        column: Column name to plot
        by: Optional column to group by
        figsize: Figure size
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    if by:
        df.boxplot(column=column, by=by, ax=ax)
        ax.set_title(f'{column} by {by}')
    else:
        ax.boxplot(df[column])
        ax.set_title(f'Boxplot of {column}', fontsize=14, fontweight='bold')
    
    ax.set_ylabel(column)
    
    plt.tight_layout()
    plt.show()


def plot_bar_chart(df: pd.DataFrame, x_col: str, y_col: str, figsize: tuple = (10, 6)) -> None:
    """
    Plot bar chart.
    
    Args:
        df: Input DataFrame
        x_col: Column name for x-axis
        y_col: Column name for y-axis
        figsize: Figure size
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    df.plot(x=x_col, y=y_col, kind='bar', ax=ax)
    ax.set_title(f'{y_col} by {x_col}', fontsize=14, fontweight='bold')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()


def plot_scatter(df: pd.DataFrame, x_col: str, y_col: str, color: str = None, figsize: tuple = (10, 6)) -> None:
    """
    Plot scatter plot.
    
    Args:
        df: Input DataFrame
        x_col: Column name for x-axis
        y_col: Column name for y-axis
        color: Optional column for color coding
        figsize: Figure size
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    if color:
        scatter = ax.scatter(df[x_col], df[y_col], c=df[color], cmap='viridis', alpha=0.6, s=50)
        plt.colorbar(scatter, ax=ax, label=color)
    else:
        ax.scatter(df[x_col], df[y_col], alpha=0.6, s=50)
    
    ax.set_title(f'{y_col} vs {x_col}', fontsize=14, fontweight='bold')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
