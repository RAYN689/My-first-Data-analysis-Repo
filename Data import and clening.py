# import necessary libraries

import pandas as pd
import numpy as np

test = '/Users/olayinkafaniran/Documents/IT PROJECTS/Pandas-Data-Science-Tasks-master 2/SalesAnalysis/Sales_Data/Sales_April_2019.csv'
data = pd.read_csv(test)

# To view information and statistical data about the file
print(data.head())
print(data.describe())
print(data.info())
print(data.dtypes)
print(data.shape())
