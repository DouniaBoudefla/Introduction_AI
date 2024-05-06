from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le dataset
df_california=pd.read_csv('california_mod.csv',sep=";")
X = df_california.drop(["MedHouseValue"], axis=1)
y = df_california["MedHouseValue"]

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Définition du modèle RandomForestRegressor
rf_model = RandomForestRegressor()

# Définition de la grille de recherche des hyperparamètres
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False]
}

# Création de l'objet GridSearchCV
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=4, n_jobs=-1, verbose=2)

# Entraînement du modèle
grid_search.fit(X_train, y_train)

# Affichage des meilleurs paramètres
print("Meilleurs paramètres:", grid_search.best_params_)

# Prédiction sur l'ensemble de test
y_pred = grid_search.predict(X_test)

# Calcul de la précision
r2 = r2_score(y_test, y_pred)
print("Coefficient de détermination:", r2)

