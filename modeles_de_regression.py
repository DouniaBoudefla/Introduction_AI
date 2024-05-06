from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le dataset
df_california=pd.read_csv('california_mod.csv',sep=";")
X = df_california.drop(["MedHouseValue"], axis=1)
y = df_california["MedHouseValue"]

# Séparation des données en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialisation des modèles
lin_reg = LinearRegression()
lasso_reg = Lasso()
random_forest_reg = RandomForestRegressor()

# Entraînement des modèles
lin_reg.fit(X_train, y_train)
lasso_reg.fit(X_train, y_train)
random_forest_reg.fit(X_train, y_train)

# Prédiction et évaluation du modèle
y_pred_lin = lin_reg.predict(X_test)
y_pred_lasso = lasso_reg.predict(X_test)
y_pred_forest = random_forest_reg.predict(X_test)

acc_log_lin = round(lin_reg.score(X_test,y_test) * 100, 2)
acc_log_lasso = round(lasso_reg.score(X_test,y_test) * 100, 2)
acc_log_forest = round(random_forest_reg.score(X_test,y_test) * 100, 2)

print("\nCoefficient de détermination pour le modèle LinearRegression :")
print(acc_log_lin)
print("\nCoefficient de détermination pour le modèle Lasso :")
print(acc_log_lasso)
print("\nCoefficient de détermination pour le modèle RandomForestRegressor :")
print(acc_log_forest)

