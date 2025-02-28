import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# https://www.kaggle.com/datasets/wlwwwlw/elite-sports-cars-in-data/data

df = pd.read_csv('Elite Sports Cars in Data.csv')

# Anzahl der Brand Autos
brands= pd.DataFrame(df['Brand'].value_counts())

# Anzahl Modele
models = df[['Brand','Model']].value_counts()
years = df[['Brand','Model', 'Year']].value_counts()





# Balkendiagramm für Marken
#plt.figure(figsize=(10, 5))
#plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)
#sns.countplot(x="Model", data=df, order=df['Model'].value_counts().index, palette="coolwarm")
#plt.title("Anzahl der Autos pro Model")
#plt.xticks(rotation=45)  # Dreht die Labels für bessere Lesbarkeit
#plt.show()





print()