import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(('localhost', 5001))

print("UDP Server waiting for message...")

message, addr = server.recvfrom(1024)

print("Client:", message.decode())

server.sendto("Hello from Server".encode(), addr)

server.close()