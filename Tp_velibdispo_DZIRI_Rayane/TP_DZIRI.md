# TP - Analyse de la Disponibilité des Stations Vélib' avec des Arbres de Décision

## Description
Ce TP consiste à analyser la disponibilité des stations Vélib' à Paris en utilisant des arbres de décision. 
 J'ai construit trois modèles pour prédire différents aspects de la disponibilité des stations :

- **Disponibilité des stations** : Prédire si une station est en fonctionnement ou non.
- **Disponibilité des vélos** : Prédire si des vélos (mécaniques ou électriques) sont disponibles.
- **Disponibilité des bornettes de stationnement** : Prédire si des bornettes de stationnement sont libres.

## Etapes du TP
1. **Chargement des données** : J'ai utilisé un fichier CSV contenant les informations des stations Vélib' en temps réel (open data paris).
2. **Nettoyage des données** : Les valeurs manquantes ont été remplies et les variables catégorielles ont été converties en valeurs numériques.
3. **Création des modèles** : J'ai utilisé des arbres de décision pour prédire la disponibilité des stations, des vélos et des bornettes de stationnement.
4. **Visualisation des arbres** : Chaque modèle a été visualisé sous forme d'un arbre de décision pour observer les critères utilisés dans les prédictions.

## Fichiers du projet
- **velib-disponibilite-en-temps-reel.csv** : Le fichier contenant les données des stations Vélib'.
- **TP_velibdispo.py** : Le script Python exécutant l'analyse et l'entraînement des modèles.
- **README.md** : Ce fichier.
