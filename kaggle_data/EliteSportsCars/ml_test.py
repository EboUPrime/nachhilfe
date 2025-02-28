import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

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

# Vorhersagen (auf Basis des Testdatensatzes)
y_pred = model.predict(X_test)

# Evaluierung
print("Klassifikationsbericht:\n", classification_report(y_test, y_pred))

# Benutzerinteraktive Eingabe
print("\nGeben Sie die Symptome ein, um eine Diagnose zu erhalten:")
fieber = int(input("Fieber (1 = Ja, 0 = Nein): "))
husten = int(input("Husten (1 = Ja, 0 = Nein): "))
muedigkeit = int(input("Müdigkeit (1 = Ja, 0 = Nein): "))

# Eingabedaten in ein DataFrame umwandeln
input_data = pd.DataFrame([[fieber, husten, muedigkeit]], columns=['Fieber', 'Husten', 'Müdigkeit'])

# Vorhersage mit dem trainierten Modell
vorhersage = model.predict(input_data)

print(f"\nDiagnose: {vorhersage[0]}")
