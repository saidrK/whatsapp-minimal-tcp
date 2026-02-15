import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime

class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp Minimal - Client")
        self.root.geometry("500x600")
        self.root.configure(bg='#075E54')
        
        self.client_socket = None
        self.connected = False
        
        self.setup_ui()
        
    def setup_ui(self):
        """Configure l'interface utilisateur"""
        # Frame de connexion
        self.connection_frame = tk.Frame(self.root, bg='#075E54')
        self.connection_frame.pack(pady=10, padx=10, fill='x')
        
        tk.Label(self.connection_frame, text="Hôte:", bg='#075E54', fg='white').grid(row=0, column=0, padx=5)
        self.host_entry = tk.Entry(self.connection_frame, width=15)
        self.host_entry.insert(0, "127.0.0.1")
        self.host_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(self.connection_frame, text="Port:", bg='#075E54', fg='white').grid(row=0, column=2, padx=5)
        self.port_entry = tk.Entry(self.connection_frame, width=8)
        self.port_entry.insert(0, "5000")
        self.port_entry.grid(row=0, column=3, padx=5)
        
        self.connect_btn = tk.Button(self.connection_frame, text="Connecter", 
                                    command=self.connect, bg='#25D366', fg='white',
                                    font=('Arial', 10, 'bold'))
        self.connect_btn.grid(row=0, column=4, padx=5)
        
        # Zone d'affichage des messages
        self.chat_frame = tk.Frame(self.root, bg='#ECE5DD')
        self.chat_frame.pack(pady=10, padx=10, fill='both', expand=True)
        
        self.chat_display = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD,
                                                    state='disabled', bg='#ECE5DD',
                                                    font=('Arial', 10))
        self.chat_display.pack(fill='both', expand=True)
        
        # Configuration des tags pour le style
        self.chat_display.tag_config('me', foreground='#075E54', font=('Arial', 10, 'bold'))
        self.chat_display.tag_config('other', foreground='#128C7E', font=('Arial', 10, 'bold'))
        self.chat_display.tag_config('system', foreground='#999999', font=('Arial', 9, 'italic'))
        
        # Zone de saisie
        self.input_frame = tk.Frame(self.root, bg='#075E54')
        self.input_frame.pack(pady=10, padx=10, fill='x')
        
        self.message_entry = tk.Entry(self.input_frame, font=('Arial', 12))
        self.message_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
        self.message_entry.bind('<Return>', lambda e: self.send_message())
        self.message_entry.config(state='disabled')
        
        self.send_btn = tk.Button(self.input_frame, text="Envoyer", command=self.send_message,
                                bg='#25D366', fg='white', font=('Arial', 10, 'bold'),
                                state='disabled')
        self.send_btn.pack(side='right')
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def connect(self):
        """Se connecte au serveur"""
        if self.connected:
            messagebox.showwarning("Attention", "Déjà connecté!")
            return
            
        host = self.host_entry.get()
        port = int(self.port_entry.get())
        
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((host, port))
            self.connected = True
            
            self.add_message("Connecté au serveur!", 'system')
            
            # Activer les contrôles
            self.message_entry.config(state='normal')
            self.send_btn.config(state='normal')
            self.connect_btn.config(state='disabled')
            self.host_entry.config(state='disabled')
            self.port_entry.config(state='disabled')
            
            # Démarrer le thread de réception
            receive_thread = threading.Thread(target=self.receive_messages, daemon=True)
            receive_thread.start()
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de se connecter: {e}")
    
    def receive_messages(self):
        """Reçoit les messages du serveur"""
        while self.connected:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.add_message(f"Serveur: {message}", 'other')
                else:
                    break
            except:
                break
        
        self.connected = False
        self.add_message("Déconnecté du serveur", 'system')
    
    def send_message(self):
        """Envoie un message au serveur"""
        message = self.message_entry.get().strip()
        
        if not message:
            return
        
        if not self.connected:
            messagebox.showwarning("Attention", "Non connecté au serveur!")
            return
        
        try:
            self.client_socket.send(message.encode('utf-8'))
            self.add_message(f"Vous: {message}", 'me')
            self.message_entry.delete(0, tk.END)
            
            if message.lower() == 'quit':
                self.disconnect()
                
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur d'envoi: {e}")
            self.disconnect()
    
    def add_message(self, message, tag):
        """Ajoute un message à la zone de chat"""
        self.chat_display.config(state='normal')
        timestamp = datetime.now().strftime("%H:%M")
        self.chat_display.insert(tk.END, f"[{timestamp}] ", 'system')
        self.chat_display.insert(tk.END, f"{message}\n", tag)
        self.chat_display.see(tk.END)
        self.chat_display.config(state='disabled')
    
    def disconnect(self):
        """Déconnecte du serveur"""
        if self.client_socket:
            self.client_socket.close()
        self.connected = False
        
        self.message_entry.config(state='disabled')
        self.send_btn.config(state='disabled')
        self.connect_btn.config(state='normal')
        self.host_entry.config(state='normal')
        self.port_entry.config(state='normal')
    
    def on_closing(self):
        """Gère la fermeture de la fenêtre"""
        if self.connected:
            try:
                self.client_socket.send('quit'.encode('utf-8'))
            except:
                pass
        self.disconnect()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClient(root)
    root.mainloop()