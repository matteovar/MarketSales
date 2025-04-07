import pandas as pd
import streamlit as st

from src.main import df
from src.utils.plotly_charts.pie_chart import pie_chart1
from src.utils.plotly_charts.bar_chart import bar_chart1
from src.main import get_group_agg


def show_cli():
    
    cols = st.columns(2)
    with cols[0]:
        df_gender = df["CustomerGender"].value_counts().reset_index()
        df_gender.columns = ["CustomerGender", "count"]
        pie_chart1(df=df_gender, values="count", names="CustomerGender", title="Genero dos Clientes")
    with cols[1]:
        
        df_sales_gender = get_group_agg(df=df, group_col="CustomerAge", agg_col="FinalSalePrice", agg_type="sum")
        bar_chart1(df=df_sales_gender, x="CustomerAge", y="FinalSalePrice",title="Receita por faixa etária.",orientation='v')
        
        
show_cli()