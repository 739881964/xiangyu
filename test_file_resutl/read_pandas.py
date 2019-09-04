import pandas as pd
from scripts.base_path import *


data = pd.read_excel(EXCEL_PATH, sheet_name='Sheet1')
res = data.isnull().sum()
print(res)
res.to_excel(PANDAS_DATA, header=False)
