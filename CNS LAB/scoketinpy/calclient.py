import socket

client = socket.socket()
print("Socket Created")
client.connect(("127.0.0.1", 8000))


while True:
    equ = input("Please give me your equation (Ex: 2+2) or Q to quit: ")
    client.send(equ.encode())
    result = client.recv(1024).decode()

    if result == "Quit":
        print("Closing client connection, goodbye")
        break
    elif result == "Error":
        print("There was an error, check your equation")
    else:
        print("The answer is:", result)

client.close()
