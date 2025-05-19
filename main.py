import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

def load_data():
    df= pd.read_csv("cleanedData.csv")
    return df
df=load_data()

st.title("🚢 Passenger Survival Dashboard")
st.markdown("An interactive dashboard to explore survival trends in the Titanic dataset.")

# Sidebar
st.sidebar.header("Filter Options")

# Gender filter
gender = st.sidebar.multiselect("Select Gender", options=df['Sex'].unique(), default=df['Sex'].unique())

# Class filter
pclass = st.sidebar.multiselect("Select Passenger Class", options=df['Pclass'].unique(), default=df['Pclass'].unique())

# Age filter
age_range = st.sidebar.slider("Select Age Range", min_value=int(df['Age'].min()), max_value=int(df['Age'].max()), value=(0, 80))

# Apply filters
filtered_df = df[(df['Sex'].isin(gender)) & 
                 (df['Pclass'].isin(pclass)) & 
                 (df['Age'].between(age_range[0], age_range[1]))]

# KPI Summary
st.subheader(" Key Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Passengers", len(filtered_df))
col2.metric("Survivors", filtered_df['Survived'].sum())
col3.metric("Survival Rate", f"{filtered_df['Survived'].mean()*100:.2f}%")

# Survival by Gender
st.subheader("🧍 Survival Count by Gender")
fig_gender = px.histogram(filtered_df, x='Sex', color='Survived', barmode='group',
                          color_discrete_map={0: "red", 1: "green"},
                          labels={'Survived': 'Survived (0 = No, 1 = Yes)'})
st.plotly_chart(fig_gender)

# Survival by Class
st.subheader("🏷️ Survival Rate by Passenger Class")
fig_class = px.bar(filtered_df.groupby('Pclass')['Survived'].mean().reset_index(),
                   x='Pclass', y='Survived',
                   labels={'Survived': 'Survival Rate'},
                   color='Survived', color_continuous_scale='greens')
st.plotly_chart(fig_class)

# Age distribution
st.subheader("📈 Age Distribution")
fig_age = px.histogram(filtered_df, x='Age', nbins=30, color='Survived',
                       color_discrete_map={0: "red", 1: "green"},
                       labels={'Survived': 'Survived (0 = No, 1 = Yes)'})
st.plotly_chart(fig_age)
