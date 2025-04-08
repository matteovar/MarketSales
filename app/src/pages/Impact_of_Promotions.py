import pandas as pd
import streamlit as st

from src.utils.plotly_charts.bar_chart import bar_chart1
from src.utils.plotly_charts.scatter_chart import scatter_chart1
from src.main import df, disc_sales, get_group_agg

def show_dic():
    st.title("Impact of Promotions")
    
    cols = st.columns(2)
    with cols[0]:
        df_sales_disc_prod = get_group_agg(df=df, group_col="ProductCategory", agg_col=["SalesPrice", "FinalSalePrice"], agg_type="sum")
        bar_chart1(df_sales_disc_prod, x="ProductCategory",y="FinalSalePrice",title= "Price without discount and with discount by category",color = "SalesPrice")
    with cols[1]:
        df_disc_sales = disc_sales(df)
        
        scatter_chart1(
            df_disc_sales,
            x="DiscountPercentage",
            y="FinalSalePrice",
            title="Descount x Final Price",
            hover_name="ProductID",
            color="ProductCategory"
        )
    st.dataframe(get_group_agg(df=df, group_col="ProductCategory",agg_col="DiscountAmount", agg_type="mean").sort_values("DiscountAmount", ascending=False), hide_index= True)

show_dic()
