# Weather Wrapper 

Ce projet est un wrapper météo qui récupère les données météorologiques d'un lieu donné en utilisant l'API OpenWeatherMap.

## Utilisation

### Prérequis

Avant d'utiliser ce projet, assurez-vous d'avoir Python installé sur votre système.

### Installation

1. Clonez ce dépôt :
   
   git clone https://github.com/Ikel0/weather-wrapper.git
   cd weather-wrapper
  

2. Installez les dépendances requises en exécutant :
   
   pip install -r requirements.txt


### Configuration de la clé API OpenWeatherMap

Pour utiliser ce wrapper, vous devez obtenir une clé API auprès d'OpenWeatherMap. Une fois que vous avez votre clé API, vous pouvez la configurer en utilisant une variable d'environnement :

export OPENWEATHER_API_KEY= "dd873b7df67e31543347c06989e163cc"


### Exécution

Pour obtenir les données météorologiques d'un lieu spécifique, exécutez le script `wrapper.py` en spécifiant la latitude et la longitude du lieu :

python wrapper.py

Vous serez invité à entrer la latitude et la longitude du lieu dont vous souhaitez obtenir les données météorologiques.

## Auteur

Ce projet a été créé par Ikel Ouedraogo.
