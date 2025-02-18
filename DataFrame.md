# Pandas-Operationen

Pandas ist eine leistungsstarke Bibliothek in Python, die hauptsächlich für die Datenanalyse und -manipulation verwendet wird. Einige der häufigsten Operationen in Pandas beinhalten das Kombinieren von DataFrames, Filtern, Gruppieren und Transformieren von Daten. Hier konzentrieren wir uns auf die **Join-Operationen**, die es ermöglichen, DataFrames zu kombinieren.

## 1. **Join Operation (Zusammenführen von DataFrames)**

### 1.1 **`merge()`** – Der Standardweg für Joins
Die `merge()`-Funktion in Pandas ist sehr flexibel und ermöglicht es, DataFrames ähnlich wie SQL-Joins zu kombinieren.

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

### 1.2 **`join()`** – Einfacher Join auf Index
Die `join()`-Funktion in Pandas ermöglicht es, DataFrames basierend auf ihren Indizes zu kombinieren.

```python
import pandas as pd

# Beispiel DataFrames
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

df2 = pd.DataFrame({
    'Salary': [5000, 6000, 7000]
})

# Join von df1 und df2 basierend auf ihren Indizes
result = df1.join(df2)
print(result)
```


### 1.3 **`concat()`** – Zusammenführen von DataFrames
Die `concat()`-Funktion in Pandas ermöglicht es, DataFrames entlang einer Achse zu kombinieren.

```python
import pandas as pd

# Beispiel DataFrames
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

df2 = pd.DataFrame({
    'Name': ['David', 'Edward'],
    'Age': [40, 45]
})

# Zusammenführen von df1 und df2 entlang der Zeilen
result = pd.concat([df1, df2])
print(result)
```

