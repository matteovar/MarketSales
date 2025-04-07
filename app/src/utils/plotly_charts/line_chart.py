import streamlit as st
import pandas as pd
import plotly.express as px


def line_chart1(df: pd.DataFrame, x: str, y: str, title: str = "Gráfico"):
    line_chart_view = px.line(data_frame=df, x=x, y=y, title=title)
    st.plotly_chart(line_chart_view)