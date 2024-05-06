import shap
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le dataset
df_california=pd.read_csv('california_mod.csv',sep=";")
X = df_california.drop(["MedHouseValue"], axis=1)
y = df_california["MedHouseValue"]

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle RandomForestRegressor
random_forest_reg = RandomForestRegressor(n_estimators=300, max_depth=10, random_state=42)
random_forest_reg.fit(X_train, y_train)

# Création de l'expliqueur SHAP
explainer = shap.TreeExplainer(random_forest_reg)

# Calcul des valeurs SHAP
shap_values = explainer.shap_values(X_test)

# Visualisation de l'importance des caractéristiques
shap.summary_plot(shap_values, X_test)
plt.savefig('SHAP.png')

shap.summary_plot(shap_values, X_test, plot_type="bar")
plt.savefig('SHAP_bar.png')
