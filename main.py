# Pandas: How to keep the Index when merging DataFrames

import pandas as pd

df1 = pd.DataFrame({
    'year': [2020, 2021, 2022, 2023],
    'profit': [1500, 2500, 3500, 4500],
}, index=['A', 'B', 'C', 'D'])


df2 = pd.DataFrame({
    'year': [2020, 2021, 2022, 2023],
    'employees': [10, 15, 20, 25],
})


df3 = df1.reset_index().merge(df2, how='left').set_index('index')

#        year  profit  employees
# index
# A      2020    1500         10
# B      2021    2500         15
# C      2022    3500         20
# D      2023    4500         25
print(df3)