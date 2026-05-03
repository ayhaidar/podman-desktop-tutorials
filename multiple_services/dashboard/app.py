import streamlit as st
import pandas as pd
import os
import time

st.set_page_config(page_title="Corporate Data Dashboard", layout="wide")

# The internal path we mapped in the Dockerfile
DATA_FILE = "/app/dashboard_data/data.csv"

st.title("📊 Real-time SQL Data")

def load_data():
    if os.path.exists(DATA_FILE):
        # Get the last modified time for the 'Last Updated' footer
        mtime = os.path.getmtime(DATA_FILE)
        last_updated = time.ctime(mtime)
        return pd.read_csv(DATA_FILE), last_updated
    return None, None

df, updated_at = load_data()

if df is not None:
    st.metric("Last Updated", updated_at)
    st.dataframe(df, use_container_width=True)
    
    # Optional: Add a button to trigger a rerun of the UI
    if st.button('Refresh View'):
        st.rerun()
else:
    st.error(f"Waiting for data... (Looking for {DATA_FILE})")
    st.info("The Data Puller might still be connecting to the database.")
