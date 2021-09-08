import socket
import threading

HOST = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

nickname = input("Chose Nickname: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK: ':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error has occurred!")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('ascii'))

def main():
    recieve_thread = threading.Thread(target = receive)
    recieve_thread.start()

    write_thread = threading.Thread(target = write)
    write_thread.start()

if __name__ == '__main__':
    main()
