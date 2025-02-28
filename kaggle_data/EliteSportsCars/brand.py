import pandas as pd
import plotly.express as px

# CSV einlesen
df = pd.read_csv('Elite Sports Cars in Data.csv')

# Anzahl der Autos pro Brand
brands = df['Brand'].value_counts().reset_index()
brands.columns = ['Brand', 'count']  # Spalten benennen

# Balkendiagramm mit Hover-Text
fig = px.bar(brands,
             x='count',
             y='Brand',
             orientation='h',
             color='Brand',  # Automatische Farbzuweisung pro Marke
             text='count',  # Werte direkt in den Balken anzeigen
             title="Verkaufszahlen pro Marke",
             labels={'count': 'Anzahl der Verkäufe', 'Brand': 'Marken'})

# Anpassungen für Hover & Design
fig.update_traces(textposition='outside', hoverinfo='x+y')

# Diagramm anzeigen
fig.show()

# save as html
fig.write_html("Elite_Sports_Cars.html")
