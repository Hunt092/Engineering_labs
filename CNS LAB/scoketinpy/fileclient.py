import socket

client = socket.socket()
client.connect(("127.0.0.1", 8000))


while True:
    servermsg = client.recv(1024).decode()
    if servermsg == "sending file data":
        file = open("Received.txt", "wb")
        file_data = client.recv(1024)
        print(file_data)
        file.write(file_data)
        file.close()
        print("Finished")

    msg = input("You:")
    if msg == "quit":
        client.send("I am leaving...".encode())
        client.close()
        break
    client.send(msg.encode())
