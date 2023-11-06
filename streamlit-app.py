import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(worksheet="Table1", usecols=list(range(2)),max_entries=10)
st.dataframe(data)