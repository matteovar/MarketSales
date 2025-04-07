import pandas as pd
import streamlit as st

from src.utils.plotly_charts.bar_chart import bar_chart1
from src.utils.plotly_charts.scatter_chart import scatter_chart1
from src.main import df, sales_disc_prod, disc_sales, disc_cat

def show_dic():
    st.title("Impacto de Promoções e Descontos")
    
    cols = st.columns(2)
    with cols[0]:
        df_sales_disc_prod = sales_disc_prod(df)
        
        bar_chart1(df_sales_disc_prod, x="ProductCategory",y="FinalSalePrice",title= "Preco sem desconto e com desconto por categoria",color = "SalesPrice")
    with cols[1]:
        df_disc_sales = disc_sales(df)
        
        scatter_chart1(df_disc_sales, x = "DiscountPercentage", y = "FinalSalePrice", title="Vendas com promocao x sem promocao", hover_name = "ProductID",color="ProductCategory")

    st.dataframe(disc_cat(df), hide_index= True)

show_dic()
