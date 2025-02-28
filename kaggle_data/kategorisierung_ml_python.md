
# Kategorisierung in Maschinellem Lernen mit Python

In diesem Abschnitt werden wir die Kategorisierung (Klassifikation) in maschinellem Lernen mit Python implementieren und die wichtigsten Modelle, deren Vorteile und Nachteile diskutieren.

## Beispiel 1: Logistische Regression

Logistische Regression ist ein einfaches Modell für binäre Klassifikation, z.B. für die Spam-Nachrichtenerkennung.

### Python-Code:
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Beispiel-Daten: E-Mails als Spam (1) oder Nicht-Spam (0)
data = {'Text': ['Win money now', 'Hello, how are you?', 'Get rich quick', 'Meeting tomorrow', 'Free money!', 'Important updates'],
        'Label': [1, 0, 1, 0, 1, 0]}
df = pd.DataFrame(data)

# Umwandlung des Textes in numerische Werte (Simple Bag-of-Words)
df['Text'] = df['Text'].apply(lambda x: len(x.split()))

# Merkmale und Zielvariable
X = df[['Text']]  # Merkmale
y = df['Label']   # Zielvariable

# Aufteilen der Daten in Trainings- und Testdatensatz
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Logistische Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Vorhersagen
y_pred = model.predict(X_test)

# Evaluierung
accuracy = accuracy_score(y_test, y_pred)
print(f'Genauigkeit: {accuracy * 100:.2f}%')
```

### Erklärung:
- **Datensammlung**: Wir haben einfache E-Mail-Daten, die als Spam oder Nicht-Spam kategorisiert sind.
- **Vorverarbeitung**: Der Text wird in numerische Werte umgewandelt, indem wir die Anzahl der Wörter in jeder E-Mail zählen (Bag-of-Words).
- **Modelltraining**: Wir trainieren ein logistische Regressionsmodell.
- **Evaluierung**: Die Genauigkeit des Modells wird anhand des Testdatensatzes berechnet.

### Vorteile:
- Einfach zu implementieren und zu interpretieren.
- Gut geeignet für binäre Klassifikationen.
- Effizient bei linearen Problemen.

### Nachteile:
- Kann bei komplexeren, nicht-linearen Problemen schlechte Ergebnisse liefern.
- Muss die Annahme einer linearen Trennung zwischen den Klassen machen.

## Beispiel 2: Entscheidungsbaum

Entscheidungsbäume sind nützlich, wenn man eine klare, interpretierbare Entscheidungslogik benötigt.

### Python-Code:
```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Beispiel-Daten: Krankheitsdiagnose
data = {'Fieber': [1, 0, 1, 0, 1],
        'Husten': [1, 0, 1, 0, 1],
        'Müdigkeit': [1, 0, 1, 1, 0],
        'Diagnose': ['Grippe', 'Erkältung', 'Grippe', 'Erkältung', 'Grippe']}
df = pd.DataFrame(data)

# Merkmale und Zielvariable
X = df[['Fieber', 'Husten', 'Müdigkeit']]
y = df['Diagnose']

# Aufteilen der Daten in Trainings- und Testdatensatz
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entscheidungsbaum
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Vorhersagen
y_pred = model.predict(X_test)

# Evaluierung
print(classification_report(y_test, y_pred))
```

### Erklärung:
- **Datensammlung**: Wir haben Daten über Symptome und die zugehörige Diagnose.
- **Vorverarbeitung**: Es sind keine großen Vorverarbeitungsschritte nötig, da die Daten bereits numerisch sind.
- **Modelltraining**: Wir trainieren ein Entscheidungsbaum-Modell.
- **Evaluierung**: Wir verwenden den `classification_report`, um Präzision, Recall und F1-Score zu bewerten.

### Vorteile:
- Einfach verständlich und interpretierbar.
- Kann sowohl für Klassifikation als auch für Regression verwendet werden.
- Sehr flexibel und gut bei der Modellierung von nicht-linearen Beziehungen.

### Nachteile:
- Neigt dazu, zu überanpassen (Overfitting), insbesondere bei tiefen Bäumen.
- Weniger stabil bei kleinen Änderungen der Eingabedaten.

## Beispiel 3: Support Vector Machines (SVM)

SVM ist besonders gut geeignet, um lineare und nicht-lineare Trennungen zwischen Klassen zu finden.

### Python-Code:
```python
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Iris-Datensatz laden
iris = load_iris()
X = iris.data
y = iris.target

# Aufteilen der Daten in Trainings- und Testdatensatz
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# SVM-Modell
model = SVC(kernel='linear')  # Lineare Trennung
model.fit(X_train, y_train)

# Vorhersagen
y_pred = model.predict(X_test)

# Evaluierung
accuracy = accuracy_score(y_test, y_pred)
print(f'Genauigkeit: {accuracy * 100:.2f}%')
```

### Erklärung:
- **Datensammlung**: Wir verwenden den Iris-Datensatz, der 150 Blumenarten in 3 Kategorien unterteilt.
- **Modelltraining**: Wir trainieren ein SVM-Modell mit einem linearen Kernel.
- **Evaluierung**: Wir berechnen die Genauigkeit des Modells.

### Vorteile:
- Effektiv für hohe-dimensionalen Raum (z.B. bei Textklassifikation oder Bildklassifikation).
- Gut geeignet für nicht-lineare Trennungen, wenn der Kernel richtig gewählt wird.

### Nachteile:
- Rechenintensiv, besonders bei großen Datensätzen.
- Schwierig zu interpretieren, da es keine klaren Entscheidungsgrenzen gibt.

## Fazit: Vorteile und Nachteile der Modelle

| Modell                    | Vorteile                                         | Nachteile                                      |
|---------------------------|--------------------------------------------------|------------------------------------------------|
| **Logistische Regression** | Einfach, schnell, gut für binäre Klassifikation | Kann bei nicht-linearen Problemen schlecht abschneiden |
| **Entscheidungsbaum**      | Gut verständlich und interpretierbar            | Neigt zu Overfitting                           |
| **SVM**                    | Gut bei hochdimensionalen Daten, flexibel       | Rechenintensiv, schwer zu interpretieren      |

## Zusammenfassung

- **Logistische Regression** eignet sich für einfache binäre Klassifikationen, hat jedoch Schwierigkeiten bei komplexeren, nicht-linearen Aufgaben.
- **Entscheidungsbäume** bieten eine einfache und verständliche Lösung, tendieren jedoch zu Überanpassung.
- **SVM** ist besonders effektiv bei der Trennung von Daten in hochdimensionalen Räumen, ist jedoch rechenintensiv.

Jedes Modell hat seine Stärken und Schwächen, und die Wahl des Modells hängt von der spezifischen Anwendung und den Eigenschaften des Datensatzes ab.
