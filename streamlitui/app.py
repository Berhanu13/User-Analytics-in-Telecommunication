import os
import pandas as pd
import streamlit as st

cwd = os.getcwd()

st.set_page_config(page_title="Telecom Analytics", layout="wide")

# Specify the image path
image_path = f"{cwd}/images/10acc.png"

# Set the desired height for the image
image_height = 200

# Display the image within a Markdown block with specified height
st.markdown(f"![10 Academy]({image_path}){{height={image_height}}}")

st.markdown("""

    ## User Analytics in the Telecommunication Industry
    > The investor, who's good at finding valuable deals, wants to check out TellCo, a mobile company in Pefkakia. I am diving into TellCo's data to see if it's a good buy or not. I am focusing on the info the company's machines automatically collect. The goal is to find chances for growth and figure out if it's a smart move to buy or sell TellCo. I am going to use what I learn from a bunch of telecom data to make decisions that fit the changing telecom world. This report keeps it simple while I dig into the numbers to see what makes sense for the investor.
    ## Data
    > For this project, I used data from a monthly aggregation of xDR records. I obtained a data dump, which was then loaded into a Postgres database. The dataset comprises 55 columns and 15,001 rows.
""")

df = pd.read_csv(f"{cwd}/streamlitui/asset/st.csv")
st.write(df)

st.markdown("""

    I am *[Naol Lamesa]* I have performed the following tasks in this challenge
    - User Overview analysis
    - User Engagement analysis
    - Experience Analytics
    - Satisfaction Analysis
""")
