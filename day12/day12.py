import pandas as pd
import numpy as np

file = '/home/sahil/Downloads/collected_data.xlsx'
foo = pd.read_excel(file)
print("Total rows: {0}".format(len(file)))
print(list(file))
data_sorted = file.sort_values(['Name'], ascending=False)
