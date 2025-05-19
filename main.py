import streamlit as sl
import pandas as pd

sl.title("Passenger Analysis")


df=pd.read_csv("cleanedData.csv")
with sl.expander("Data Preview"):
    sl.dataframe(df)
    df,
    column_config={
        ""
    }

