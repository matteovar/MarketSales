import streamlit as st
import pandas as pd
import plotly.express as px


def scatter_chart1(df: pd.DataFrame, x: str, y: str, color = None, hover_name = None,size = None, title: str = "Gráfico"):
    scatter_chart_view = px.scatter(data_frame=df, x=x, y=y, color=color, hover_name=hover_name,size=size, title=title)
    st.plotly_chart(scatter_chart_view)