# Installation

Il est recommandé de créer un environnement virtuel pour installer vos packages Python.

Sous Linux :

``` python -m venv venv
    source venv/bin/activate
```

Essayer également avec ```python -m``` au lieu de ```python3 -m```:

``` python -m venv venv
```

Sous Windows c'est quelque peu différent :
<https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html>

Vous pouvez ensuite installer les packages nécessaires en utilisant le fichier ```requirements.txt```.

``` pip install -r requirements.txt
```

# Exécuter le code

Installer les dépendances :

``` pip install -r requirements.txt
```

Puis lancer le jeu :

```
python main.py
```

# Exécuter les testes unitaires

#TODO

# Linter

Vous pouvez exécuter ```flake8``` (à configurer) pour avoir une idée de la qualité de votre code.
```flake8 *.py```

Pour en savoir plus :
<https://flake8.pycqa.org/en/latest/>

