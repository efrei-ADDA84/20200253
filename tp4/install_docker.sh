#!/bin/bash

# Installation de Docker
sudo apt-get update
sudo apt-get install -y docker.io

# Ajouter l'utilisateur courant au groupe docker pour éviter l'utilisation de sudo
sudo usermod -aG docker ${USER}
