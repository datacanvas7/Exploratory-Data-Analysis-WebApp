import streamlit as st
import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport
from streamlit.components.v1 import html

# Set the page title
st.set_page_config(page_title="EDA Web App", layout="wide")

# Sidebar menu
menu = ["Home", "Explore Dataset"]
choice = st.sidebar.selectbox("Menu", menu)

# HOME PAGE
if choice == "Home":
    st.header("**Automated Exploratory Data Analysis (EDA)**")

    st.markdown('''
    __This EDA webapp has been created in Python by [Yawar Ali](https://github.com/datacanvas7/).__

    *Libraries used: Streamlit, Pandas, and YData-Profiling*
    ''')

    st.subheader("Exploratory Data Analysis (EDA)")

    st.markdown('''
    **Exploratory data analysis (EDA)** is a crucial step in the data analysis process that involves 
    visualization, summarization, and interpretation of data to gain insights into patterns, 
    relationships, and anomalies.

    EDA helps analysts:
    - Identify potential issues with the data  
    - Formulate hypotheses  
    - Make informed decisions about further analysis steps  

    **Common EDA Techniques:**
    - Data visualization: histograms, scatter plots, box plots, and heatmaps  
    - Descriptive statistics: mean, median, std. deviation, correlation  
    - Data transformation: normalization, scaling, standardization  
    - Data cleaning: handling missing data, outliers, and inconsistencies  

    **Use Cases:**
    - Understanding variable distributions  
    - Identifying relationships between features  
    - Detecting anomalies or outliers  
    - Testing assumptions about the data  
    - Ensuring data quality for modeling  

    Overall, EDA is a **foundation** for all reliable data analysis and machine learning workflows.
    ''')

# EXPLORE DATASET PAGE
elif choice == "Explore Dataset":
    st.title("**Explore Your Dataset**")
    st.markdown("Upload your dataset to generate an automated EDA report using **YData-Profiling**.")

    # Sidebar - Upload file
    with st.sidebar.header("1. Upload your dataset (.csv or .xlsx)"):
        uploaded_file = st.sidebar.file_uploader("Upload your file", type=["csv", "xlsx"])
        st.sidebar.markdown("[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)")

    # If user uploads a file
    if uploaded_file is not None:

        @st.cache_data
        def load_file(file):
            if file.name.endswith(".csv"):
                return pd.read_csv(file)
            elif file.name.endswith(".xlsx"):
                return pd.read_excel(file)
            else:
                return None

        df = load_file(uploaded_file)

        if df is not None:
            st.header("**Input DataFrame**")
            st.write(df)
            st.write("---")

            st.header("**Profiling Report**")
            profile = ProfileReport(df, title="Profiling Report", explorative=True)
            html(profile.to_html(), height=1000, scrolling=True)
        else:
            st.error("Unsupported file format.")

    # If no file uploaded, use a sample dataset
    elif st.button("Use Example Dataset"):

        @st.cache_data
        def load_example():
            return pd.DataFrame(
                np.random.rand(100, 5),
                columns=["age", "banana", "Codanics", "Dutch", "Ears"]
            )

        df = load_example()

        st.header("**Example Input DataFrame**")
        st.write(df)
        st.write("---")

        st.header("**Profiling Report**")
        profile = ProfileReport(df, title="Profiling Report", explorative=True)
        html(profile.to_html(), height=1000, scrolling=True)
