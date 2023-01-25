import socket

def main():
    host = "192.168.150.131"
    port = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    fahrenheit = input("Enter temperature in Fahrenheit: ")
    s.send(fahrenheit.encode())

    celsius = s.recv(1024).decode()
    print(f"Temperature in Celsius: {celsius}")

    s.close()

if __name__ == "__main__":
    main()
