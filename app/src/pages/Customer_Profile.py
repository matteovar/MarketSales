import pandas as pd
import streamlit as st

from src.main import df
from src.utils.plotly_charts.pie_chart import pie_chart1
from src.utils.plotly_charts.bar_chart import bar_chart1
from src.main import get_group_agg


def show_cli():

    st.title("Costumer Profile")

    cols = st.columns(2)
    with cols[0]:
        df_gender = df["CustomerGender"].value_counts().reset_index()
        df_gender.columns = ["CustomerGender", "count"]
        pie_chart1(
            df=df_gender,
            values="count",
            names="CustomerGender",
            title="Customer by Gender",
            names_label="Gender",
            values_label="Amount"
        )
    with cols[1]:

        df_sales_gender = get_group_agg(
            df=df, group_col="CustomerAge", agg_col="FinalSalePrice", agg_type="sum"
        )
        bar_chart1(
            df=df_sales_gender,
            x="CustomerAge",
            y="FinalSalePrice",
            title="Revenue by Age",
            orientation="v",
            x_label="Age",
            y_label="Final Price",
        )

    df_region_sales = get_group_agg(
        df=df, group_col="Region", agg_col="FinalSalePrice", agg_type="sum"
    )
    bar_chart1(
        df=df_region_sales,
        x="Region",
        y="FinalSalePrice",
        title="Revenue by Geographic Location",
        y_label="Final Price"
    )


show_cli()
