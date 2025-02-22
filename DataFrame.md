
# Unterschied zwischen `merge()` und `join()` in Pandas

Der Unterschied zwischen **`merge()`** und **`join()`** in Pandas liegt hauptsächlich in der Art und Weise, wie die DataFrames miteinander kombiniert werden. Beide Funktionen dienen zum Kombinieren von DataFrames, aber sie haben unterschiedliche Anwendungsfälle und Flexibilität.

## 1. **`merge()`**

Die `merge()`-Funktion in Pandas ist die vielseitigere Methode, die sich auf die Kombination von DataFrames anhand von spezifischen **Spalten** oder **Indexwerten** konzentriert. Es ist dem SQL-Join sehr ähnlich und bietet eine große Flexibilität bei der Auswahl der Join-Bedingungen.

- **Spaltenbasiertes Zusammenführen**: `merge()` verwendet standardmäßig Spalten, um DataFrames zu verbinden. Du kannst die `on`-Option verwenden, um explizit die Spalte anzugeben, auf der der Join basieren soll.
  
- **Flexibilität bei der Auswahl der Joins**: `merge()` unterstützt alle gängigen SQL-Join-Typen: `inner`, `left`, `right`, und `outer`. Du kannst diese mit der `how`-Option steuern.

- **Mehrere Spalten**: Du kannst auch mehrere Spalten als Schlüssel verwenden, um DataFrames zu verbinden.

#### Beispiel:

```python
import pandas as pd

# Beispiel DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'Alter': [25, 30, 35]
})

# Merge von df1 und df2 basierend auf der Spalte 'ID'
result = pd.merge(df1, df2, on='ID', how='inner')
print(result)
```

#### Ergebnis:

```plaintext
ID    Name    Alter
1     Alice   25
2     Bob     30
```

- Hier ist der Join auf der Spalte `ID` basierend auf einem **inner Join** durchgeführt worden.

## 2. **`join()`**

Die `join()`-Methode ist eine einfachere und spezifischere Methode, um DataFrames zu verbinden, die standardmäßig **über den Index** zusammengeführt werden. Sie eignet sich hervorragend, wenn du DataFrames anhand ihres **Index** kombinieren möchtest.

- **Indexbasiertes Zusammenführen**: Standardmäßig wird `join()` verwendet, um DataFrames anhand ihrer **Indexwerte** zu verbinden.
  
- **Einfache Anwendung**: `join()` ist einfacher und eignet sich besser für DataFrames, die bereits den gleichen Index haben oder eine einfache Index-Verbindung benötigen.

- **Einschränkung auf Index**: `join()` kann auch mit einer **Spalte** als Index verwendet werden, aber dies ist eine Ausnahme und erfordert explizite Anpassung.

#### Beispiel:

```python
import pandas as pd

# Beispiel DataFrames mit Index
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Alter': [25, 30, 35]
}, index=[1, 2, 3])

df2 = pd.DataFrame({
    'Geschlecht': ['F', 'M', 'M']
}, index=[1, 2, 3])

# Join df2 an df1
result = df1.join(df2)
print(result)
```

#### Ergebnis:

```plaintext
       Name  Alter Geschlecht
1     Alice     25          F
2       Bob     30          M
3   Charlie     35          M
```

- Hier wird der Join durch den Index der DataFrames durchgeführt. Der Indexwert von `df1` und `df2` wird verglichen, um die Zeilen zu kombinieren.

## 3. **`concat()`** – Zusammenführen von DataFrames

Die `concat()`-Funktion in Pandas ermöglicht es, DataFrames entlang einer Achse zu kombinieren. Dies kann sowohl zeilenweise (vertikal) als auch spaltenweise (horizontal) erfolgen.

#### Beispiel: Zeilenweise Zusammenführen

```python
import pandas as pd

# Beispiel DataFrames
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Alter': [25, 30, 35]
})

df2 = pd.DataFrame({
    'Name': ['David', 'Edward'],
    'Alter': [40, 45]
})

# Zusammenführen von df1 und df2 entlang der Zeilen
result = pd.concat([df1, df2])
print(result)
```

#### Ergebnis:

```plaintext
       Name  Alter
0     Alice     25
1       Bob     30
2   Charlie     35
0     David     40
1    Edward     45
```

- `concat()` fügt `df1` und `df2` zeilenweise zusammen. Beachte, dass der Index von `df2` dupliziert wird.

#### Beispiel: Spaltenweise Zusammenführen

```python
# Zusammenführen entlang der Spalten (Achse 1)
df3 = pd.concat([df1, df2], axis=1)
print(df3)
```

#### Ergebnis:

```plaintext
       Name  Alter     Name  Alter
0     Alice     25    David     40
1       Bob     30   Edward     45
2   Charlie     35     NaN    NaN
```

- In diesem Fall wird der Join entlang der Spaltenachse durchgeführt.

## 4. **Weitere nützliche Pandas-Operationen**

### 4.1 **`drop()`** – Entfernen von Spalten oder Zeilen

Die `drop()`-Methode entfernt Spalten oder Zeilen aus einem DataFrame.

#### Beispiel: Entfernen einer Spalte

```python
df1 = df1.drop('Alter', axis=1)
print(df1)
```

#### Ergebnis:

```plaintext
       Name
0     Alice
1       Bob
2   Charlie
```

### 4.2 **`rename()`** – Umbenennen von Spalten

Mit `rename()` kannst du Spaltennamen ändern.

#### Beispiel:

```python
df1 = df1.rename(columns={'Name': 'Vollständiger Name'})
print(df1)
```

#### Ergebnis:

```plaintext
  Vollständiger Name
0              Alice
1                Bob
2            Charlie
```

### 4.3 **`sort_values()`** – Sortieren von DataFrames

Die Methode `sort_values()` sortiert die Werte eines DataFrames basierend auf einer bestimmten Spalte.

#### Beispiel:

```python
df1 = df1.sort_values(by='Alter', ascending=False)
print(df1)
```

#### Ergebnis:

```plaintext
       Name  Alter
2   Charlie     35
1       Bob     30
0     Alice     25
```

### 4.4 **`groupby()`** – Gruppieren von Daten

Die `groupby()`-Methode ermöglicht das Gruppieren von Daten nach bestimmten Spalten und die Anwendung von Aggregatfunktionen.

#### Beispiel:

```python
df1 = pd.DataFrame({
    'Kategorie': ['A', 'B', 'A', 'B', 'A'],
    'Wert': [10, 20, 30, 40, 50]
})

grouped = df1.groupby('Kategorie').sum()
print(grouped)
```

#### Ergebnis:

```plaintext
           Wert
Kategorie      
A           90
B           60
```

## 5. **Zusammenfassung der wichtigsten Pandas-Operationen**

| **Operation**          | **Beschreibung**                           | **Beispiel**                                |
|------------------------|--------------------------------------------|---------------------------------------------|
| `merge()`              | Kombiniert DataFrames basierend auf einer oder mehreren Spalten | `df1.merge(df2, on='ID', how='inner')`      |
| `join()`               | Kombiniert DataFrames basierend auf dem Index | `df1.join(df2)`                             |
| `concat()`             | Kombiniert DataFrames entlang einer Achse (Zeilen oder Spalten) | `pd.concat([df1, df2])`                     |
| `drop()`               | Entfernt Spalten oder Zeilen aus einem DataFrame | `df.drop('Spalte', axis=1)`                |
| `rename()`             | Benennt Spalten um                        | `df.rename(columns={'alt': 'neu'})`         |
| `sort_values()`        | Sortiert den DataFrame basierend auf einer Spalte | `df.sort_values(by='Spalte', ascending=False)` |
| `groupby()`            | Gruppiert den DataFrame nach einer Spalte und wendet Aggregatfunktionen an | `df.groupby('Spalte').sum()`               |

## 6. **Fazit**

- **Verwende `merge()`** und **`concat()`**, wenn du DataFrames auf flexible und effiziente Weise kombinieren möchtest.
- **Verwende `join()`**, wenn du Daten basierend auf dem Index schnell verbinden musst.
- **Nutze weitere Operationen** wie `drop()`, `rename()`, `sort_values()` und `groupby()`, um deine DataFrames nach Bedarf zu bearbeiten und zu analysieren.



# Pandas Aggregationsmethoden

## 🔍 Grundlegende Aggregationsmethoden
| Methode          | Beschreibung |
|-----------------|-------------|
| `.count()`      | Anzahl der Werte |
| `.sum()`        | Summe der Werte |
| `.mean()`       | Durchschnitt (arithmetisches Mittel) |
| `.median()`     | Median (Zentralwert) |
| `.min()`        | Minimum |
| `.max()`        | Maximum |

```python
# Beispiel: Summe aller Werte in der Spalte "Wert"
df["Wert"].sum()
```

## 📈 Statistische Aggregationen
| Methode          | Beschreibung |
|-----------------|-------------|
| `.std()`        | Standardabweichung |
| `.var()`        | Varianz |
| `.sem()`        | Standardfehler des Mittelwerts |
| `.mad()`        | Mittlere absolute Abweichung |
| `.skew()`       | Schiefe (Asymmetrie der Verteilung) |
| `.kurt()`       | Kurtosis (Wölbung der Verteilung) |

```python
# Beispiel: Standardabweichung der Spalte "Wert"
df["Wert"].std()
```

## 📝 Positionale Aggregationen
| Methode          | Beschreibung |
|-----------------|-------------|
| `.idxmin()`     | Index des kleinsten Werts |
| `.idxmax()`     | Index des größten Werts |
| `.quantile(q)`  | Quantil (z. B. 0.25 für das 25%-Perzentil) |

```python
# Beispiel: 25%-Quantil der Spalte "Wert"
df["Wert"].quantile(0.25)
```

## 🌟 Aggregation für kategorische Werte
| Methode          | Beschreibung |
|-----------------|-------------|
| `.nunique()`    | Anzahl einzigartiger Werte |
| `.mode()`       | Häufigster Wert (Modus) |

```python
# Beispiel: Anzahl einzigartiger Kategorien
df["Kategorie"].nunique()
```

## 📝 String-Operationen (bei `object`-Spalten)
| Methode          | Beschreibung |
|-----------------|-------------|
| `.str.join()`   | Strings zusammenfügen |
| `.str.cat()`    | Strings verketten |

```python
# Beispiel: Strings innerhalb einer Gruppe verketten
df.groupby("Kategorie")["Name"].agg(lambda x: ", ".join(x))
```

## 🔢 Aggregation mit `groupby()`
```python
df.groupby("Kategorie").agg({
    "Wert": ["sum", "mean", "max"],
    "Preis": ["min", "median"]
})
```




# Lambda-Funktionen in Python – Use Cases

## 1. Einfache Berechnungen direkt in `map()` oder `filter()`
Lambda-Funktionen eignen sich gut für **kurze Transformationen** oder **Filteroperationen**.

### Quadrat aller Zahlen berechnen
```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # ➝ [1, 4, 9, 16, 25]
```

### Nur gerade Zahlen behalten
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # ➝ [2, 4, 6]
```

---

## 2. Sortieren mit `lambda`
Man kann `lambda` nutzen, um eine **Sortierfunktion** für `sorted()` oder `sort()` zu definieren.

### Sortieren nach der Länge von Strings
```python
words = ["Banane", "Apfel", "Kiwi", "Erdbeere"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # ➝ ['Kiwi', 'Apfel', 'Banane', 'Erdbeere']
```

### Sortieren nach dem 2. Element in einer Liste von Tupeln
```python
data = [(1, 3), (4, 1), (2, 5)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # ➝ [(4, 1), (1, 3), (2, 5)]
```

---

## 3. Verwenden von `lambda` in `pandas`
Lambda-Funktionen sind sehr nützlich in **pandas**, z. B. für das Bearbeiten von Spalten.

### Eine Spalte transformieren
```python
import pandas as pd

df = pd.DataFrame({'Name': ['Max', 'Anna', 'Tom'], 'Alter': [15, 22, 30]})
df['Alter_plus_5'] = df['Alter'].apply(lambda x: x + 5)
print(df)

```

```python
python
import pandas as pd

# Beispiel-DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Alter': [25, 30, 35],
    'Stadt': ['Berlin', 'Hamburg', 'München']
})

# Methode zur Bearbeitung einer Zeile mit Lambda
def transform_row(row):
    return f"{row['Name']} ist {row['Alter']} Jahre alt und lebt in {row['Stadt']}."

# Neue Spalte mit transformierten Werten
df['Beschreibung'] = df.apply(lambda row: transform_row(row), axis=1)
print(df)

```

```python
python
import pandas as pd

data = {
    "Kategorie": ["DE", "DE", "SY", "SY", "TR", "TR"],
    "Name": ["Berlin", "München","Istanbul", "Izmir", "Aleppo", "Damaskus"],
    "Umsatz": [100, 200, 150, 300, 250, 400]
}

df = pd.DataFrame(data)

def process(row):
    row['Umsatz'] = row['Umsatz'] + 20
    return row

df = df.apply(lambda row:process(row), axis=1)

print(df)

```



### Spaltenwerte basierend auf einer Bedingung ersetzen
```python
df['Status'] = df['Alter'].apply(lambda x: 'Erwachsen' if x >= 18 else 'Kind')
print(df)
```

---

## 4. Mehrere Bedingungen in einer einzigen Zeile

### Notenbewertung
```python
note = lambda x: "Bestanden" if x >= 50 else "Nicht bestanden"
print(note(70))  # ➝ Bestanden
print(note(40))  # ➝ Nicht bestanden
```

---

## 5. Kombination mit `reduce()`

### Summe berechnen
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
summe = reduce(lambda x, y: x + y, numbers)
print(summe)  # ➝ 15
```

**Hinweis:** `reduce()` wendet die `lambda`-Funktion **schrittweise** auf die Werte an.

