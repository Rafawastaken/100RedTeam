#Create a Chat Server

import socket
import threading

HOST = "127.0.0.1"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)

        except Exception as e:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f"{nickname} left the Chat!".encode('ascii'))
            break

def receive():
    while True:
        client, addr = server.accept()
        print(f"New Connection: {str(addr)}")

        client.send('NICK: '.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of client: {nickname}")
        broadcast(f"{nickname} joined the Chat!".encode('ascii'))
        client.send("Connected to the server".encode("ascii"))

        #Start Threading
        thread = threading.Thread(target = handle, args=(client,))
        thread.start()

def main():
    print("Server is running...")
    receive()


if __name__ == '__main__':
    main()
