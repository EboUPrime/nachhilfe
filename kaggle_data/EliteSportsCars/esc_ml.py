import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# https://www.kaggle.com/datasets/wlwwwlw/elite-sports-cars-in-data/data

df = pd.read_csv('Elite Sports Cars in Data.csv')

# Umwandlung der kategorischen Merkmale in numerische Werte
df['Brand'] = df['Brand'].astype('category')
df['Model'] = df['Model'].astype('category')
df['Country'] = df['Country'].astype('category')
df['Transmission'] = df['Transmission'].astype('category')

# Speichern der Kategorien, um später zurückzuübersetzen
brand_categories = df['Brand'].cat.categories
model_categories = df['Model'].cat.categories
country_categories = df['Country'].cat.categories
transmission_categories = df['Transmission'].cat.categories

# Umwandlung in numerische Werte
df['Brand'] = df['Brand'].cat.codes
df['Model'] = df['Model'].cat.codes
df['Country'] = df['Country'].cat.codes
df['Transmission'] = df['Transmission'].cat.codes

# Merkmale und Zielvariable
X = df[['Brand', 'Model', 'Country', 'Transmission']]
y = df['Price']

# Aufteilen der Daten in Trainings- und Testdatensatz
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=100)

from sklearn.ensemble import GradientBoostingRegressor

# Modell erstellen und trainieren
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Vorhersagen
y_pred = model.predict(X_test)

# Evaluierung (MSE - Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE) des Gradient Boosting: {mse}")

# Ausgabe der Vorhersagen
for idx, (true, pred) in enumerate(zip(y_test, y_pred)):
    brand_code = X_test.iloc[idx]['Brand']
    model_code = X_test.iloc[idx]['Model']
    country_code = X_test.iloc[idx]['Country']

    # Umwandlung der numerischen Werte zurück in Text
    brand_name = brand_categories[brand_code]
    model_name = model_categories[model_code]
    country_name = country_categories[country_code]
    transmission_name = transmission_categories[country_code]

    print(f'Merkmale - Brand: {brand_name}, Model: {model_name}, Country: {country_name}')
    print(f'Tatsächlicher Preis: {true}, Vorhergesagter Preis: {pred}')
    print()












"""

model = LinearRegression()
model.fit(X_train, y_train)

# Vorhersagen
y_pred = model.predict(X_test)

# Evaluierung (MSE - Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE) der Linearen Regression: {mse}")

# Ausgabe der Vorhersagen
for idx, (true, pred) in enumerate(zip(y_test, y_pred)):
    brand_code = X_test.iloc[idx]['Brand']
    model_code = X_test.iloc[idx]['Model']
    country_code = X_test.iloc[idx]['Country']

    # Umwandlung der numerischen Werte zurück in Text
    brand_name = brand_categories[brand_code]
    model_name = model_categories[model_code]
    country_name = country_categories[country_code]

    print(f'Merkmale - Brand: {brand_name}, Model: {model_name}, Country: {country_name}')
    print(f'Tatsächlicher Preis: {true}, Vorhergesagter Preis: {pred}')
    print()
"""
"""
# Entscheidungsbaum für Regression
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Vorhersagen (auf Basis des Testdatensatzes)
y_pred = model.predict(X_test)

# Evaluierung (MSE - Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse}")

# Vorhersagen für den Testdatensatz
print("\nVorhersagen für den Testdatensatz:")
for idx, (true, pred) in enumerate(zip(y_test, y_pred)):
    # Ausgabe der Merkmale und der Vorhersage
    brand_code = X_test.iloc[idx]['Brand']
    model_code = X_test.iloc[idx]['Model']
    country_code = X_test.iloc[idx]['Country']

    # Umwandlung der numerischen Werte zurück in kategorische Werte
    brand_name = brand_categories[brand_code]
    model_name = model_categories[model_code]
    country_name = country_categories[country_code]

    # Ausgabe der Merkmale und Preise
    print(f'Merkmale - Brand: {brand_name}, Model: {model_name}, Country: {country_name}')
    print(f'Tatsächlicher Preis: {true}, Vorhergesagter Preis: {pred}')
    print()

"""