import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = int(input("\n[*] Port: "))
host = str(input("[*] Target: "))

def portScanner(port):
    if sock.connect_ex((host, port)):
        print("\n[*] Port %d is closed" %(port))
    else:
        print("\n[*] Port %d is open" %(port))

portScanner(port)
