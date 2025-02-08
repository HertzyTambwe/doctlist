# doclist

Projet Django qui est couramment appelé ToDo list.

## Models

- Collection
  - name
  - slug
- Taches
  - description
  - collection (ForeignKey)

## Fonctionnalités

- [x] Ajouter une collection
- [x] Supprimer une collection
- [x] Empêcher l'ajout d'une collection en doublon
- [x] Ajouter une tâche (reliée à une collection)
- [x] Supprimer une tâche
- [x] Afficher les tâches d'une collection

## Installation

1. Clonez le dépôt :
    ```sh
    git clone <url-du-depot>
    cd doclist
    ```
    N'oubliez pas de remplacer `<url-du-depot>` par l'URL réelle de votre dépôt Git.

2. Créez et activez un environnement virtuel :
    ```sh
    python -m venv .env
    source .env/bin/activate  # Sur Windows, utilisez `.env\Scripts\activate`
    ```

3. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

4. Appliquez les migrations :
    ```sh
    python manage.py migrate
    ```

5. Lancez le serveur de développement :
    ```sh
    python manage.py runserver
    ```

## Utilisation

- Accédez à l'application via `http://127.0.0.1:8000/`.
- Utilisez l'interface pour ajouter, supprimer et afficher des collections et des tâches.

## Tests

Pour exécuter les tests, utilisez la commande suivante :
```sh
python manage.py test
