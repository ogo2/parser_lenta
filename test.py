
import pandas as pd
import csv

vlans = {"Город": [1, 2, 3, 4], "Название в системе": [5,6,7,8]}
data = [vlans]
df = pd.DataFrame(vlans)
df.to_csv('table/csv/stock_ozon.csv', index=False)