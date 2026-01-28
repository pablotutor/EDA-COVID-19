# COVID-19 EDA (OWID)

## Objective
Perform an exploratory data analysis to understand the evolution, impact and heterogeneity of COVID-19 across countries.

## Dataset
Source: Our World in Data  
Time span: 2020–2023  
Granularity: Country-level, daily

## Key Questions
- How did cases and deaths evolve over time?
- Are there structural differences between regions?
- How do vaccinations relate to outcomes?

## Main Insights
- ...


## Structure of the project

```
covid-owid-eda/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── 01_data_overview.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_univariate_analysis.ipynb
│   ├── 04_bivariate_analysis.ipynb
│   ├── 05_temporal_analysis.ipynb
│   ├── 06_geographical_analysis.ipynb
│   └── 07_insights_summary.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── cleaning.py
│   ├── features.py
│   └── visualization.py
│
├── figures/
│   ├── univariate/
│   ├── bivariate/
│   ├── temporal/
│   └── maps/
│
├── reports/
│   └── eda_report.md
│
└── config/
    └── config.yaml
```


