import streamlit as st
st.title("Employee Performance and Attrition Analysis")
power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=d4b99a30-da9a-422e-8451-97b579322320&autoAuth=true&ctid=a5f26ada-3efd-4be5-853c-0a0b5f301a25"  # Replace with your report URL
st.components.v1.iframe(power_bi_url, width=1000, height=600)