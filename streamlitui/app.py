import os
import pandas as pd
cwd = os.getcwd()
# sys.path.append("./scripts")


import streamlit as st


st.set_page_config(page_title="Telecom Analytics", layout="wide")

# st.sidebar.markdown("Please select the desired page")

st.markdown("""

    ## TelCo Telecom Data Analysis
    > The week 1 challenge of [10Academy](https://www.10academy.org/) is to provide a report to analyse opportunities for growth and make a recommendation on whether TellCo is worth buying or selling.  This is done by analysing a telecommunication dataset that contains useful information about the customers & their activities on the network. It is required to deliver insights via web based dashboard and a written report.
    ## Data
    - The data extracted from a month of aggregated data on xDR. 
    - The features described can be found below
""")

df=pd.read_csv(f"{cwd}/streamlitui/asset/st.csv")
st.write(df)

st.markdown("""

    I am *[Naol Lamesa]* I have performed the following tasks in this challenge
    - User Overview analysis
    - User Engagement analysis
    - Experience Analytics
    - Satisfaction Analysis
""")