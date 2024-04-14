## Rapport TP2 - Configuration d'une API Flask et déploiement sur Docker Hub


Le TP2 avait pour objectif de configurer une API Flask pour récupérer les données météorologiques à partir de l'API OpenWeatherMap, de transformer cette API en une image Docker, et de la publier sur Docker Hub. Le déploiement automatique devait être géré via GitHub Actions.

### Objectifs
Les principaux objectifs étaient :
1. Configurer une API Flask pour récupérer les données météorologiques.
2. Transformer l'API Flask en une image Docker.
3. Publier l'image Docker sur Docker Hub.
4. Automatiser le processus de construction et de déploiement avec GitHub Actions.

### Étapes réalisées
1. **Configuration de l'API Flask :**
    - Création d'une application Flask avec une route `/weather`.
    - Intégration de l'API OpenWeatherMap pour obtenir les données météorologiques actuelles.

2. **Écriture du Dockerfile :**
    - Rédaction d'un Dockerfile pour empaqueter l'application Flask dans une image Docker.
    - Installation des dépendances requises pour l'application Flask.

3. **Configuration de GitHub Actions :**
    - Mise en place d'un flux de travail GitHub Actions pour automatiser la construction et le déploiement de l'image Docker sur Docker Hub.
    - Utilisation de secrets GitHub pour sécuriser les informations sensibles.

4. **Publication sur Docker Hub :**
    - Publication de l'image Docker sur Docker Hub pour la rendre accessible au public.

### Difficultés rencontrées
1. **Configuration de l'API Flask :**
    - Gestion des erreurs de requête vers l'API OpenWeatherMap.
    - Manipulation des données de réponse pour les formater correctement.

2. **Configuration de GitHub Actions :**
    - Compréhension de la syntaxe YAML pour définir les étapes du flux de travail.
    - Gestion des autorisations et des secrets pour accéder à Docker Hub.

### Résultats obtenus
- L'API Flask a été correctement configurée et fonctionne comme prévu.
- L'image Docker a été construite avec succès et publiée sur Docker Hub.
- Le flux de travail GitHub Actions est opérationnel et gère automatiquement le processus de construction et de déploiement.


### Liens utiles
- [Dépôt GitHub](https://github.com/efrei-ADDA84/20200253)
- [Docker Hub](https://hub.docker.com/repository/docker/ikel2777/weather-api/general)
