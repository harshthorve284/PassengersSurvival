import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as pllt

def load_data():
    pd.read_csv("C:/PassengersSurvival/cleanedData.csv")
    return df
df = load_data()

st.title('Passenger Survival Dashboard')