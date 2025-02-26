import os

import pandas as pd
from matplotlib import pyplot as plt

pd.options.display.max_rows = 50  # limit the number of rows to display
pd.options.display.max_columns = None  # display all columns

from env_vars import excels, output

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
df3 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

df2 = pd.DataFrame({
    'Salary': [5000, 6000]
})

inner = df3.join(df2, how='inner')
outer = df3.join(df2, how='outer')
left = df3.join(df2, how='left')
right = df3.join(df2, how='right')
#print("--------------------------------------------------------------------")
#print(inner)
#print("--------------------------------------------------------------------")
#print(outer)
#print("--------------------------------------------------------------------")
#print(left)
#print("--------------------------------------------------------------------")
#print(right)


data = {
    "Kategorie": ["DE", "DE", "SY", "SY", "TR", "TR"],
    "Name": ["Berlin", "München","Istanbul", "Izmir", "Aleppo", "Damaskus"],
    "Umsatz": [100, 200, 150, 300, 250, 400]
}

df = pd.DataFrame(data)

statistics_df = pd.DataFrame()
statistics_df['describe'] = df['Kategorie'].describe()

print(statistics_df)

# balkendiagramm erstellen
# plt.bar(df['Name'], df['Umsatz'], color='skyblue')
# liniendiagramm erstellen
#plt.plot(df['Name'], df['Umsatz'], color='skyblue')
# Pie chart erstellen
#plt.pie(df['Umsatz'], labels=df['Name'], autopct='%1.1f%%', startangle=140, colors=['red', 'green', 'blue', 'yellow'])
#plt.title('Balkendiagramm Beispiel')
#plt.xlabel('Name')
#plt.ylabel('Umsatz')
#plt.show()

# Aggregation: Summe, Durchschnitt und Maximum berechnen
agg_result = df.groupby("Kategorie")["Umsatz"].agg(["sum", "mean", "max"]).round(1)
agg_result2 = df.groupby("Kategorie")["Name"].agg(lambda x: ", ".join(x.astype(str))).reset_index()
res = agg_result2.merge(agg_result, on="Kategorie", how="left")
#print(agg_result)
#print(agg_result2)
#print(res)

def process(row):
    row['Umsatz'] = row['Umsatz'] + 20
    return row

df = df.apply(lambda row:process(row), axis=1)

import pandas as pd

df = pd.DataFrame({
    'id': [1, 2, 3, 1, 2],
    'A': ['a1', 'a2', 'a3', 'a1', 'a2'],
    'B': ['b1', 'b2', 'b3', 'b1', 'b2']
})

df2 = df.copy()
df2['A'] = ['c1', 'c2', 'c3', 'c1', 'c2']

print(
    df2.compare(df2)
)

# Alle einzigartigen Werte aus der ersten Spalte 'id' erhalten
unique_values = df["id"].unique()

dfs = []
for value in unique_values:
    filtered_df = df[df["id"] == value].reset_index(drop=True)
    filtered_df["Value"] = value
    dfs.append(filtered_df)
    print("--------------------------------------------------------------------")
    print(filtered_df)






