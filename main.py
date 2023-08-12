import forcesApi
import streamlit as st
import os
import pandas as pd

# Streamlit app
st.title("Chose the contest to produce the rank list: ")

# Dropdown to select ID
selected_id = st.selectbox("Select ID", list(forcesApi.cid_data.keys()))

# Display the selected DataFrame
st.write("Selected DataFrame:")
st.dataframe(forcesApi.cid_data[selected_id])

# Export button
if st.button("Export DataFrame"):
    selected_df = forcesApi.cid_data[selected_id]
    downloads_path = os.path.expanduser("~") + "/Downloads"
    st.write(downloads_path)
    filename = os.path.join(downloads_path, f"{selected_id}_export.csv")
    selected_df.to_csv(filename, index=False)
    st.success(f"DataFrame exported as '{filename}'")

