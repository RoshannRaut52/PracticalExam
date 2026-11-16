import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("Hello from Client".encode(), ('localhost', 5001))

message, addr = client.recvfrom(1024)

print("Server:", message.decode())

client.close()