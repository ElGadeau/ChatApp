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
			connection, client = self.s_stream.accept()
			self.connection = connection
			self.client = client
			message = str(self.client) + " connected"
			print("message sent:", message)
			self.connection.sendall(message.encode())

	@classmethod
	def recieve_data(self):
		if not callable(self.connection) :
			return self.connection.recv(16)