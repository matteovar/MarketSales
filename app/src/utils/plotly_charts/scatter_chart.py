import streamlit as st
import pandas as pd
import plotly.express as px


def scatter_chart1(
    df: pd.DataFrame,
    x: str,
    y: str,
    color=None,
    hover_name=None,
    size=None,
    title: str = "Gráfico",
    x_label: str = None,
    y_label: str = None,
    color_label: str = None,
    hover_label: str = None,
):
    labels = {x: x_label if x_label else x, y: y_label if y_label else y}

    if color and color_label:
        labels[color] = color_label
    if hover_name and hover_label:
        labels[hover_name] = hover_label
    scatter_chart_view = px.scatter(
        data_frame=df,
        x=x,
        y=y,
        color=color,
        hover_name=hover_name,
        size=size,
        title=title,
        labels=labels,
    )
    st.plotly_chart(scatter_chart_view)
