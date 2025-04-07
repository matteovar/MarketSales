import pandas as pd
import streamlit as st
import plotly.express as px

from src.utils.plotly_charts.bar_chart import bar_chart1
from src.utils.plotly_charts.line_chart import line_chart1
from src.main import df, get_data_agg, get_group_agg
from src.utils.cards import create_cards

def show_dashboard():
    st.title("Visão Geral")

    cols = st.columns(4)  

    with cols[0]:  
        create_cards("Valor Total", f"{get_data_agg(df=df,column_name="FinalSalePrice", agg_type="sum"):,.2f}")

    with cols[1]:  
        create_cards("Numero de Vendas", f"{get_data_agg(df=df,column_name="SalesQuantity", agg_type="sum")}")

    with cols[2]:  
        create_cards("Feedback do Cosumidor", f"{get_data_agg(df=df,column_name="CustomerFeedbackRating", agg_type="mean"):.1f}")

    with cols[3]:  
        create_cards("Taxa de retorno", f"{(get_data_agg(df=df,column_name="ReturnFlag", agg_type="sum")/1000)*100}%")

    col_chart = st.columns(2)
    
    with col_chart[0]:
        df_sales_date = get_group_agg(df=df, group_col="TransactionDate", agg_col="FinalSalePrice", agg_type="sum")
        line_chart1(df=df_sales_date, x= "TransactionDate", y="FinalSalePrice", title="Receita ao longo do tempo")
    with col_chart[1]:    
        df_fat_cat = get_group_agg(df=df, group_col="ProductCategory", agg_col="FinalSalePrice", agg_type="sum")
        bar_chart1(df = df_fat_cat, x = "ProductCategory", y= "FinalSalePrice", title="Faturamento por categoria")
        
show_dashboard()