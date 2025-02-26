import pandas as pd
from matplotlib import pyplot as plt

# Beispiel-Daten
data = {'Kategorie': ['A', 'B', 'C', 'D'],
        'Wert': [10, 20, 15, 25]}

df = pd.DataFrame(data)

# Balkendiagramm erstellen
# plt.bar(df['Kategorie'], df['Wert'], color='skyblue')
# liniendiagramm erstellen
# plt.plot(df['Kategorie'], df['Wert'], color='skyblue')
# Pie chart erstellen
# plt.pie(df['Wert'], labels=df['Kategorie'], autopct='%1.1f%%', startangle=140, colors=['red', 'green', 'blue', 'yellow'])
# Scatter plot erstellen
# plt.scatter(df['Kategorie'], df['Wert'], color='skyblue')
# Histogramm erstellen
# plt.hist(df['Wert'], bins=5, color='skyblue')
# Box plot erstellen
# plt.boxplot(df['Wert'], patch_artist=True, boxprops=dict(facecolor='skyblue'))
# Violin plot erstellen
# plt.violinplot(df['Wert'], showmedians=True)
# Heatmap erstellen
# plt.imshow([df['Wert']], cmap='hot', interpolation='nearest')
# multiple line chart erstellen
df2 = pd.DataFrame({
'Kategorie': ['A', 'B', 'C', 'D'],
    'Wert2': [15, 25, 10, 20]
})


# differenz zwischen zwei dfs
df['Wert3'] = df['Wert'] - df2['Wert2']

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Balkendiagramm Beispiel')
plt.xlabel('Kategorie')
plt.ylabel('Wert')

# Diagramm anzeigen
plt.show()