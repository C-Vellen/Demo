# &#8205;&#127891; Projet de chat avec un LLM opensource &#8205;&#127891; 

## &#128203; Généralités :
- python3.12 / django 5.2 
- librairies pytorch et transformers
- base de donnée mysql
- auteur : Christophe Vellen


##  &#8205;&#127891; Démonstration : [ici](https://www.demo.experientiae.fr) [accès protégé par mot de passe]

## &#127919; Objectifs :
- expérimenter un chat avec un LLM opensource, depuis un serveur distant et en utilisant les librairies pytorch et transformers de HuggingFace
 
## &#129520; Fonctionnalités :
- analyse de sentiments avec: distilbert-base-uncased-finetuned-sst-2-english
- génération de texte avec : meta-llama/Llama-3.2-1B-Instruct


## &#128736; Installation : 

- installer pyenv, poetry et python3 v3.12 :
```bash
    curl https://pyenv.run | bash
    curl -sSL https://install.python-poetry.org | python3
    pyenv local 3.12.10
```

- cloner le projet :
```bash
    git clone https://xxxxxxxxx.git
```
- créer une base de donnée Mysql ou Postgresql

- en développement, créer et paramétrer /mooc/mooc/settings/develop.py, ou bien définir des variables d'environnement, et documenter le token d'accès à HuggingFace HF_TOKEN :
    ```bash 
        SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxx'
        DEBUG = True
        ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
        CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8000", "http://localhost:8000"]
        PROTOCOL = "http"
        SITE_ID = 1
        DATABASES = {
            'default':  {
                'ENGINE': 'django.db.backends.postgresql' ou 'django.db.backends.mysql,
                'NAME': 'xxxxxxxxxxxx',
                'USER': 'xxxxxxxxxxxx',
                'PASSWORD': 'xxxxxxxxxxxxx',
                'HOST': '127.0.0.1',
                'PORT': xxxx,
            }
        }
        HF_TOKEN = 'token-à-prendre-sur-HuggingFace'
        
    ``` 
- en production, créer et paramétrer /mooc/mooc/settings/production.py ou bien définir des variables d'environnement, et documenter le token d'accès à HuggingFace HF_TOKEN :
    ```bash 
        SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxx'
        DEBUG = False
        ALLOWED_HOSTS = ['www.xxxxx.xx', ... ]
        CSRF_TRUSTED_ORIGINS = ['https://www.xxxxx.xx', ... ]
        PROTOCOL = 'https'
        SITE_ID = 1
        DATABASES = {
            'default':  {
                'ENGINE': 'django.db.backends.postgresql' ou 'django.db.backends.mysql,
                'NAME': 'xxxxxxxxxxxx',
                'USER': 'xxxxxxxxxxxx',
                'PASSWORD': 'xxxxxxxxxxxxx',
                'HOST': '127.0.0.1',
                'PORT': xxxx,
            }
        }
        STATIC_ROOT = 'chemin vers fichiers statiques sur le serveur'
        MEDIA_ROOT =  'chemin vers fichiers media sur le serveur'
        HF_TOKEN = 'token-à-prendre-sur-HuggingFace'
    ``` 

- installer les dépendances, définies dans le fichier **pyproject.toml** :
    ```bash
        poetry install
    ```
- il est possible que torch ne s'installe pas correctement avec poetry, dans ce cas l'installer avec pip :
    ```bash
        pip install torch
    ```

- activer l'environnement virtuel:
    sur console du serveur, à la racine du projet :
    ```bash 
        source .venv/bin/activate
    ```
    - première migration de la base de donnée :
    ```bash
        ./mooc/manage.py migrate
    ```
    - création du superuser (administrateur):
    ```bash
        ./mooc/manage.py createsuperuser
    ```
    - initialisation tailwind V4:
    ```bash
        ./mooc/manage.py tailwind build
    ```

    - collecte des fichiers statiques (en production) :
    ```bash
        ./mooc/manage.py collectstatic
    ```

    - lancer le serveur (voir ci-dessous), se connecter en tant qu'administrateur et aller sur l'administration django
        

## &#128640; Lancement du serveur de développement :

```bash
    ./mooc/manage.py tailwind dev
```
## &#8505;&#65039; Informations :

        projet en cours d'évolution
    


