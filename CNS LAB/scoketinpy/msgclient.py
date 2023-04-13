import socket
# Client
client = socket.socket()
print("Socket Created")
client.connect(("127.0.0.1", 8000))


name = input("Enter your name:")
client.send(name.encode())
while True:
    print("Server:", client.recv(1024).decode())
    msg = input("You:")
    if msg.lower() == "quit":
        client.send("I am leaving..".encode())
        break
    client.send(msg.encode())
client.close()
