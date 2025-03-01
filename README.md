# Vision Analysis App Web

Une application web qui envoie une image à l'API OpenAI (GPT-4o) pour analyse et affiche la description détaillée. Cette application respecte une architecture standard avec séparation front-end/back-end.

## Architecture

L'application suit une architecture en couches :
- **Frontend** : Interface utilisateur simple en HTML/CSS/JavaScript
- **API** : Endpoints Flask pour communiquer avec le service
- **Services** : Couche de service pour encapsuler la logique métier
- **Backend** : Analyse d'images via l'API OpenAI

## Configuration

1. Clonez ce dépôt
2. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```
3. Créez un fichier `.env` à la racine du projet avec votre clé API OpenAI :
   ```
   OPENAI_API_KEY=votre_clé_api_openai
   ```

## Utilisation

### Application Web
```bash
python app.py
```
Puis ouvrez votre navigateur à l'adresse http://localhost:5000

### Version console (toujours disponible)
```bash
python vision_app.py chemin/vers/votre/image.jpg
```

## Fonctionnalités

- Interface utilisateur intuitive pour télécharger des images
- Prévisualisation des images avant analyse
- Envoi d'images à l'API OpenAI GPT-4o
- Analyse et description détaillée de l'image en français
- Possibilité de personnaliser le prompt d'analyse
- Gestion des erreurs pour les problèmes d'API ou de fichier
- Architecture modulaire et extensible