import tkinter as tk
import tkinter.ttk as ttk
import asyncio
from threading import Thread

import server as sv

class ConnectionPage(ttk.Frame):
	controller: Optional[object] = None

	def __init__(self, parent, controller: object):
		ttk.Frame.__init__(self, parent)
		self.controller = controller

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(3, weight=1)
		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(5, weight=1)

		label = ttk.Label(self, text="Enter the IP and the PORT of the server")
		label.grid(column=1, columnspan=2, row=1)

		ip_label = ttk.Label(self, text="IP :")
		ip_label.grid(column=1, row=2)

		ip_entry = ttk.Entry(self)
		ip_entry.grid(column=2, row=2)


		port_label = ttk.Label(self, text="PORT :")
		port_label.grid(column=1, row=3)

		port_entry = ttk.Entry(self)
		port_entry.grid(column=2, row=3)


		button = ttk.Button(self, text="Create", command=lambda: self.submit_connection(ip_entry.get(), port_entry.get()))
		button.grid(column=1, columnspan=2, row=4)

	def submit_connection(self, ip, port):
		print("info given :", ip, port)
		sv.server.connection(str(ip), int(port))
		self.controller.show_frame("TextPage")
		self.controller.frames["TextPage"].start_connection()


class TextPage(ttk.Frame):
	controller: Optional[object] = None
	text_box: Optional[tk.Text] = None

	def __init__(self, parent, controller: object):
		ttk.Frame.__init__(self, parent)
		self.controller = controller

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(3, weight=1)
		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(5, weight=1)

		label = ttk.Label(self, text="this is the dummy page")
		label.grid(column=1, columnspan=2, row=1)

		self.text_box = tk.Text(self, state="disabled")
		self.text_box.grid(column=1, columnspan=2, row=2)

	def start_connection(self):
		Thread(target=sv.server.user_connect).start()
		Thread(target=self.update_text).start()

	def update_text(self):
		while True:
			message = sv.server.recieve_data()
			if message != None:
				print("message recieved:", message.decode())
				self.text_box.insert(tk.END, message.decode())


class MainView(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		self.title("Chat App")
		self.geometry("800x600")

		container = ttk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		for F in (ConnectionPage, TextPage):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame

			frame.grid(column=0, row=0, sticky="nsew")

		self.show_frame("ConnectionPage")

	def show_frame(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()

main = MainView()
main.mainloop()