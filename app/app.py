import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sales", layout="wide")


def main():

    pages_1 = {
        "Pages": [
            st.Page("src/pages/General_Informations.py", title="General Informations"),
            st.Page(
                "src/pages/Performance_by_Category.py", title="Performance by Category"
            ),
            st.Page("src/pages/Impact_of_Promotions.py", title="Impact of Promotions"),
            st.Page("src/pages/Costumer_Profile.py", title="Costumer Profile"),
        ],
    }

    pg = st.navigation(pages_1)
    pg.run()


if __name__ == "__main__":
    main()
