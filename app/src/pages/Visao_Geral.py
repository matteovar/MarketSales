import pandas as pd
import streamlit as st
from src.main import df, feedback, receita, returnflag, total_sales
from src.utils.cards import create_cards


def show_dashboard():
    st.subheader("Dashboard")

    st.dataframe(df)

    cols = st.columns(4)  # Cria 4 colunas

    with cols[0]:  # Adiciona o card na primeira coluna
        create_cards("Valor Total", f"{receita(df):,.2f}")

    with cols[1]:  # Adiciona outro card na segunda coluna
        create_cards("Numero de Vendas", f"{total_sales(df)}")

    with cols[2]:  # Adiciona outro card na terceira coluna
        create_cards("Feedback do Cosumidor", f"{feedback(df):.1f}")

    with cols[3]:  # Adiciona outro card na quarta coluna
        create_cards("Taxa de retorno", f"{(returnflag(df)/1000)*100}%")
