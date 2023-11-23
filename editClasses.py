# editClasses.py

import tkinter as tk
from tkinter import ttk

class EditClasses:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.button1 = tk.Button(self.frame, text="Button 1")
        self.button1.pack(side="left")

        self.button2 = tk.Button(self.frame, text="Button 2")
        self.button2.pack(side="left")

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(self.frame, yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side="left", fill="both")

        self.scrollbar.config(command=self.listbox.yview)

        self.load_classes()

    def load_classes(self):
        with open('app_data.txt', 'r') as file:
            classes = file.readlines()

        for class_name in classes:
            self.listbox.insert(tk.END, class_name.strip())

if __name__ == "__main__":
    root = tk.Tk()
    app = EditClasses(root)
    root.mainloop()
