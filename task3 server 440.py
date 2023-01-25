import random
import socket
import threading

class QOTDServer:
    def __init__(self, host='192.168.150.131', port=8888):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.quotes = [
            "When life give you lemon, you made lemonade.",
            "If your team is throwing, go abandon the game.",
            "Git Gud"
        ]
    def listen(self):
        self.server.listen()
        while True:
            client_socket, client_address = self.server.accept()
            print(f'Connection from {client_address} has been established.')
            client_socket.send(random.choice(self.quotes).encode())
            client_socket.close()
            
    def start(self):
        print(f'Server listening on {self.host}:{self.port}...')
        listen_thread = threading.Thread(target=self.listen)
        listen_thread.start()
        
if __name__ == '__main__':
    server = QOTDServer()
    server.start()
