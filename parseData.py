import pandas as pd

def getData():
    return [pd.read_excel("OEC2021 - School Record Book.xls", sheet_name=0),
        pd.read_excel("OEC2021 - School Record Book.xls", sheet_name=1),
        pd.read_excel("OEC2021 - School Record Book.xls", sheet_name=2),
        pd.read_excel("OEC2021 - School Record Book.xls", sheet_name=3)]

