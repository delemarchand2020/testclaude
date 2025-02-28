# Vision Analysis App

Une simple application Python qui envoie une image à l'API OpenAI (GPT-4o) pour analyse et affiche la description détaillée.

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

```bash
python vision_app.py chemin/vers/votre/image.jpg
```

## Fonctionnalités

- Envoi d'images à l'API OpenAI GPT-4o
- Analyse et description détaillée de l'image
- Gestion des erreurs pour les problèmes d'API ou de fichier