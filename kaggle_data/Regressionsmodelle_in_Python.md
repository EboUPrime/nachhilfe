
# Regressionsmodelle in Python

In diesem Dokument werden verschiedene Regressionsmodelle in Python demonstriert, die auf einem Beispiel von Fahrzeugdaten angewendet werden. Wir verwenden `pandas` und `sklearn` Bibliotheken, um verschiedene Regressionsmodelle zu implementieren.

## Beispiel-Daten

Zunächst definieren wir ein Beispiel-Dataset mit Fahrzeugmerkmalen:

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# Beispiel-Daten: Fahrzeugdaten
data = {'Brand': ['Toyota', 'Ford', 'Honda', 'BMW', 'Audi'],
        'Model': ['Corolla', 'Focus', 'Civic', 'X5', 'A4'],
        'Country': ['Japan', 'USA', 'Japan', 'Germany', 'Germany'],
        'Price': [20000, 25000, 23000, 50000, 45000]}
df = pd.DataFrame(data)

# Umwandlung der kategorischen Merkmale in numerische Werte
df['Brand'] = df['Brand'].astype('category')
df['Model'] = df['Model'].astype('category')
df['Country'] = df['Country'].astype('category')

# Speichern der Kategorien, um später zurückzuübersetzen
brand_categories = df['Brand'].cat.categories
model_categories = df['Model'].cat.categories
country_categories = df['Country'].cat.categories

# Umwandlung in numerische Werte
df['Brand'] = df['Brand'].cat.codes
df['Model'] = df['Model'].cat.codes
df['Country'] = df['Country'].cat.codes

# Merkmale und Zielvariable
X = df[['Brand', 'Model', 'Country']]
y = df['Price']

# Aufteilen der Daten in Trainings- und Testdatensatz
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=100)
```

## 1. Lineare Regression (Linear Regression)

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Modell erstellen und trainieren
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
```

## 2. Entscheidungsbaum (Decision Tree Regressor)

```python
from sklearn.tree import DecisionTreeRegressor

# Modell erstellen und trainieren
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Vorhersagen
y_pred = model.predict(X_test)

# Evaluierung (MSE - Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE) des Entscheidungsbaums: {mse}")

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
```

## 3. Random Forest Regressor

```python
from sklearn.ensemble import RandomForestRegressor

# Modell erstellen und trainieren
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Vorhersagen
y_pred = model.predict(X_test)

# Evaluierung (MSE - Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE) des Random Forest: {mse}")

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
```

## 4. Support Vector Regressor (SVR)

```python
from sklearn.svm import SVR

# Modell erstellen und trainieren
model = SVR(kernel='rbf')
model.fit(X_train, y_train)

# Vorhersagen
y_pred = model.predict(X_test)

# Evaluierung (MSE - Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE) des Support Vector Regressors: {mse}")

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
```

## 5. K-Nearest Neighbors Regressor (KNN)

```python
from sklearn.neighbors import KNeighborsRegressor

# Modell erstellen und trainieren
model = KNeighborsRegressor(n_neighbors=5)
model.fit(X_train, y_train)

# Vorhersagen
y_pred = model.predict(X_test)

# Evaluierung (MSE - Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE) des K-Nearest Neighbors: {mse}")

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
```

## 6. Gradient Boosting Regressor

```python
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
    
    print(f'Merkmale - Brand: {brand_name}, Model: {model_name}, Country: {country_name}')
    print(f'Tatsächlicher Preis: {true}, Vorhergesagter Preis: {pred}')
    print()
```

## 7. XGBoost Regressor

```python
import xgboost as xgb

# Modell erstellen und trainieren
model = xgb.XGBRegressor()
model.fit(X_train, y_train)

# Vorhersagen
y_pred = model.predict(X_test)

# Evaluierung (MSE - Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE) des XGBoost: {mse}")

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
```

