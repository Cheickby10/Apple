import streamlit as st
from ui.dashboard import show_dashboard

st.set_page_config(page_title="Bet Analytics Pro", layout="wide")

st.title("📊 Bet Analytics Pro")

show_dashboard()
