import socket

s_stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost"
port = 8080

s_stream.bind((host, port))
s_stream.listen(1)

print("waiting for connection")
connection, client = s_stream.accept()

print(client, "connected")

data = connection.recv(16)
print("recieved", data)
if data:
	connection.sendall(data)
else:
	print("no data from", client)

connection.close()