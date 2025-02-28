import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Daten einlesen
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

# Umwandlung der Merkmale in numerische Werte
df['Brand'] = df['Brand'].cat.codes
df['Model'] = df['Model'].cat.codes
df['Country'] = df['Country'].cat.codes
df['Transmission'] = df['Transmission'].cat.codes

# Umwandlung der Zielvariable 'Market_Demand' (kategorisch) in numerische Werte
df['Market_Demand'] = df['Market_Demand'].astype('category')  # Sicherstellen, dass es den 'category' Typ hat
market_demand_categories = df['Market_Demand'].cat.categories
df['Market_Demand'] = df['Market_Demand'].cat.codes

# Merkmale und Zielvariable
X = df[['Brand', 'Model', 'Country', 'Transmission']]
y = df['Market_Demand']

# Aufteilen der Daten in Trainings- und Testdatensatz
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modell erstellen und trainieren (Random Forest Regressor)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Vorhersagen für den Testdatensatz
y_pred = model.predict(X_test)

# Evaluierung (MSE - Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE) des Random Forest Modells: {mse}")

# Ausgabe der Vorhersagen und tatsächlichen Werte
for idx, (true, pred) in enumerate(zip(y_test, y_pred)):
    brand_code = X_test.iloc[idx]['Brand']
    model_code = X_test.iloc[idx]['Model']
    country_code = X_test.iloc[idx]['Country']
    transmission_code = X_test.iloc[idx]['Transmission']

    # Umwandlung der numerischen Werte zurück in Text
    brand_name = brand_categories[brand_code]
    model_name = model_categories[model_code]
    country_name = country_categories[country_code]
    transmission_name = transmission_categories[transmission_code]
    market_demand_name = market_demand_categories[true]

    print(
        f'Merkmale - Brand: {brand_name}, Model: {model_name}, Country: {country_name}, Transmission: {transmission_name}')
    print(
        f'Tatsächlicher Marktbedarf: {market_demand_name}, Vorhergesagter Marktbedarf: {market_demand_categories[int(pred)]}')
    print()
