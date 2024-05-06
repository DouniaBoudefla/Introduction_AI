from sklearn.datasets import fetch_california_housing
# Charger le dataset
california = fetch_california_housing()
# Séparer les caractéristiques et la variable cible
X, y = california.data, california.target

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Créer un DataFrame à partir des caractéristiques et de la variable cible
df_california = pd.DataFrame(data=california.data, columns=california.feature_names)
df_california['MedHouseValue'] = california.target

## Mener une exploration statistique des donnée : 

# Afficher des informations sur les colonnes
print("\nInfos sur la dataframe:\n")
df_california.info()

# Afficher les premières lignes du DataFrame
print("\nPremières lignes du Datframe:\n")
print(df_california.head())

# Boite à moustache du revenu médian des ménages
sns.boxplot(x='MedHouseValue',data=df_california,palette='winter')
plt.savefig('boxplot_MedHouseValue.png')

# Traitement des valeurs manquantes
pourcentage = df_california.isnull().sum() / len(df_california) * 100
print("\nPoucentage des valeurs manquantes:\n")
print(pourcentage)
sns.heatmap(df_california.notnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.savefig('valeurs_manquantes.png')

# Mesure de corrélation entre les variables
correlation = df_california.corr()
print("\nCorrélation entre les variables\n")
print(correlation)
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.savefig('correlation.png')

# Visualisation du comportement de deux variables selon les modalités de la variable à prédire "MedHouseValue"

# Création de catégories pour 'MedHouseValue' pour la visualisation
df_california['MedHouseValueCat'] = pd.cut(df_california['MedHouseValue'], bins=3, labels=['Bas', 'Moyen', 'Haut'])

# Convertir 'MedInc' en catégories basées sur des quantiles
df_california['MedIncCat'] = pd.qcut(df_california['MedInc'], q=3)

# Convertir 'HouseAge' en catégories basées sur des quantiles
df_california['HouseAgeCat'] = pd.qcut(df_california['HouseAge'], q=3)

# Visualisation pour la première variable 'MedInc'
sns.catplot(x='MedHouseValueCat', col='MedIncCat', kind='count', data=df_california)
plt.savefig('comportement_MedInc_et_MedHouseValue.png')

# Visualisation pour la deuxième variable 'HouseAge'
sns.catplot(x='MedHouseValueCat', col='HouseAgeCat', kind='count', data=df_california)
plt.savefig('comportement_HouseAge_et_MedHouseValue.png')




