import socket

class server():
	s_stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = ""
	port = 0
	server_open = True
	connection: socket.socket
	connection: tuple

	@classmethod
	def connection(self, ip, port):
		self.host = ip
		self.port = port
		print("IP:", self.host)
		print("PORT:", self.port)
		self.s_stream.bind((self.host, self.port))


	@classmethod
	def user_connect(self):
		self.s_stream.listen()
		print("Waiting for connection")
		while self.server_open:
			self.connection, self.client = self.s_stream.accept()
			print(self.client, "connected")

	def recieve_data(self):
		data = self.connection.recv(16)

#	@classmethod
#	async def message_loop(self):


#	s_stream.listen(1)

#	print("waiting for connection")

#	connection, client = s_stream.accept()

#	print(client, "connected")

#	data = connection.recv(16)
#	print("recieved", data)
#	if data:
#		connection.sendall(data)
#	else:
#		print("no data from", client)

#	connection.close()