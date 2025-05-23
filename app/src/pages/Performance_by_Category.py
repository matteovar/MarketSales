import pandas as pd
import streamlit as st
from src.main import df, get_group_agg
from src.utils.plotly_charts.line_chart import line_chart1


def show_hello():
    st.title("Performance by Product Category")

    df_rec_cat = get_group_agg(
        df=df,
        group_col=["ProductID", "ProductCategory"],
        agg_col="FinalSalePrice",
        agg_type="sum",
    )

    option = st.selectbox(
        "Select a box", options=df_rec_cat["ProductCategory"].unique()
    )

    filtered_df = df_rec_cat[df_rec_cat["ProductCategory"] == option]

    line_chart1(
        df=filtered_df,
        x="ProductID",
        y="FinalSalePrice",
        title="Revenue by product category",
        x_label="Product",
        y_label="Final Price",
    )
