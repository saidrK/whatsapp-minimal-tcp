import socket
import threading

def handle_client(conn, addr):
    """Gère la communication avec un client connecté"""
    print(f"[NOUVELLE CONNEXION] {addr} connecté.")
    
    connected = True
    while connected:
        try:
            # Réception du message du client
            message = conn.recv(1024).decode('utf-8')
            
            if not message:
                break
                
            print(f"\n[{addr}] Client: {message}")
            
            # Vérifier si le client veut quitter
            if message.lower() == 'quit':
                print(f"[DÉCONNEXION] {addr} s'est déconnecté.")
                conn.send("Au revoir!".encode('utf-8'))
                connected = False
                break
            
            # Le serveur saisit une réponse
            reponse = input("Serveur: ")
            conn.send(reponse.encode('utf-8'))
            
            # Si le serveur tape quit, fermer la connexion
            if reponse.lower() == 'quit':
                print(f"[FERMETURE] Fermeture de la connexion avec {addr}")
                connected = False
                
        except Exception as e:
            print(f"[ERREUR] {e}")
            connected = False
    
    conn.close()

def start_server():
    """Démarre le serveur TCP"""
    # Configuration
    HOST = '127.0.0.1'  # Localhost
    PORT = 5000
    
    # Création du socket TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Liaison du socket à l'adresse et au port
    server.bind((HOST, PORT))
    
    # Mise en mode écoute (max 5 connexions en attente)
    server.listen(5)
    print(f"[DÉMARRAGE] Serveur en écoute sur {HOST}:{PORT}")
    
    try:
        while True:
            # Accepter une connexion entrante
            conn, addr = server.accept()
            
            # Gérer le client dans un thread séparé (pour supporter plusieurs clients)
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[CONNEXIONS ACTIVES] {threading.active_count() - 1}")
            
    except KeyboardInterrupt:
        print("\n[ARRÊT] Arrêt du serveur...")
    finally:
        server.close()

if __name__ == "__main__":
    print("="*50)
    print("SERVEUR DE MESSAGERIE TCP")
    print("="*50)
    start_server()