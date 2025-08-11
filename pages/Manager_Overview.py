import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
service_account_info = st.secrets["gcp_service_account"]
creds = Credentials.from_service_account_info(service_account_info, scopes=scope)
client = gspread.authorize(creds)

spreadsheet = client.open("MNP Stats 25/26")
manager_tabs = spreadsheet.worksheets()[1:11]  # Skip 'Home'

selected_manager = st.sidebar.selectbox("Select Manager", [ws.title for ws in manager_tabs])

ws = spreadsheet.worksheet(selected_manager)
data = ws.get_all_values()
df = pd.DataFrame(data[1:], columns=data[0])

st.title(f"{selected_manager} Overview")
st.dataframe(df)