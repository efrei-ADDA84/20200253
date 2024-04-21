### Rapport de Projet - Déploiement d'une Infrastructure avec Terraform sur Azure

---

#### **Introduction**

Ce rapport présente en détail le processus de déploiement d'une infrastructure sur Microsoft Azure en utilisant Terraform. L'objectif de ce projet est de mettre en place une architecture cloud automatisée et reproductible pour répondre aux besoins d'une application ou d'un service.

---

#### **Étape 1: Configuration de l'Environnement**

###### 1. Installation de Terraform

Si Terraform n'est pas encore installé sur votre machine, vous pouvez l'installer en utilisant Homebrew sur macOS ou en téléchargeant le binaire depuis le site officiel.

```bash
# Installation de Terraform avec Homebrew (sur macOS)
brew install terraform
```

###### 2. Configuration de l'accès à Azure

Connectez-vous à votre compte Azure en utilisant l'Azure CLI.

```bash
az login
```


---

#### **Étape 2: Création des Fichiers de Configuration Terraform**

1. **Fichier provider.tf**:
   - Le fichier `provider.tf` contient la configuration du fournisseur Azure, spécifiant la région et les informations d'authentification.

2. **Fichier main.tf**:
   - Le fichier `main.tf` définit les ressources Azure telles que les réseaux, les machines virtuelles, les groupes de ressources, etc.
   - Utilisation des ressources de données Azure pour récupérer des informations existantes.

3. **Fichier output.tf**:
   - Le fichier `output.tf` définit les sorties pour afficher les informations utiles après le déploiement.

4. **Fichier data.tf** (éventuellement)**
   - Utilisation des ressources de données pour récupérer des informations existantes sur Azure, telles que les sous-réseaux, les groupes de sécurité réseau, etc.

---

#### **Étape 3: Exécution de Terraform**

1. **Initialisation du Projet Terraform**:
   ```bash
   terraform init
   ```

2. **Validation des Changements**:
   ```bash
   terraform plan
   ```

3. **Application des Changements**:
   ```bash
   terraform apply
   ```

---

#### **Étape 4: Configuration supplémentaire avec Cloud-Init**

1. **Création du script Install_docker.sh**:
   ```bash
   # Contenu du script d'installation de Docker
   ```

2. **Utilisation de Cloud-Init pour exécuter le script au démarrage**:
   - Intégration du script `Install_docker.sh` dans la configuration de la machine virtuelle pour installer Docker automatiquement lors du démarrage.

---

#### **Étape 5: Finalisation du projet Terraform**

1. **Exécution de Terraform fmt pour formater le code**:
   ```bash
   terraform fmt
   ```

2. **Validation et application des changements**:
   - Exécution de `terraform plan` pour valider les changements proposés et `terraform apply` pour les appliquer.

3. **Génération des clés SSH et autorisation d'accès**:
   -Génération de la Clé SSH Privée: terraform output -raw tls_private_key > id_rsa

   - Création des clés SSH avec `ssh-keygen` et modification des permissions avec `sudo chmod 600 id_rsa` pour sécuriser l'accès.

4. **Connexion à la machine virtuelle via SSH**:
    _Récupération de l'Adresse IP Publique: terraform output public_ip_address

   - Utilisation de la clé SSH pour se connecter à la machine virtuelle avec `ssh -v -i id_rsa username@public_ip_address`

---

#### **Conclusion**

Ce rapport a détaillé le processus complet de déploiement d'une infrastructure sur Microsoft Azure en utilisant Terraform. Chaque étape, depuis la configuration de l'environnement jusqu'à l'installation de Docker avec Cloud-Init, a été présentée en détail. Ce projet a permis d'acquérir une compréhension approfondie de Terraform et de son utilisation pour la gestion automatisée des infrastructures cloud.

# Déploiement d'une machine virtuelle sur Azure avec Terraform

## Prérequis
- Terraform installé localement
- Accès à un compte Azure avec Azure CLI configuré


## Étapes
1. Cloner ce dépôt Git localement.
2. Créer un fichier `terraform.tfvars` contenant les variables nécessaires.
3. Exécuter `terraform init` pour initialiser Terraform.
4. Exécuter `terraform plan` pour voir les changements proposés.
5. Exécuter `terraform apply` pour déployer les ressources sur Azure.
6. Une fois le déploiement terminé, l'adresse IP publique de la machine virtuelle sera affichée.
7. Vous pouvez vous connecter à la machine virtuelle à l'aide de SSH : `ssh -i id_rsa devops@<IP_PUBLIQUE>`.

## Configuration supplémentaire
- Pour installer Docker automatiquement au démarrage, modifiez le script `install_docker.sh` selon vos besoins et mettez-le à jour dans le fichier Terraform `main.tf`.


