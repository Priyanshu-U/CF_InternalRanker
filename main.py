import streamlit as st
import os
import pandas as pd
import forcesApi


# Function to export or append data to CSV
def export_or_append_csv(data, filename):
    if os.path.exists(filename):
        existing_data = pd.read_csv(filename)
        updated_data = pd.concat([existing_data, data], ignore_index=True)
        updated_data.to_csv(filename, index=False)
        st.success("Data appended to existing CSV.")
    else:
        data.to_csv(filename, index=False)
        st.success("Data exported to new CSV.")


# Streamlit app
st.title("Chose the contest to produce the rank list: ")

# Dropdown to select ID
selected_id = st.selectbox("Select ID", list(forcesApi.cid_data.keys()))

# Display the selected DataFrame
st.write("Selected DataFrame:")
st.dataframe(forcesApi.cid_data[selected_id])

if st.button("Export DataFrame"):
    selected_df = forcesApi.cid_data[selected_id]
    filename = f"contest_{selected_id}_rankList.csv"
    export_or_append_csv(selected_df, filename)
    st.download_button(
        label="Download CSV file",
        data=selected_df.to_csv(index=False).encode(),
        file_name=filename,
        mime="text/csv"
    )