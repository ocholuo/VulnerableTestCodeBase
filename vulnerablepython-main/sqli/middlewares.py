import socket

def connect_to_server(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    buf = s.recv(2048)
    print("Received:", buf.decode())

if __name__ == "__main__":
    connect_to_server("127.0.0.1", 1234)