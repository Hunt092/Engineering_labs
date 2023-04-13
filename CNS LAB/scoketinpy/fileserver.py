import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8000))
s.listen(5)
print("waiting for connection")
while True:
    client, addr = s.accept()
    print(f"Connected with {addr}")
    while True:
        client.send("which file would you like?".encode())
        filename = client.recv(1024).decode().strip() + ".txt"
        # print(filename)
        try:
            fil = open(filename, "rb")
            client.send("sending file data".encode())
            filedata = fil.read(1024)
            # print(filedata)
            client.send(filedata)
            print("sent")
            fil.close()
        except:
            client.send("File not found".encode())
        print("Client", client.recv(1024).decode())
