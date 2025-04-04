import pandas as pd

df = pd.read_csv("app/data/input/Sales_Data.csv")


def receita(df):
    receita = df["FinalSalePrice"].sum()

    return receita


def total_sales(df):
    sales = df["SalesQuantity"].sum()
    return sales


def feedback(df):
    fb = df["CustomerFeedbackRating"].mean()
    return fb


def returnflag(df):
    rf = df["ReturnFlag"].sum()
    return rf
