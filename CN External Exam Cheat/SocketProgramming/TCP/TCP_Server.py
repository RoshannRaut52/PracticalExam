import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 5000))
server.listen(1)

print("Server waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

message = conn.recv(1024).decode()
print("Client:", message)

conn.send("Hello from Server".encode())

conn.close()
server.close()