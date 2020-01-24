# OC-Pr5-OpenFoodFacts

Programme permettant à un utilisateur de fournir un aliment de substitution plus sain que celui sélectionné.

Basé sur l'API Openfoodfact

## Description du parcours utilisateur

#### L'utilisateur ouvre le programme, les choix suivants sont proposés: 

    Que voulez vous faire ?

    1: Mettre à jour les produits
    2: Rechercher un produit
    3: Consulter les produits sauvegardés
    4: Quit


#### L'utilisateur selectionne le choix 1: 

La base de données sera mise à jour avec les données OFF, cependant une fois les données
chargées il ne sera plus nécessaire de selectionner cette option.

#### L'utilisateur sélectionne 2. 

Le programme proposera les catégories suivantes : 

    1: Confitures de fruits rouges
    2: Pâtes à tartiner aux noisettes
    3: Brioches
    4: Jus de fruits

Bien entendu, il est possible pour l'utilisateur de modifier les catégories produit dans le fichier CONFIG.PY section API prévue à cet éffet, il faudra ensuite procéder à une mise à jour de la base de données.

L'utilisateur selectionne une catégorie, le programme va afficher une liste de 10 produits, l'utilisateur pourra ensuite selectionner le produit désiré.

Le programme retournera le détail du produit, ensuite l'utilisateur devra appuyer sur "entrer" afin d'afficher un substitut si un produit plus sain est disponible.

#### Le programme proprosera ensuite le menu suivant :

    1: Sauvegarder produit(s)
    2: Consulter produit(s)
    3: Supprimer produit(s)
    4: Rechercher un produit
    5: Quit

L'utilisateur suivant son choix, pourra alors choisir de sauvegarder ses produits en base de données si il le souhaite ou bien supprimer des produits précédement enregistrer.

## Pré-requis

Il est nécessaire dans un premier temps de créer une base de donnée "open_ff" et de remplir les informations de connexion à cette dernière dans le fichier CONFIG.PY dans la section DATABASE configuration.

## Lancement

python3 main.py

   

