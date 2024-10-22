import streamlit as st
st.title("Supply chain Analysis")
power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=d07e5234-4b92-46c0-91b1-a17a91770fa9&autoAuth=true&ctid=a5f26ada-3efd-4be5-853c-0a0b5f301a25"  # Replace with your report URL
st.components.v1.iframe(power_bi_url, width=1000, height=600)