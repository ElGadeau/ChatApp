import socket

s_stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost"
port = 8080

server_address = ((host, port))
s_stream.connect(server_address)

message = "message"

s_stream.sendall(message.encode())

data = s_stream.recv(10)
print(data)

while True:
	print("wait")