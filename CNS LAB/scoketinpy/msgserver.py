import socket
# Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8000))
s.listen(5)
while True:
    print("waiting for connection")
    client, addr = s.accept()
    print(f"Connected with {addr}")
    while True:
        clientmsg = client.recv(1024).decode()
        if clientmsg == "I am leaving..":
            print(f"Breaking connection with {addr}")
            client.close()
            break
        print("Client:", clientmsg)
        msg = input("Server:")
        client.send(msg.encode())
