# **Python-Nachhilfe für Anfänger & Fortgeschrittene**

## **1. Datentypen in Python**
Python bietet verschiedene Datentypen, die für unterschiedliche Anwendungen genutzt werden können. Hier sind die wichtigsten:

### **1.1 Grundlegende Datentypen**

#### **Integer (int)** - Ganzzahlen
```python
x = 10  # Eine ganze Zahl
print(type(x))  # Ausgabe: <class 'int'>
```

#### **Float (float)** - Gleitkommazahlen
```python
x = 3.14  # Eine Fließkommazahl
print(type(x))  # Ausgabe: <class 'float'>
```

#### **String (str)** - Zeichenketten
```python
text = "Hallo, Python!"
print(type(text))  # Ausgabe: <class 'str'>
```

#### **Boolean (bool)** - Wahrheitswerte
```python
wahr = True
falsch = False
print(type(wahr))  # Ausgabe: <class 'bool'>
```

### **1.2 Komplexe Datentypen**

#### **Listen (list)** - Geordnete Sammlung von Werten
```python
zahlen = [1, 2, 3, 4, 5]
print(type(zahlen))  # Ausgabe: <class 'list'>
```

#### **Tupel (tuple)** - Unveränderliche Listen
```python
tupla = (10, 20, 30)
print(type(tupla))  # Ausgabe: <class 'tuple'>
```

#### **Dictionaries (dict)** - Schlüssel-Wert-Paare
```python
daten = {"Name": "Max", "Alter": 25}
print(type(daten))  # Ausgabe: <class 'dict'>
```

#### **Mengen (set)** - Ungeordnete, einzigartige Werte
```python
zahlen_menge = {1, 2, 3, 4, 5}
print(type(zahlen_menge))  # Ausgabe: <class 'set'>
```

## **2. Kombination von Datentypen & häufige Fehler**

### **2.1 Kombinationen verschiedener Typen**

#### **Kombination von Strings und Zahlen**
```python
zahl = 5
text = "Das Ergebnis ist: " + str(zahl)  # Explizite Umwandlung nötig
print(text)  # Ausgabe: Das Ergebnis ist: 5
```

#### **Listen mit verschiedenen Typen**
```python
mix = [1, "Hallo", 3.14, True]
print(mix)  # Ausgabe: [1, 'Hallo', 3.14, True]
```

#### **Dictionary mit unterschiedlichen Werten**
```python
daten = {"Name": "Lisa", "Alter": 30, "Hobbies": ["Lesen", "Sport"]}
print(daten["Hobbies"])  # Zugriff auf Liste im Dictionary
```

### **2.2 Häufige Fehler bei Datentypen**

#### **Addition von String und Zahl (TypeError)**
```python
zahl = 10
text = "Alter: "
# print(text + zahl)  # TypeError: can only concatenate str (not "int") to str
```
**Lösung:** Explizite Typumwandlung:
```python
print(text + str(zahl))  # Ausgabe: Alter: 10
```

#### **Zugriff auf nicht vorhandene Dictionary-Schlüssel (KeyError)**
```python
daten = {"Name": "Max", "Alter": 25}
# print(daten["Adresse"])  # KeyError: 'Adresse'
```
**Lösung:**
```python
print(daten.get("Adresse", "Nicht vorhanden"))  # Ausgabe: Nicht vorhanden
```

#### **Ändern eines Tupels (TypeError)**
```python
tupla = (1, 2, 3)
# tupla[0] = 10  # TypeError: 'tuple' object does not support item assignment
```
**Lösung:** Ein neues Tupel erstellen:
```python
tupla = (10,) + tupla[1:]
print(tupla)  # Ausgabe: (10, 2, 3)
```

## **3. String-Manipulation in Python**
### **Wichtige Methoden zur Bearbeitung von Strings**  
```python
text = "   Hallo, Python!   "

# Groß- und Kleinschreibung ändern
print(text.upper())  # "   HALLO, PYTHON!   "
print(text.lower())  # "   hallo, python!   "

# Leerzeichen entfernen
print(text.strip())  # "Hallo, Python!"
print(text.lstrip())  # "Hallo, Python!   "
print(text.rstrip())  # "   Hallo, Python!"
```

## **4. Fortgeschrittene Mathematik mit Python**
### **4.1 Grundlegende mathematische Funktionen**
```python
import math

print(math.sqrt(16))  # Quadratwurzel: 4.0
print(math.pow(2, 3))  # Potenz: 8.0
print(math.factorial(5))  # Fakultät: 120
print(math.log(100, 10))  # Logarithmus: 2.0
```

## **5. Reguläre Ausdrücke (Regex) in Python**
### **Grundlagen von Regex**
```python
import re

text = "Meine Telefonnummer ist 0176-12345678."

# Telefonnummer finden
muster = r"\d{4}-\d{8}"
treffer = re.search(muster, text)
if treffer:
    print("Gefundene Nummer:", treffer.group())  # 0176-12345678
```

## **6. Python-Nachhilfe für Anfänger: Ideen & Projekte**
### **6.1 Einführung in Python: Die ersten Schritte**
📌 **Themen:**
- Installation von Python & einer IDE (z. B. Thonny, VS Code)
- Die erste `print()`-Anweisung
- Kommentare in Python

🛠 **Mini-Projekt:**
```python
name = input("Wie heißt du? ")
print("Hallo", name, "Willkommen in der Welt von Python!")
```

## **Quellen & Weiterführende Links**
- [Python Dokumentation](https://docs.python.org/3/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Real Python](https://realpython.com/)

