import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Elite Sports Cars in Data.csv')

# Anzahl der Brand Autos
brands= pd.DataFrame(df['Brand'].value_counts())

# Anzahl Modele
models = df[['Brand','Model']].value_counts()
years = df[['Brand','Model', 'Year']].value_counts()

# Diagramm von years erstellen
# plt.bar(brands.index, brands['count'])

# color für balken labels einstellen
colors = ['blue', 'red', 'green', 'purple', 'yellow', 'orange', 'pink', 'brown', 'black', 'grey']
# Diagramm erstellen
plt.figure(figsize=(8, 5))

# Horizontal Diagramm erstellen
plt.barh(brands.index, brands['count'], color=colors)

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Balkendiagramm Beispiel')
plt.xlabel('Brand')


# x takt einstellen
plt.xticks(range(0, max(brands['count'])+200, 50))
#plt.xticks(rotation=90)



plt.ylabel('count')
# y takt einstellen
#plt.yticks(range(0, len(brands)+1, 1))





# margin einstellen
plt.margins(0.1)

# äußere Rahmen margin einstellen
plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.3)


# Diagramm anzeigen
plt.show()






print()