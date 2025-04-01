import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# CSV einlesen
df = pd.read_csv('Elite Sports Cars in Data.csv')

# Anzahl der Autos pro Brand
brands = df['Brand'].value_counts().reset_index()
brands.columns = ['Brand', 'count']  # Spalten benennen

# Initiale Balkendiagramm-Figur ohne Daten (diese werden in den Buttons festgelegt)
fig = go.Figure()

# Jede Marke als separaten Trace hinzufügen, damit man sie ausblenden kann
for i, brand in enumerate(brands["Brand"]):
    fig.add_trace(go.Bar(
        x=[brands["count"][i]],
        y=[brand],
        orientation='h',
        name=brand,
        visible=True  # Standardmäßig sichtbar
    ))


# Layout mit Dropdown-Menü
fig.update_layout(
    updatemenus=[{
        "direction": "down",
        "showactive": True
    }],
    title="Verkaufszahlen pro Marke",
    xaxis_title="Anzahl der Verkäufe",
    yaxis_title="Marken"
)

# Diagramm anzeigen
fig.show()

# Save as HTML
fig.write_html("Elite_Sports_Cars_Filter.html")
