import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
buf = 1024

file_name = input("What file you want to send:")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(file_name.encode(), (UDP_IP, UDP_PORT))
print(f'Send file {file_name}')

f = open(file_name, "r")
data = f.read(buf)
while(data):
    if(sock.sendto(data.encode(), (UDP_IP, UDP_PORT))):
        data = f.read(buf)
        time.sleep(0.02)  # Give receiver a bit time to save

sock.close()
f.close()
