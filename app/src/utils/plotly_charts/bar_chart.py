import streamlit as st
import pandas as pd
import plotly.express as px

def bar_chart1(df: pd.DataFrame, x: str, y: str, title: str = "Gráfico",color = None, orientation="v"):
    bar_chart_view = px.bar(data_frame = df, x=x, y=y, title=title, color= color, orientation=orientation)
    st.plotly_chart(bar_chart_view)