# Comment j'ai créé une app d'analyse d'images pour 1$ avec Claude Code

Dans un monde où le développement d'applications peut sembler coûteux et complexe, j'ai récemment relevé un défi intéressant : créer une application d'analyse d'images fonctionnelle pour seulement 1 USD. Comment ? Grâce à Claude Code, l'assistant IA en ligne de commande d'Anthropic. Voici mon parcours, des premiers pas à une application web complète.

## L'idée de départ

Tout a commencé par une simple curiosité : pouvais-je créer rapidement une application qui analyse des images à l'aide d'un modèle de vision artificielle ? J'ai décidé d'utiliser GPT-4o d'OpenAI comme modèle de vision et Claude Code comme partenaire de développement.

## Les premiers pas

J'ai commencé par explorer l'environnement avec quelques commandes simples :

```bash
ls -l
écrire une phrase simple genre hello world dans le fichier test.txt
```

Après une petite difficulté avec les permissions d'écriture, j'ai lancé la création de l'application :

```bash
créer une petite app pour tester l'envoi d'une image et son analyse par un modèle de vision
```

Claude Code a immédiatement compris ma demande et a commencé à créer une application console simple. J'ai ensuite précisé le modèle que je souhaitais utiliser :

```bash
je veux que le modèle de vision soit openai gpt-4o
```

## Passage de la console au web

L'application console fonctionnait, mais je voulais quelque chose de plus élégant. J'ai donc demandé à Claude Code :

```bash
je veux que tu modifies cette app qui est en mode console pour avoir une app avec 
une interface web légère pour charger l'image et afficher le résultat. 
je compte sur toi pour que l'architecture respecte les standards de conception : 
front-end, api, back-end, service open ai.
```

En un rien de temps, Claude Code a transformé mon application console en une application web complète avec :
- Une interface utilisateur intuitive pour télécharger des images
- Une API backend pour traiter les requêtes
- Un service dédié pour communiquer avec l'API OpenAI
- Une architecture propre respectant les standards modernes

## Peaufinage et optimisation

Comme dans tout projet de développement, quelques ajustements étaient nécessaires. J'ai remarqué que l'indicateur de chargement (spinner) ne fonctionnait pas correctement :

```bash
ok mais au démarrage quand il n'y a pas d'image on voit le spinner tourner par défaut
```

Après quelques corrections :

```bash
c'est parfait ! petite modif : le spinner est super mais il tourne même quand 
le travail d'analyse est terminé. je veux qu'il tourne uniquement lorsque 
l'analyse est en cours
```

## Gestion du code source avec Git

Pour assurer la pérennité du projet, j'ai demandé à Claude Code de configurer Git :

```bash
je veux mettre cette petite app dans git
```

Claude a créé un dépôt local, puis l'a synchronisé avec mon dépôt distant sur GitHub :

```bash
oui le dépôt est https://github.com/delemarchand2020/testclaude.git
```

Après vérification de la synchronisation, j'ai finalisé le projet en poussant tous les fichiers sur le dépôt distant :

```bash
pousse le tout sur le git distant
```

## Le coût final

Le coût total ? Environ 1 USD, uniquement pour l'utilisation de Claude Code. C'est remarquablement économique pour développer une application d'analyse d'images fonctionnelle avec une interface web.

## Ce que j'ai appris

Cette expérience m'a montré que :
1. Les outils d'IA comme Claude Code peuvent transformer radicalement le processus de développement
2. Même avec un budget minimal, on peut créer des applications fonctionnelles et élégantes
3. La combinaison de différents services d'IA (Claude pour le code, OpenAI pour la vision) offre des possibilités puissantes

Si vous êtes curieux de tester Claude Code ou de développer votre propre application à moindre coût, je vous encourage vivement à essayer cette approche. Le code source complet est disponible sur mon [dépôt GitHub](https://github.com/delemarchand2020/testclaude.git).

Alors, quel sera votre prochain projet à 1 USD ?