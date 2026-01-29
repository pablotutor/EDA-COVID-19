# COVID-19 EDA (OWID)

## Objective
Perform an exploratory data analysis to understand the evolution, impact and heterogeneity of COVID-19 across countries.

## Dataset
Source: Our World in Data  
Time span: 2020–2023  
Granularity: Country-level, daily

## Key Questions
In this EDA, we explore the COVID-19 pandemic using data from Our World in Data (OWID). 
We aim to understand temporal evolution, regional differences, the impact of vaccinations, 
economic factors, and policy measures.

- **How did cases and deaths evolve over time?**  
  We analyze how the pandemic developed and detect peaks.

- **Are there structural differences between regions?**  
  Understand how distinct continents/regions were affected.

- **How do vaccinations relate to outcomes?**  
  Measure whether vaccination had an immediate effect on cases and deaths.

- **Wealth relationships**  
  Did richer countries (GDP or other indicators) influence pandemic management?

- **Country clustering**  
  Identify clusters of countries with similar behaviors during the pandemic.

- **Relative severity**  
  How severe was COVID in each country relative to population? Not global scores.

- **Spread velocity and peaks**  
  Identify which countries experienced the fastest spikes in cases or deaths.

- **Stricter containment measures**  
  Evaluate if control policies (lockdowns, restrictions) were effective.


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


