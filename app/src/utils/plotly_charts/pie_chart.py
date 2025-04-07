import streamlit as st
import pandas as pd
import plotly.express as px


def pie_chart1(df: pd.DataFrame, values: str, names: str, title: str = "Gráfico"):
    pie_chart_view = px.pie(data_frame=df, values=values, names=names, title=title)
    st.plotly_chart(pie_chart_view)