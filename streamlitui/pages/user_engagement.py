import os
import pandas as pd
import streamlit as st
import pickle

cwd = os.getcwd()

@st.cache
def load_data(DATA_URL):
    data = pickle.load(open(DATA_URL, "rb"))
    return data

st.set_page_config(page_title="User Engagement Analysis", page_icon="👤", layout="wide")

st.markdown("## User Engagement")
st.markdown("### In this task, each user's engagement was studied")
st.markdown("""
- Top ten users by session traffic: which is Downloaded and Uploaded data
- Top ten users per sessions frequency
- Top ten users per duration of session
are presented below
Users are represented by *msisdn number* which is a unique customer number
# """)

st.markdown("# ")

data = load_data(f"{cwd}/data/engagement_data.pkl")

st.markdown("### Top ten customers with highest dl/ul traffic ")
st.table(data['top_ten_per_traffic'])
st.markdown("# ")

st.markdown("### Top ten customers with the most session frequency ")
st.table(data['top_ten_per_freq'])
st.markdown("# ")

st.markdown("### Top ten customers with longest session ")
st.table(data['top_ten_per_duration'])
st.markdown("# ")

# Convert dictionary values to DataFrames
df1 = pd.DataFrame.from_dict(data['top_ten_per_traffic'], orient='index')
df2 = pd.DataFrame.from_dict(data['top_ten_per_freq'], orient='index')
df3 = pd.DataFrame.from_dict(data['top_ten_per_duration'], orient='index')

# Find the common index among all DataFrames
common_index = df1.index.intersection(df2.index).intersection(df3.index)

# Filter DataFrames to keep only common index
df1 = df1.loc[common_index, :]
df2 = df2.loc[common_index, :]
df3 = df3.loc[common_index, :]

st.markdown("### Top customers who made it to the top 10 rank by all engagement metrics")
st.table(df1)
