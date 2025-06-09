import pandas as pd
import streamlit as st
from datetime import datetime
import requests


API_URL = "http://127.0.0.1:9000"

def analytics_by_months_tab():
    years = list(range(2024, datetime.now().year + 1))
    expense_year = st.selectbox(label="Select Year", options=years[::-1])

    if st.button(label="Get Analytics", key= "button_2"):
        response = requests.get(f"{API_URL}/analytics/months/{expense_year}")
        summary = response.json()

        data = {
            "Month": [row["month_name"] for row in summary],
            "Total": [row["total"] for row in summary]
        }

        df = pd.DataFrame(data)
        df["Total"] = df["Total"].round(2)

        st.header("Expense Breakdown By Months")

        st.bar_chart(df.set_index("Month")["Total"], use_container_width=True)

        df["Total"] = df["Total"].map("{:.2f}".format)
        st.table(df)

