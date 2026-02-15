![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

# 💬 WhatsApp Minimal avec Sockets TCP

Un système de messagerie instantanée simplifié développé en Python utilisant les sockets TCP pour illustrer la communication client-serveur.

## 📌 Description

Ce projet est une implémentation éducative d'un système de chat basique similaire à WhatsApp, développé dans le cadre d'un projet académique pour apprendre la programmation réseau avec les sockets TCP.

## ✨ Fonctionnalités

- 🔌 Communication client-serveur via sockets TCP
- 👥 Support multi-clients (plusieurs utilisateurs simultanément)
- 💬 Échange de messages en temps réel
- 🖥️ Interface en ligne de commande (CLI)
- 🎨 Interface graphique moderne (GUI) inspirée de WhatsApp
- 🔒 Déconnexion propre avec commande "quit"
- ⏰ Horodatage des messages (version GUI)

## 🛠️ Technologies Utilisées

- **Python 3.x**
- **socket** - Communication réseau
- **threading** - Gestion multi-clients
- **tkinter** - Interface graphique

## 📦 Installation

### Prérequis

- Python 3.7 ou supérieur installé sur votre machine

### Cloner le dépôt

```bash
git clone https://github.com/votre-username/whatsapp-minimal-tcp.git
cd whatsapp-minimal-tcp
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

> Note : Ce projet utilise uniquement des bibliothèques standard Python, aucune installation supplémentaire n'est nécessaire.

## 🚀 Utilisation

### Version Console

#### 1. Démarrer le serveur

Ouvrez un terminal et exécutez :

```bash
python server.py
```

Le serveur démarre sur `127.0.0.1:5000`

#### 2. Connecter un client

Ouvrez un nouveau terminal et exécutez :

```bash
python client.py
```

#### 3. Échanger des messages

- Tapez votre message et appuyez sur Entrée
- Tapez `quit` pour vous déconnecter proprement

### Version Interface Graphique

#### 1. Démarrer le serveur

```bash
python server.py
```

#### 2. Lancer le client GUI

```bash
python client_gui.py
```

#### 3. Se connecter

- Entrez l'hôte (par défaut : `127.0.0.1`)
- Entrez le port (par défaut : `5000`)
- Cliquez sur "Connecter"
- Échangez des messages via l'interface

## 📁 Structure du Projet

```
whatsapp-minimal-tcp/
│
├── server.py           # Serveur TCP avec support multi-clients
├── client.py           # Client console
├── client_gui.py       # Client avec interface graphique
├── README.md           # Documentation
├── requirements.txt    # Dépendances Python
└── .gitignore         # Fichiers à ignorer par Git
```

## 🔧 Configuration

### Changer l'adresse et le port

Dans `server.py` :

```python
HOST = '127.0.0.1'  # Changez l'adresse IP
PORT = 5000         # Changez le port
```

Dans `client.py` ou `client_gui.py`, ajustez les mêmes valeurs.

## 📖 Concepts Techniques

### Architecture Client-Serveur

- **Serveur** : Écoute les connexions entrantes et gère plusieurs clients simultanément
- **Client** : Initie la connexion et envoie/reçoit des messages

### Protocole TCP

- **Fiabilité** : Garantit la livraison des messages dans l'ordre
- **Connexion** : Établit une connexion avant l'échange de données
- **3-way handshake** : SYN → SYN-ACK → ACK

### Threading

Le serveur utilise des threads pour gérer plusieurs clients en parallèle :

```python
thread = threading.Thread(target=handle_client, args=(conn, addr))
thread.start()
```

## 🎯 Phases du Projet

### Phase 1 : Serveur

- ✅ Création du socket TCP
- ✅ Liaison (bind) à une adresse IP et un port
- ✅ Mise en écoute (listen)
- ✅ Acceptation de connexions
- ✅ Réception et envoi de messages
- ✅ Boucle d'échange jusqu'à "quit"

### Phase 2 : Client

- ✅ Création du socket TCP
- ✅ Connexion au serveur
- ✅ Boucle d'envoi de messages
- ✅ Réception des réponses
- ✅ Déconnexion propre

### Phase 3 : Amélioration

- ✅ Interface graphique (Tkinter)
- ✅ Support multi-clients
- ✅ Horodatage des messages
- ✅ Gestion d'erreurs robuste

## 🐛 Dépannage

### Le serveur ne démarre pas

- Vérifiez que le port 5000 n'est pas déjà utilisé
- Essayez un autre port (ex: 5001, 8080)

### Impossible de se connecter

- Assurez-vous que le serveur est démarré
- Vérifiez l'adresse IP et le port
- Désactivez temporairement le pare-feu
