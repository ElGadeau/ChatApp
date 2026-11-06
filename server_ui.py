import tkinter as tk
import tkinter.ttk as ttk

class ConnectionPage(ttk.Frame):
	def __init__(self, parent, controller):
		ttk.Frame.__init__(self, parent)
		self.controller = controller

		label = ttk.Label(self, text="this is the connection page")
		label.pack()
		
		button = ttk.Button(self, text="page 2", command=lambda: controller.show_frame("DummyPage"))
		button.pack()

class DummyPage(ttk.Frame):
	def __init__(self, parent, controller):
		ttk.Frame.__init__(self, parent)
		self.controller = controller

		label = ttk.Label(self, text="this is the dummy page")
		label.pack()

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
		for F in (ConnectionPage, DummyPage):
			page_name = F.__name__
			print(page_name)
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame

			frame.grid(column=0, row=0, sticky="nsew")

		self.show_frame("ConnectionPage")

	def show_frame(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()

main = MainView()
main.mainloop()