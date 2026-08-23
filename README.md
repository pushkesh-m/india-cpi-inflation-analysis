# India CPI Inflation Analysis (2013-2023)

Interactive Streamlit dashboard exploring India's Consumer Price Index across 10 years. Pick a year range, sector, and category from the sidebar - all 7 charts update instantly.

## What's inside

Seven questions answered across tabs:

1. Overall CPI trend (2013-2023)
2. Which category rose the most
3. Food vs Fuel during COVID (2019-2021)
4. Rural vs Urban comparison
5. Seasonal patterns by month
6. Food and Fuel correlation
7. Biggest single-year spike

## Run it locally

```bash
pip install streamlit pandas matplotlib seaborn
streamlit run app.py
```

## Data

All India Consumer Price Index dataset from Kaggle (MOSPI). Covers Rural, Urban, and combined figures across 8 categories from 2013 to 2023.

Two cleaning issues in the raw data - a typo ('Marcrh' for March) and trailing whitespace on November. Fixed before any analysis runs.

## Stack

Python, Pandas, Matplotlib, Streamlit

## Author

Pushkesh Mital | [GitHub](https://github.com/pushkesh-m) | [LinkedIn](https://www.linkedin.com/in/pushkesh-mital)
