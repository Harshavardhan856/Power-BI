import streamlit as st
st.title("Sales Insights Analysis")
power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=a0db98d6-9cf2-4960-8937-a5661b21f1f4&autoAuth=true&ctid=a5f26ada-3efd-4be5-853c-0a0b5f301a25"  # Replace with your report URL
st.components.v1.iframe(power_bi_url, width=1000, height=600)
