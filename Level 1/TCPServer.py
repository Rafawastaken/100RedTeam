#TCPServer to Receive Messages
#Server

import socket

HOST = "127.0.0.1"
PORT = 9999


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()

    print("[*] Server Running...\n")

    conn, addr = server.accept()
    
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

