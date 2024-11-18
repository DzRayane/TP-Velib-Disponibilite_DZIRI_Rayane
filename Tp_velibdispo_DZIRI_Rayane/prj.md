README pour le projet de classification d'images Pokémon

Introduction

Ce projet vise à construire un réseau de neurones convolutif (CNN) pour la classification d'images de différents Pokémon. Les fichiers pikachu, randouou, et Pokemon contiennent des photos spécifiques à chaque catégorie, servant de base de données pour entraîner et tester le modèle. Le projet est conçu pour explorer le fonctionnement des couches de convolution, clé des CNN, et comprendre leur rôle dans l'extraction de caractéristiques pertinentes des images.

Qu'est-ce qu'une convolution dans les CNN ?
Les CNN sont des types de réseaux de neurones profonds spécialement conçus pour le traitement des données structurées en grille, comme les images. Une couche de convolution applique un filtre (ou noyau) sur l'image d'entrée, faisant ressortir des motifs spécifiques tels que des bords, des textures, ou des formes.

Convolution : Les filtres appliqués glissent sur l'image, calculant des produits scalaires avec des sous-régions de l'image pour produire une carte de caractéristiques.
ReLU (Rectified Linear Unit) : Fonction d'activation utilisée pour ajouter de la non-linéarité.
Pooling (Sous-échantillonnage) : Technique pour réduire la dimension de la carte de caractéristiques, améliorant ainsi l'efficacité et réduisant le surapprentissage.
Explication des étapes du projet

1. Préparation des données
Les dossiers pikachu, randouou, et Pokemon contiennent les images catégorisées selon le type de Pokémon. Ces fichiers sont prétraités pour être compatibles avec le modèle de CNN, comprenant :

Chargement des images
Redimensionnement pour uniformiser la taille
Normalisation des pixels pour que les valeurs soient comprises entre 0 et 1
2. Structure du modèle de CNN
Le modèle est construit avec plusieurs couches, chaque couche jouant un rôle précis :

Couches de convolution : Appliquent des filtres pour extraire des caractéristiques locales des images.
Couches d'activation (ReLU) : Introduisent la non-linéarité.
Couches de pooling : Réduisent la taille des cartes de caractéristiques tout en conservant les informations les plus importantes.
Couches denses (fully connected) : Interprètent les caractéristiques extraites pour effectuer la classification finale.
3. Entraînement du modèle
Le modèle est entraîné avec les images des trois catégories. L'entraînement inclut :

La division des données en ensembles d'entraînement et de validation
Le choix d'une fonction de coût et d'un optimiseur (comme l'entropie croisée et l'optimiseur Adam)
4. Évaluation et résultats
Les performances du modèle sont évaluées sur l'ensemble de validation, et les résultats incluent des métriques telles que l'accuracy et la matrice de confusion.

Explication détaillée du code

Chaque section du code est expliquée pour faciliter la compréhension :

Chargement des bibliothèques : Importation des modules nécessaires tels que TensorFlow/Keras, NumPy, et Matplotlib.
Prétraitement des données : Utilisation de scripts pour lire et préparer les images.
Définition du modèle :
Construction des couches convolutives et denses.
Compilation du modèle avec des paramètres optimaux.
Entraînement et visualisation :
Utilisation de model.fit() pour entraîner le modèle.
Affichage des courbes de perte et d'accuracy pour visualiser l'apprentissage.
Conclusion

Ce projet démontre la puissance des CNN dans le domaine de la classification d'images en montrant comment ils peuvent extraire et apprendre des caractéristiques complexes. Grâce aux étapes détaillées de préparation, construction et évaluation, le modèle est capable de distinguer efficacement entre plusieurs types de Pokémon.