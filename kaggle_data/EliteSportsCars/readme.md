# Ausreißer in einem Datensatz erkennen

Ausreißer sind extreme Werte in einem Datensatz, die weit von anderen Werten entfernt liegen. Sie können durch Messfehler, unterschiedliche Bedingungen oder einfach durch natürliche Varianz entstehen. Hier sind einige Methoden zur Erkennung von Ausreißern.

## 1. Z-Score-Methode (Standardabweichung)

Die Z-Score-Methode bewertet, wie viele Standardabweichungen ein Wert von der mittleren Verteilung entfernt ist. Werte mit einem Z-Score > 3 werden oft als Ausreißer betrachtet.

```python
from scipy import stats
import numpy as np
import pandas as pd

# Beispiel-Daten
np.random.seed(42)
data = np.random.normal(50, 10, 100)  # Normalverteilte Daten
outlier_data = np.append(data, [150, 200])  # Fügt Ausreißer hinzu
df = pd.DataFrame({'Wert': outlier_data})

# Z-Score berechnen
z_scores = np.abs(stats.zscore(df['Wert']))
outliers = df[z_scores > 3]  # Alle Werte mit Z-Score > 3
print(outliers)
```

### Vorteile:
- Effektiv bei normalverteilten Daten
- Schnell berechenbar

### Nachteile:
- Funktioniert schlecht bei nicht normalverteilten Daten
- Empfindlich gegenüber extremen Ausreißern

---

## 2. Interquartilsabstand (IQR-Methode)

Der Interquartilsabstand (IQR) ist die Differenz zwischen dem oberen (Q3) und unteren Quartil (Q1). Werte außerhalb von 1.5 * IQR gelten als Ausreißer.

```python
# Quartile berechnen
Q1 = df['Wert'].quantile(0.25)
Q3 = df['Wert'].quantile(0.75)
IQR = Q3 - Q1

# Definition von Ausreißern
outliers = df[(df['Wert'] < (Q1 - 1.5 * IQR)) | (df['Wert'] > (Q3 + 1.5 * IQR))]
print(outliers)
```

### Vorteile:
- Funktioniert gut bei nicht normalverteilten Daten
- Weniger anfällig für extreme Ausreißer

### Nachteile:
- Nicht optimal für sehr kleine oder stark symmetrische Datensätze

---

## 3. Visuelle Methoden

### a) Boxplot

Ein Boxplot zeigt den Median, die Quartile und Ausreißer visuell an.

```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
sns.boxplot(x=df['Wert'])
plt.title("Ausreißer-Erkennung mit Boxplot")
plt.show()
```

### b) Scatterplot

Scatterplots sind hilfreich, um Ausreißer in mehreren Dimensionen zu erkennen.

```python
# Beispiel-Daten mit mehreren Spalten
df2 = pd.DataFrame({
    'Jahr': np.random.randint(2000, 2025, size=len(df)),
    'Wert': df['Wert']
})

sns.scatterplot(x=df2['Jahr'], y=df2['Wert'])
plt.title("Ausreißer-Erkennung mit Scatterplot")
plt.show()
```

### Vorteile:
- Intuitiv und einfach zu interpretieren
- Kann Muster oder Gruppen sichtbar machen

### Nachteile:
- Nicht objektiv messbar
- Funktioniert nicht gut bei hohen Datenmengen

---

## 4. Weitere Methoden

- **Lokale Ausreißerfaktor-Methode (LOF)**: Identifiziert Ausreißer durch Vergleiche in einer lokalen Umgebung.
- **DBSCAN (Clustering-Methode)**: Gruppiert dichte Bereiche und markiert isolierte Punkte als Ausreißer.
- **Maschinelles Lernen**: Modelle wie Isolation Forest oder One-Class SVM können verwendet werden.

---

## Fazit

Die Wahl der Methode hängt von den Daten und dem Anwendungsfall ab:
- **Z-Score** für normalverteilte Daten
- **IQR** für allgemeine numerische Werte
- **Boxplot & Scatterplot** für eine visuelle Analyse

Benötigst du eine bestimmte Methode für dein Projekt? 🚀

