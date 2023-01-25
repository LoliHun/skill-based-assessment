import socket

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    host = "192.168.150.131"
    port = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"[*] Listening on {host}:{port}")

    conn, addr = s.accept()
    print(f"[*] Connection from {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"[*] Received {data} from {addr}")

        celsius = fahrenheit_to_celsius(float(data))
        conn.send(str(celsius).encode())
        print(f"[*] Sent {celsius} to {addr}")

    conn.close()

if __name__ == "__main__":
    main()
