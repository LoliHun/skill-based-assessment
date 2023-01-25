import socket

class QOTDClient:
    def __init__(self, host='192.168.150.131', port=8888):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get_quote(self):
        self.client.connect((self.host, self.port))
        quote = self.client.recv(1024).decode()
        print(f'Received quote: "{quote}"')
        self.client.close()

if __name__ == '__main__':
    client = QOTDClient()
    client.get_quote()
