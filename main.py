import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

def load_data():
    df= pd.read_csv("cleanedData.csv")
    return df
df=load_data()
st.set_page_config(page_title="Passenger Survival Dashboard",layout="wide")

st.title("🚢 Passenger Survival Dashboard")
st.markdown("An interactive dashboard to explore survival trends in the Titanic dataset.")

st.sidebar.header("Filter Data")
selected_class = st.sidebar.multiselect("Select Passenger Class ",options=df['Pclass'].unique(),default=df['Pclass'].unique())
selected_sex = st.sidebar.multiselect("Select Gender", options=df['Sex'].unique(), default=df['Sex'].unique())

filtered_df = df[(df['Pclass'].isin(selected_class)) & (df['Sex'].isin(selected_sex))]

#kpi
total_passengers = len(df)
survived_passengers = df[df['Survived'] == 1].shape[0]
survival_rate =(survived_passengers/total_passengers)*100
avg_age = df['Age'].mean()
avg_fare = df['Fare'].mean()

st.title("KPI")
col1,col2,col3,col4= st.columns(4)

with col1:
    st.metric("Total Passengers",f"{total_passengers}")
with col2:
    st.metric("Survival Rate",f"{survival_rate:.2f}%")
with col3:
    st.metric("Avg Fare",f"{avg_age:.2f}%")
with col4:
    st.metric("Avg age",f"{avg_age:.2f}%")   
           
    

#Display


# Layout in two columns
col1, col2 = st.columns(2)

# 📊 1. Survival Count Bar Chart
with col1:
    st.subheader("1️⃣ Survival Count")
    survival_count = filtered_df['Survived'].value_counts().rename(index={0: 'Not Survived', 1: 'Survived'})
    st.bar_chart(survival_count)

# 📊 2. Age Distribution Histogram
with col2:
    st.subheader("2️⃣ Age Distribution by Survival")
    fig1, ax1 = plt.subplots()
    sns.histplot(data=filtered_df, x='Age', hue='Survived', multiple='stack', bins=20, palette='pastel', ax=ax1)
    st.pyplot(fig1)

# 📊 3. Gender Distribution Pie Chart
with col1:
    st.subheader("3️⃣ Gender Distribution")
    gender_count = filtered_df['Sex'].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(gender_count, labels=gender_count.index, autopct='%1.1f%%', colors=['#66b3ff', '#ff9999'])
    ax2.axis('equal')
    st.pyplot(fig2)



# 📊 4. Survival Rate by Passenger Class
with col2:
    st.subheader("4️⃣ Survival Rate by Passenger Class")
    class_survival = filtered_df.groupby('Pclass')['Survived'].mean()
    fig3, ax3 = plt.subplots()
    sns.barplot(x=class_survival.index, y=class_survival.values, palette='Blues_d', ax=ax3)
    ax3.set_ylabel("Survival Rate")
    ax3.set_xlabel("Passenger Class")
    st.pyplot(fig3)