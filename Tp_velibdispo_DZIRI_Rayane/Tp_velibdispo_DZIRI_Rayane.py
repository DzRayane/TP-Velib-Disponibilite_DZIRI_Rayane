
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

#Chargement des données
df = pd.read_csv('velib-disponibilite-en-temps-reel.csv', sep=";")

#Explorer les données de manière globale
print("Aperçu des données :")
print(df.head())  # Voir les premières lignes du DataFrame
print("\nInformations générales sur le DataFrame :")
print(df.info())  # Vérifier les types de données et les valeurs manquantes
print("\nDescription statistique des colonnes numériques :")
print(df.describe())

#Nettoyage des données
# Vérifier les valeurs manquantes
print("\nValeurs manquantes dans chaque colonne :")
print(df.isnull().sum())

# Suppression des lignes valeurs manquantes et remplace les valeurs manquantes par des zéros
df = df.fillna(0)

# Convertir les colonnes catégorielles en valeurs numériques
df['Station en fonctionnement'] = df['Station en fonctionnement'].map({'NON': 0, 'OUI': 1})
df['Borne de paiement disponible'] = df['Borne de paiement disponible'].map({'NON': 0, 'OUI': 1})
df['Retour vélib possible'] = df['Retour vélib possible'].map({'NON': 0, 'OUI': 1})





####################################----- Arbre de prediction Station en fonctionnement ou non ------###########################################


X = df[['Capacité de la station', 'Nombre bornettes libres', 'Vélos mécaniques disponibles', 'Vélos électriques disponibles']]
y = df['Station en fonctionnement']  # La colonne cible à prédire

max_depth = 3
clf = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
clf.fit(X, y)

#Visualisation de l'arbre de décision
plt.figure(figsize=(30, 20))
plot_tree(clf, feature_names=X.columns, class_names=['Non opérationnel', 'Opérationnel'], filled=True)
plt.title(f"Arbre de Décision (profondeur max={max_depth})")
plt.show()






####################################------- Arbre de prediction  la disponibilité des vélos--------###########################################

X_bikes = df[['Capacité de la station', 'Nombre bornettes libres', 'Vélos mécaniques disponibles', 'Vélos électriques disponibles']]
y_bikes = ((df['Vélos mécaniques disponibles'] > 0) | (df['Vélos électriques disponibles'] > 0)).astype(int)  # 1 si des vélos sont disponibles, sinon 0

clf_bikes = DecisionTreeClassifier(max_depth=3, random_state=42)
clf_bikes.fit(X_bikes, y_bikes)

# Visualisation de l'arbre de décision pour la disponibilité des vélos
plt.figure(figsize=(30, 20))
plot_tree(clf_bikes, feature_names=X_bikes.columns, class_names=['Pas de vélos', 'Vélos disponibles'], filled=True)
plt.title(f"Arbre de Décision pour la Disponibilité des Vélos (profondeur max=3)")
plt.show()




####################################------- Arbre de prediction  disponibilité des emplacements de stationnement--------###########################################

X_parking = df[['Capacité de la station', 'Nombre bornettes libres', 'Vélos mécaniques disponibles', 'Vélos électriques disponibles']]
y_parking = df['Nombre bornettes libres'] > 0  # 1 si une bornette libre est disponible, sinon 0

clf_parking = DecisionTreeClassifier(max_depth=3, random_state=42)
clf_parking.fit(X_parking, y_parking)

# Visualisation de l'arbre de décision pour la disponibilité des bornettes
plt.figure(figsize=(30, 20))
plot_tree(clf_parking, feature_names=X_parking.columns, class_names=['Pas de bornettes libres', 'Bornettes libres'], filled=True)
plt.title(f"Arbre de Décision pour la Disponibilité des Bornettes (profondeur max=3)")
plt.show()