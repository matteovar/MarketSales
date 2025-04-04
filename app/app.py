import pandas as pd
import streamlit as st
from src.pages import pages
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Sales", layout="wide")


def main():
    st.title("Meu Aplicativo Streamlit")

    # Sidebar para selecionar as páginas
    selected_page = st.sidebar.selectbox("Escolha a página", list(pages.keys()))

    # Exibindo a página selecionada
    if selected_page in pages:
        pages[selected_page]()


if __name__ == "__main__":
    main()
