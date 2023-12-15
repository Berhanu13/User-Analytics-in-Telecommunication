import os
import pandas as pd
import streamlit as st
import pickle
import matplotlib.pyplot as plt

cwd = os.getcwd()

# @st.experimental_memo
def load_data(DATA_URL):
    
    data = pickle.read_pickle(open(DATA_URL, "rb"))
    return data

st.set_page_config(page_title="User Engagement Analysis", page_icon="👤", layout="wide")

# st.sidebar.header("Please select the desired page")

st.markdown("## User Engagement")
st.markdown("### In this task, each users' engagement was studied")
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


df1=pd.DataFrame(data['top_ten_per_traffic'])
df2=pd.DataFrame(data['top_ten_per_freq'])
df3=pd.DataFrame(data['top_ten_per_duration'])

idx = df1.index.intersection(df2.index)

df1=df1.loc[idx,:]

idx = df1.index.intersection(df3.index)

df1=df1.loc[idx,:]

st.markdown("### Top customers who made it to the top 10 rank by all engagement metrics")

st.table(df1)
# st.write(data.keys())