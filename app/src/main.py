import pandas as pd

df = pd.read_csv("app/data/input/Sales_Data.csv")

def sales_date(df):
    return df.groupby(["TransactionDate"])["FinalSalePrice"].sum().reset_index()

def fat_cat(df):
    return df.groupby(["ProductCategory"])["FinalSalePrice"].sum().reset_index()

def rec_cat(df):
    return  df.groupby(["ProductID", "ProductCategory"])["FinalSalePrice"].sum().reset_index()

def sales_disc_prod(df):
    return df.groupby(["ProductCategory"])[["SalesPrice","FinalSalePrice"]].sum().reset_index()

def get_data_agg(df: pd.DataFrame, column_name: str, agg_type: str = "sum"):
    return df[column_name].agg(agg_type)

def disc_sales(df):
    return df.groupby("ProductID").agg({"DiscountPercentage": "mean", "FinalSalePrice":"sum", "ProductCategory": "first"}).reset_index()

def disc_cat(df):
    return df.groupby(["ProductCategory"])["DiscountAmount"].mean().reset_index()