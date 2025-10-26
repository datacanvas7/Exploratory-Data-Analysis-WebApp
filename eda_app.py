import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# WebApp Title
st.markdown('''
# **Exploratory Data Analysis WebApp**
This app is developed by Yawar Ali
''')

st.markdown('''
Welcome! Upload your dataset using the sidebar, or press the button below to use a sample dataset.
''')

# Sidebar - Upload file
with st.sidebar.header('1. Upload your dataset (.csv or .xlsx)'):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=["csv", "xlsx"])
    st.sidebar.markdown("[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)")

# Load and process uploaded file
if uploaded_file is not None:

    @st.cache_data
    def load_file(file):
        if file.name.endswith('.csv'):
            return pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            return pd.read_excel(file)
        else:
            return None

    df = load_file(uploaded_file)

    if df is not None:
        profile = ProfileReport(df, title="Profiling Report", explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Profiling Report**')
        st_profile_report(profile)
    else:
        st.error("Unsupported file format.")

elif st.button('Press to use Example Dataset'):

    @st.cache_data
    def load_example():
        return pd.DataFrame(np.random.rand(100, 5), columns=['age', 'banana', 'Codanics', 'Dutch', 'Ears'])

    df = load_example()
    profile = ProfileReport(df, title="Profiling Report", explorative=True)
    st.header('**Example Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Profiling Report**')
    st_profile_report(profile)
