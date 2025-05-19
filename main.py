import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    df= pd.read_csv("cleanedData.csv")
    return df
df=load_data()

st.title("🚢 Passenger Survival Dashboard")