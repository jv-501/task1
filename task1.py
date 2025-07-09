import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To‑Do List")
        self.tasks = []
        self.build_ui()

    def build_ui(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.entry = tk.Entry(frame, width=40)
        self.entry.grid(row=0, column=0, padx=5)

        add_btn = tk.Button(frame, text="Add", command=self.add_task)
        add_btn.grid(row=0, column=1)

        del_btn = tk.Button(frame, text="Delete", command=self.delete_task)
        del_btn.grid(row=1, column=1, pady=5)

        self.listbox = tk.Listbox(self.root, width=50, height=10)
        self.listbox.pack(pady=5)

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter a task")

    def delete_task(self):
        sel = self.listbox.curselection()
        if sel:
            idx = sel[0]
            self.tasks.pop(idx)
            self.listbox.delete(idx)
        else:
            messagebox.showwarning("Warning", "Select a task to delete")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
