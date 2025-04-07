import pandas as pd

df = pd.read_csv("app/data/input/Sales_Data.csv")

def get_data_agg(df: pd.DataFrame, column_name: str, agg_type: str = "sum"):
    return df[column_name].agg(agg_type)

def disc_sales(df):
    return df.groupby("ProductID").agg({"DiscountPercentage": "mean", "FinalSalePrice":"sum", "ProductCategory": "first"}).reset_index()

def get_group_agg(df: pd.DataFrame, group_col: str, agg_col: str, agg_type: str = "sum") -> pd.DataFrame:
    return df.groupby(group_col)[agg_col].agg(agg_type).reset_index()
