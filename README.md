# India CPI Inflation Analysis (2013-2023)

An interactive Streamlit dashboard exploring India's Consumer Price Index across a decade. Filter by year range, sector, and category from the sidebar - all charts update instantly.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://india-cpi-inflation-analysis.streamlit.app/)

---

## What's Inside

Seven analysis questions, each with its own tab:

| Tab | Question |
|---|---|
| Trend | How has overall CPI moved from 2013 to 2023? |
| Category Rise | Which category increased the most over the decade? |
| COVID Impact | How did Food and Fuel behave during 2019-2021? |
| Rural vs Urban | Where is inflation hitting harder? |
| Seasonality | Which months consistently see higher CPI? |
| Correlation | How closely do Food and Fuel move together? |
| YoY Spike | Which year saw the biggest single-year jump? |

---

## Run Locally

```bash
git clone https://github.com/pushkesh-m/india-cpi-inflation-analysis.git
cd india-cpi-inflation-analysis
pip install -r requirements.txt
streamlit run app.py
```

---

## Data

**Source:** All India Consumer Price Index - MOSPI via Kaggle

Covers Rural, Urban, and combined figures across 8 categories (Food and Beverages, Fuel and Light, Clothing, Health, Education, Transport, Vegetables, Cereals) from January 2013 to December 2023.

Two issues fixed before analysis runs - a typo (`Marcrh` for March) and trailing whitespace on month names.

---

## Stack

- [Streamlit](https://streamlit.io/) - app framework
- [Pandas](https://pandas.pydata.org/) - data manipulation
- [Matplotlib](https://matplotlib.org/) + [Seaborn](https://seaborn.pydata.org/) - charts

---

**GitHub:** [pushkesh-m](https://github.com/pushkesh-m) | **LinkedIn:** [Pushkesh Maheshwari](https://www.linkedin.com/in/pushkesh-mital)
