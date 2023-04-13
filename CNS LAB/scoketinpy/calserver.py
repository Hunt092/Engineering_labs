import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8000))
s.listen(5)
print("waiting for connection")

while True:
    c, addr = s.accept()
    print("Got connection from", addr)

    while True:
        try:
            equation = c.recv(1024).decode()
            if equation.lower() == "q":
                print(f"Closing the connection {addr}")
                c.send("Quit".encode())
                c.close()
                break
            else:
                print("You gave me the equation:", equation)
                result = eval(equation)
                c.send(str(result).encode())
        except:
            c.send("Error".encode())
       
    c.close()
