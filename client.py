import socket

def start_client():
    """Démarre le client TCP et se connecte au serveur"""
    # Configuration
    HOST = '127.0.0.1'  # Adresse du serveur
    PORT = 5000
    
    # Création du socket TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connexion au serveur
        client.connect((HOST, PORT))
        print(f"[CONNECTÉ] Connexion établie avec {HOST}:{PORT}")
        print("Tapez 'QUIT' pour vous déconnecter\n")
        
        # Boucle d'échange de messages
        while True:
            # Saisie du message par l'utilisateur
            message = input("Vous: ")
            
            # Envoi du message au serveur
            client.send(message.encode('utf-8'))
            
            # Si l'utilisateur tape QUIT, on sort de la boucle
            if message.lower() == 'quit':
                # Réception du message d'au revoir du serveur
                reponse = client.recv(1024).decode('utf-8')
                print(f"Serveur: {reponse}")
                print("\n[DÉCONNEXION] Connexion fermée.")
                break
            
            # Réception de la réponse du serveur
            reponse = client.recv(1024).decode('utf-8')
            
            if not reponse:
                print("[ERREUR] Le serveur a fermé la connexion.")
                break
                
            print(f"Serveur: {reponse}\n")
            
            # Si le serveur envoie quit, on ferme la connexion
            if reponse.lower() == 'quit':
                print("\n[DÉCONNEXION] Le serveur a fermé la connexion.")
                break
                
    except ConnectionRefusedError:
        print("[ERREUR] Impossible de se connecter au serveur.")
        print("Vérifiez que le serveur est démarré.")
    except Exception as e:
        print(f"[ERREUR] {e}")
    finally:
        # Fermeture propre du socket
        client.close()

if __name__ == "__main__":
    print("="*50)
    print("CLIENT DE MESSAGERIE TCP")
    print("="*50)
    start_client()