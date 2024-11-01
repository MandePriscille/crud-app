# projet crud django

petit projet de realisation de crud sur une table employee Django CRUD.

## Table des Matières

- [Fonctionnalités](#fonctionnalités)
- [Technologies Utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Utilisation](#utilisation)

## Fonctionnalités

- Création, lecture, mise à jour et suppression (CRUD) d'objets.
- Interface utilisateur simple.
- Validation des données.

## Technologies Utilisées

- [Django](https://www.djangoproject.com/) - Framework web
- [SQLite](https://www.sqlite.org/index.html) - Base de données par défaut (ou autre si différent)
- [HTML/CSS/](https://developer.mozilla.org/fr/docs/Web) - Frontend

## Installation

1. Clonez le dépôt :

  https://github.com/MandePriscille/crud-app.git
  
2. Activez l'environnement virtuel
  source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
3. Installez les dépendances 
  pip install -r requirements.txt
4. Appliquez les migrations 
  python manage.py migrate
5. python manage.py runserver
  python manage.py migrate

## Utilisation
  Accédez à l'application via http://127.0.0.1:8000/.
  Suivez les instructions pour créer, lire, mettre à jour et supprimer des objets.
