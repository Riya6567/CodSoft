import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "todo.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Main App Class
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.config(bg="#f4f4f4")

        self.tasks = load_tasks()

        # Title
        tk.Label(root, text="📌 To-Do List", font=("Arial", 16, "bold"), bg="#f4f4f4").pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(root, font=("Arial", 12))
        self.task_entry.pack(pady=5, fill="x", padx=20)

        # Buttons
        frame = tk.Frame(root, bg="#f4f4f4")
        frame.pack(pady=5)

        tk.Button(frame, text="Add", width=10, command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Update", width=10, command=self.update_task).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Mark Done", width=10, command=self.mark_done).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(frame, text="Delete", width=10, command=self.delete_task).grid(row=1, column=1, padx=5, pady=5)

        # Task List
        self.listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
        self.listbox.pack(pady=10, fill="both", expand=True, padx=20)

        # Load existing tasks
        self.refresh_list()

    # Add a new task
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"task": task, "done": False})
            save_tasks(self.tasks)
            self.refresh_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    # Update selected task
    def update_task(self):
        try:
            index = self.listbox.curselection()[0]
            new_task = self.task_entry.get().strip()
            if new_task:
                self.tasks[index]["task"] = new_task
                save_tasks(self.tasks)
                self.refresh_list()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Task cannot be empty!")
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to update!")

    # Mark task as done
    def mark_done(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks[index]["done"] = True
            save_tasks(self.tasks)
            self.refresh_list()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to mark as done!")

    # Delete a task
    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            del self.tasks[index]
            save_tasks(self.tasks)
            self.refresh_list()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to delete!")

    # Refresh list display
    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✔" if task["done"] else "✘"
            self.listbox.insert(tk.END, f"{task['task']} [{status}]")

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
