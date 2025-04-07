import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sales", layout="wide")


def main():

    pages_1 = {
        "Favoritos": [
            st.Page("src/pages/Visao_Geral.py", title="Visão Geral"),
            st.Page("src/pages/Desempenho_por_Categoria.py", title="Desempenho por Categoria"),
            st.Page("src/pages/Impacto_de_Promoções.py", title="Impacto de Promoções"),
        ],
    }

    pg = st.navigation(pages_1)
    pg.run()


if __name__ == "__main__":
    main()
