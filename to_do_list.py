import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self, rang):
        self.root = rang
        self.root.title("Todo List")
        self.tasks = []

        self.task_list_frame = tk.Frame(self.root)
        self.task_list_frame.pack(fill="both", expand=True) 

        self.task_list = tk.Listbox(self.task_list_frame)
        self.task_list.pack(fill="both", expand=True)

        self.new_task_entry = tk.Entry(self.root)
        self.new_task_entry.pack(fill="x")

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(fill="x")

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(fill="x")

        self.clear_all_tasks_button = tk.Button(self.root, text="Clear All Tasks", command=self.clear_all_tasks)
        self.clear_all_tasks_button.pack(fill="x")

    def add_task(self):
        task = self.new_task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert("end", task)
            self.new_task_entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
        except:
            messagebox.showwarning("Warning", "Select a task to delete")

    def clear_all_tasks(self):
        self.tasks = []
        self.task_list.delete(0, "end")

if __name__ == "__main__":
    rang = tk.Tk()
    todo_list = TodoList(rang)
    rang.mainloop()