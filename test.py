import pandas as pd

# Beispiel-Daten
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['x', 'y', 'z'],
    'C': [10, 20, 30],
    'D': [100, 200, 300]
})

# Neue Zeile, die hinzugefügt werden soll
new_row = {'A': 4, 'B': 'w'}

# Zeile hinzufügen
df = df._append(new_row, ignore_index=True)

liste = ["x", "y", "z"]

liste_2 = [1, 2]

print(df)
output = pd.DataFrame()
for buchstabe in liste:
    for zahl in liste_2:
        df_2 = df.loc[(df["A"] == zahl)&(df["B"].str.strip() == buchstabe), ["C", "D"]]
        if df_2.empty:
            continue
        label = buchstabe+" " + str(zahl)
        df_2["label"] = label
        output = output._append(df_2, ignore_index=True)
        print(output)


