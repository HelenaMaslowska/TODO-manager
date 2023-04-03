import random
from tkinter import *
from tkinter.ttk import Style

list_of_tasks = []

class TODO(Frame):
	def __init__(self, root):
		Frame.__init__(self, root, bg="red")
		self.root = root
		mylabel = Label(root, text="TODO manager")
		mylabel.grid(row=0, column=1)
		self.input = Input(root)
		self.input.input.grid(row=1, column=1)
		self.add_button = Button(root, text="Add", command=self.add_task)
		self.add_button.grid(row=1, column=2)
		self.list = TODOList(root)

	def add_task(self):
		list_of_tasks.append(Task(random.random(), self.input.input.get(), "Description", "Due Date", "Priority", 2))

class TODOList(Frame):
	def __init__(self, root):
		Frame.__init__(self, root, bg="blue")
		self.root = root
		print(list_of_tasks)
	
	def create_tasks(self):
		for i in list_of_tasks:
			Task(i, "Task " + str(i), "Description", "Due Date", "Priority", i).grid(row=i, column=1)

class Input(Frame):
	def __init__(self, root):
		Frame.__init__(self, root, bg="green")
		self.root = root
		self.input = Entry(root)

class Task(Frame):
	def __init__(self, id, name, description, due_date, priority, n):
		Frame.__init__(self, root, bg="yellow", height=70, width=400)
		Checkbutton(root, text=name).grid(row=n, column=n)
		print(n)
		self.id = id
		self.name = name
		self.description = description
		self.due_date = due_date
		self.priority = priority


if __name__ == "__main__":
	root = Tk()
	root.geometry("1280x720")
	todo = TODO(root)
	root.mainloop()
