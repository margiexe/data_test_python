import pandas as pd

def read_excel_data(file_path):
    return pd.read_excel("HINDALCO_1D.xlsx")

if __name__ == "__main__":
    data = read_excel_data("HINDALCO_1D.xlsx")
    print(data.head())
