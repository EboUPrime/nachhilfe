import os

import pandas as pd
pd.options.display.max_rows = 50  # limit the number of rows to display
pd.options.display.max_columns = None  # display all columns

from env_vars import images, excels, output

list_of_excel_files =  [os.path.join(excels, x) for x in os.listdir(excels) if x.endswith('.xlsx')]

df0 = pd.read_excel(list_of_excel_files[0])
df1 = pd.read_excel(list_of_excel_files[1])

#print(df0)
#print("--------------------------------------------------------------------")
#print(df1)

# join the two dataframes joining on the column 'id' left join
df = pd.merge(df0, df1, on='id', how='left')
#print("--------------------------------------------------------------------")
#print(df)
df.to_excel(os.path.join(output, 'output.xlsx'), index=False)

# concatenate the two dataframes along the rows
df_concat = pd.concat([df0, df1], axis=0)
#print("--------------------------------------------------------------------")
#print(df_concat)

# Beispiel DataFrames
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

df2 = pd.DataFrame({
    'Salary': [5000, 6000]
})

inner = df1.join(df2, how='inner')
outer = df1.join(df2, how='outer')
left = df1.join(df2, how='left')
right = df1.join(df2, how='right')
#print("--------------------------------------------------------------------")
#print(inner)
#print("--------------------------------------------------------------------")
#print(outer)
#print("--------------------------------------------------------------------")
#print(left)
#print("--------------------------------------------------------------------")
#print(right)


