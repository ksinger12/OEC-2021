import pandas as pd

data = [
    pd.read_excel("OEC2021 - School Record Book .xlsx", sheet_name=0),
    pd.read_excel("OEC2021 - School Record Book .xlsx", sheet_name=1),
    pd.read_excel("OEC2021 - School Record Book .xlsx", sheet_name=2),
    pd.read_excel("OEC2021 - School Record Book .xlsx", sheet_name=3),
    ]


print(data)
