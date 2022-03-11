**Site de critique communautaire de livre**

Ce site permet à un utilisateur de demander une critique sur un livre ou de poster son avis sur une demande de critique

---

## cloner le répertoire

``git clone https://graquil@bitbucket.org/graquil/p9_raquil_giovanni.git``

## activation de l'environnement virtuel

pour préparer le lancement du site veuillez suivre les instructions suivantes dans un terminal.


2. lancer l'environement virtuel :

    1. sous Windows:
        - ``python -m venv env``
        - ``.\env\Scripts\activate``
   
   2. sous Unix:
      - ``python3 -m venv env``
      - ``source env/bin/activate``

3. ``pip install requirement.txt``.

## lancement du serveur

entrer dans le dossier LitReview.

4. `` cd LitReview ``

lancer le serveur.

5. `` python manage.py runserver``