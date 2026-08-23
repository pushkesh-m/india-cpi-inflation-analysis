import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\Pushk\Desktop\COURSES\PROJECTS\STREAMLIT\india-CPI-inflation-analysis\All India Consumer Price Index.csv")
    df['Month'] = df['Month'].str.replace('Marcrh', 'March')
    df['Month'] = df['Month'].str.strip()
    return df

df = load_data()

# Title 
st.title("India CPI Inflation Analysis")
st.subheader("2013 - 2023 | Consumer Price Index Dashboard")

# Sidebar Filters 
st.sidebar.title("Filters")

year_range = st.sidebar.slider("Select Year Range", min_value=2013, max_value=2023, value=(2013, 2023))

sector_range = st.sidebar.selectbox("Select Sector", ["All", "Rural", "Urban"])

category_range = st.sidebar.selectbox("Select Category", [
    'Food and beverages',
    'Fuel and light',
    'Clothing and footwear',
    'Health',
    'Education',
    'Transport and communication',
    'Vegetables',
    'Cereals and products'
])

# Apply Filters
df_filtered = df[df['Year'].between(year_range[0], year_range[1])]

if sector_range != "All":
    df_filtered = df_filtered[df_filtered['Sector'] == sector_range]

# Metrics Row 
yearly_avg = df_filtered.groupby('Year')['General index'].mean()
yoy_change = yearly_avg.diff()

peak_year = int(yoy_change.idxmax())
avg_cpi = round(df_filtered['General index'].mean(), 2)

categories = [
    'Food and beverages', 'Fuel and light', 'Clothing and footwear',
    'Health', 'Education', 'Transport and communication',
    'Vegetables', 'Cereals and products'
]
start = df_filtered[df_filtered['Year'] == df_filtered['Year'].min()][categories].mean()
end = df_filtered[df_filtered['Year'] == df_filtered['Year'].max()][categories].mean()
rise = end - start
top_category = rise.idxmax()

col1, col2, col3 = st.columns(3)
col1.metric("Peak Inflation Year", peak_year)
col2.metric("Avg CPI (Selected Range)", avg_cpi)
col3.metric("Highest Rising Category", top_category)

# Tabs 
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Trend", "Category Rise", "COVID Impact",
    "Rural vs Urban", "Seasonality", "Correlation",
    "YoY Spike", "About"
])

# Q1 - Overall CPI trend
with tab1:
    st.subheader("Overall CPI Inflation Trend")
    fig, ax = plt.subplots()
    ax.plot(df_filtered['Year'], df_filtered['General index'])
    ax.set_xlabel("Year")
    ax.set_ylabel("CPI Index")
    ax.set_title("India CPI Inflation Trend")
    st.pyplot(fig)
    st.info("CPI has shown a consistent upward trend from 2013 to 2023.")

# Q2 - Category-wise rise
with tab2:
    st.subheader("Category-wise CPI Rise")
    fig, ax = plt.subplots()
    rise.plot(kind='bar', ax=ax)
    ax.set_title("Category-wise CPI Rise")
    ax.set_ylabel("Rise in Index")
    st.pyplot(fig)
    st.success(f"Highest rising category: {top_category}")

# Q3 - COVID Food vs Fuel
with tab3:
    st.subheader("Food vs Fuel during COVID (2019-2021)")
    covid = df_filtered[(df_filtered['Year'] >= 2019) & (df_filtered['Year'] <= 2021)]
    fig, ax = plt.subplots()
    ax.plot(covid['Year'], covid['Food and beverages'], label='Food')
    ax.plot(covid['Year'], covid['Fuel and light'], label='Fuel')
    ax.set_xlabel("Year")
    ax.set_ylabel("CPI Index")
    ax.set_title("Food vs Fuel during COVID (2019-2021)")
    ax.legend()
    st.pyplot(fig)
    st.info("Food inflation spiked sharply in 2020 due to supply chain disruptions.")

# Q4 - Rural vs Urban
with tab4:
    st.subheader("Rural vs Urban CPI Comparison")
    rural_urban = df_filtered[df_filtered['Sector'].isin(['Rural', 'Urban'])].copy()
    compare_cols = ['Food and beverages', 'Fuel and light', 'Health', 'Education', 'General index']
    avg_by_sector = rural_urban.groupby('Sector')[compare_cols].mean()
    fig, ax = plt.subplots()
    avg_by_sector.T.plot(kind='bar', ax=ax)
    ax.set_xlabel("Category")
    ax.set_ylabel("Average CPI")
    ax.set_title("Rural vs Urban CPI Comparison")
    ax.legend(title="Sector")
    st.pyplot(fig)

# Q5 - Seasonal pattern
with tab5:
    st.subheader("Seasonal Pattern by Month")
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    avg_month = df_filtered.groupby('Month')['General index'].mean()
    avg_month = avg_month.reindex(month_order)
    fig, ax = plt.subplots()
    ax.plot(avg_month.index, avg_month.values)
    ax.set_xlabel("Month")
    ax.set_ylabel("Average CPI")
    ax.set_title("Seasonal Pattern by Month")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Q6 - Correlation
with tab6:
    st.subheader("Food vs Fuel Correlation")
    correlation = df_filtered['Food and beverages'].corr(df_filtered['Fuel and light'])
    fig, ax = plt.subplots()
    ax.scatter(df_filtered['Food and beverages'], df_filtered['Fuel and light'])
    text_str = f"Correlation (r) = {correlation:.2f}"
    ax.text(0.05, 0.95, text_str, transform=ax.transAxes)
    ax.set_xlabel("Food and Beverages CPI")
    ax.set_ylabel("Fuel and Light CPI")
    ax.set_title("Food vs Fuel Correlation")
    st.pyplot(fig)
    st.info(f"Correlation between Food and Fuel: {correlation:.2f}")

# Q7 - YoY Spike
with tab7:
    st.subheader("Biggest Single Year CPI Spike")
    fig, ax = plt.subplots()
    ax.bar(yoy_change.index, yoy_change.values)
    ax.set_xlabel("Year")
    ax.set_ylabel("CPI Change from Previous Year")
    ax.set_title("Year on Year CPI Spike")
    st.pyplot(fig)
    st.success(f"Biggest spike was in {peak_year} with a rise of {yoy_change.max():.2f} points")

# About
with tab8:
    st.subheader("About This Project")
    st.write("""
    This dashboard analyses India's Consumer Price Index (CPI) from 2013 to 2023.

    **Data Source:** All India Consumer Price Index dataset from Kaggle

    **Built with:** Python, Pandas, Matplotlib, Streamlit

    **Author:** Pushkesh
    """)
    with st.expander("Data Cleaning Steps"):
        st.write("""
        - Fixed typo: 'Marcrh' corrected to 'March'
        - Stripped trailing whitespace from Month column
        - Applied @st.cache_data for faster load times
        """)
    with st.expander("View Raw Data"):
        st.dataframe(df_filtered)
