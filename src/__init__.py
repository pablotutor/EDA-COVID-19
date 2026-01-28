"""
EDA COVID-19 Analysis Package
Main package initialization for data processing and visualization modules.
"""

__version__ = "1.0.0"
__author__ = "Pablo Tutor"

from . import data_loader
from . import cleaning
from . import features
from . import visualization

__all__ = [
    "data_loader",
    "cleaning",
    "features",
    "visualization",
]
