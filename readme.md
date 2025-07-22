# Formation Python Avancé

Ce dépôt contient les ressources et notebooks Jupyter pour une formation avancée en Python.

## Structure du projet

```
├── seq1/              # Séquence 1 - Les bases avancées
│   ├── variables.ipynb    # Types de variables et opérations
│   ├── condition.ipynb    # Structures conditionnelles 
│   ├── boucle.ipynb      # Boucles et itérations
│   ├── fonction.ipynb     # Fonctions et paramètres
│   └── module_importation.ipynb # Import et modules
│
├── tools/             # Bibliothèques essentielles
│   ├── Numpy.ipynb       # Calcul numérique avec NumPy
│   ├── Pandas.ipynb      # Manipulation de données avec Pandas
│   ├── Matplotlib.ipynb  # Visualisation avec Matplotlib
│   └── Scikit-learn.ipynb # Machine learning avec Scikit-learn
│
└── environment.yml    # Environnement conda
```

## Prérequis

- Python 3.9+
- Jupyter Notebook
- Les bibliothèques suivantes :
  - NumPy
  - Pandas 
  - Matplotlib
  - Scikit-learn

## Installation

1. Cloner ce dépôt
2. Créer l'environnement conda :
```bash
conda env create -f environment.yml
```
3. Activer l'environnement :
```bash 
conda activate python-advance-env
```

## Contenu

### Séquence 1 : Les bases avancées
- Variables et types de données
- Structures conditionnelles
- Boucles et itérations 
- Fonctions et paramètres
- Import et modules

### Tools : Bibliothèques essentielles
- NumPy : Calcul numérique et tableaux multidimensionnels
- Pandas : Manipulation et analyse de données
- Matplotlib : Visualisation de données
- Scikit-learn : Machine learning et data science

## Utilisation

Les notebooks peuvent être exécutés dans l'ordre avec Jupyter Notebook :

```bash
jupyter notebook
```

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Auteur

By Abdou Khadre DIOP with ❤️