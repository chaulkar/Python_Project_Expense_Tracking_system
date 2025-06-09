import pandas as pd
import streamlit as st
from datetime import date
import requests

API_URL = "http://127.0.0.1:9000"

def analytics_by_category_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("start_date")

    with col2:
        end_date = st.date_input("end_date")

    if st.button(label="Get Analytics", key="button_1"):
        payload={
            "start_date": str(start_date),
            "end_date": str(end_date)
        }
        response = requests.post(f"{API_URL}/analytics",json=payload)
        response = response.json()

        data={
            "category": list(response.keys()),
            "total": [response[category]["total"] for category in response],
            "percentage": [response[category]["percentage"] for category in response]
        }

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="percentage", ascending= False)
        df_sorted["percentage"] = df_sorted["percentage"].round(2)


        st.header("Expense Breakdown By Category")

        st.bar_chart(data=df_sorted.set_index("category")["percentage"], use_container_width=True)
        df_sorted["total"] = df_sorted["total"].map("{:.2f}".format)
        df_sorted["percentage"] = df_sorted["percentage"].map("{:.2f}%".format)

        st.table(df_sorted)