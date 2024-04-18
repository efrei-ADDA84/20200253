

# TP3 - Déploiement d'une API météo sur Azure Container Instance

## Introduction

Ce projet vise à déployer une API météo sur Azure Container Instance (ACI) en utilisant GitHub Actions pour automatiser le processus de construction et de déploiement. L'API permet aux utilisateurs de récupérer les données météo en fournissant les coordonnées géographiques.

## Contenu du Repository

- `wrapper.py`: Code de l'API météo.
- `requirements.txt`: Liste des dépendances Python.
- `Dockerfile`: Définition des étapes pour la construction de l'image Docker.
- `.github/workflows`: Répertoire contenant les fichiers de configuration des actions GitHub.

## Fonctionnalités

- L'API permet de récupérer les données météo en fournissant les coordonnées géographiques (latitude et longitude).
- GitHub Actions est utilisé pour automatiser le processus de construction de l'image Docker et de déploiement sur Azure.

## Utilisation

### Prérequis

- Un compte GitHub avec les autorisations pour accéder au repository.
- Un compte Azure avec les autorisations pour créer des ressources (Azure Container Registry et Azure Container Instance).
- Une clé API OpenWeatherMap pour accéder aux données météo.

### Étapes pour l'utilisation

1. **Cloner le Repository :** Clonez ce repository sur votre machine locale en utilisant la commande suivante :
   ```
   git clone <URL_DU_REPOSITORY>
   ```

2. **Configurer les Secrets GitHub :** Dans les paramètres du repository sur GitHub, configurez les secrets suivants :
   - `AZURE_CREDENTIALS`: Informations d'authentification pour Azure.
   - `REGISTRY_LOGIN_SERVER`: Lien de la registry Azure Container Registry.
   - `REGISTRY_USERNAME`: Nom d'utilisateur pour la registry.
   - `REGISTRY_PASSWORD`: Mot de passe pour la registry.
   - `OPENWEATHER_API_KEY`: Clé API OpenWeatherMap pour accéder aux données météo.

3. **Modifier le Code :** Si nécessaire, modifiez le fichier `wrapper.py` pour ajouter votre clé API OpenWeatherMap ou apportez d'autres modifications à l'API selon vos besoins.

4. **Construction de l'Image Docker :** GitHub Actions se déclenchera automatiquement lors d'un push sur la branche principale. Il construira l'image Docker et la poussera vers Azure Container Registry.

5. **Déploiement sur Azure :** Une fois l'image Docker poussée sur Azure Container Registry, GitHub Actions déclenchera le déploiement de l'application sur Azure Container Instance.

6. **Accès à l'API :** Une fois le déploiement terminé, l'API sera accessible via le DNS configuré dans Azure Container Instance. Utilisez les coordonnées géographiques pour récupérer les données météo en accédant à l'URL de l'API.

## Points d'Attention

- Assurez-vous d'avoir configuré correctement les secrets GitHub pour l'authentification avec Azure.
- Vérifiez que la clé API OpenWeatherMap est correctement configurée dans le code de l'API.
