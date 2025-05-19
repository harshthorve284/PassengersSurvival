# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Passenger Survival Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("cleanedData.csv")

df = load_data()

# Title
st.title("🚢 Passenger Survival Dashboard")

# Sidebar Filters
st.sidebar.header("Filter Options")
sex_filter = st.sidebar.multiselect("Select Gender", options=df["Sex"].unique(), default=df["Sex"].unique())
pclass_filter = st.sidebar.multiselect("Select Class", options=sorted(df["Pclass"].unique()), default=sorted(df["Pclass"].unique()))
embarked_filter = st.sidebar.multiselect("Embarked From", options=df["Embarked"].dropna().unique(), default=df["Embarked"].dropna().unique())

# Apply filters
filtered_df = df[
    (df["Sex"].isin(sex_filter)) &
    (df["Pclass"].isin(pclass_filter)) &
    (df["Embarked"].isin(embarked_filter))
]

# KPIs
total_passengers = filtered_df.shape[0]
survival_rate = filtered_df["Survived"].mean() * 100
avg_age = filtered_df["Age"].mean()
avg_fare = filtered_df["Fare"].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Passengers", total_passengers)
col2.metric("Survival Rate", f"{survival_rate:.2f}%")
col3.metric("Avg Age", f"{avg_age:.2f}")
col4.metric("Avg Fare", f"${avg_fare:.2f}")

# Charts
st.subheader("🎯 Survival Distribution")
fig1 = px.pie(filtered_df, names='Survived', title='Survived vs Not Survived',
              labels={0: 'Not Survived', 1: 'Survived'})
st.plotly_chart(fig1, use_container_width=True)

st.subheader("📊 Survival Count by Sex and Class")
fig2 = px.histogram(filtered_df, x="Sex", color="Survived", barmode="group", facet_col="Pclass",
                    category_orders={"Survived": [0, 1]}, labels={"Survived": "Survival"})
st.plotly_chart(fig2, use_container_width=True)

st.subheader("📈 Age Distribution")
fig3 = px.histogram(filtered_df, x="Age", nbins=30, title="Age Distribution")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("💵 Fare by Passenger Class")
fig4 = px.box(filtered_df, x="Pclass", y="Fare", color="Pclass", title="Fare by Class")
st.plotly_chart(fig4, use_container_width=True)

st.markdown("Data Source: Titanic Dataset")

