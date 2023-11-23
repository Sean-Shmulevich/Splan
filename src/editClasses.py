# src/editClasses.py

import tkinter as tk
from tkinter import ttk

def parse_class_list():
    class_list = []
    with open('app_data.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('class'):
                class_list.append(line.split(':')[1].strip())
    return class_list

def create_scrollable_list(root, class_list):
    frame = tk.Frame(root)
    frame.pack(fill='both', expand=True)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side='right', fill='y')

    listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
    for class_name in class_list:
        listbox.insert('end', class_name)
    listbox.pack(side='left', fill='both', expand=True)

    scrollbar.config(command=listbox.yview)

def create_buttons(root):
    button_frame = tk.Frame(root)
    button_frame.pack(fill='x')

    button1 = tk.Button(button_frame, text='Button 1')
    button1.pack(side='left')

    button2 = tk.Button(button_frame, text='Button 2')
    button2.pack(side='left')

def main():
    root = tk.Tk()
    root.title('Edit Classes')

    create_buttons(root)
    class_list = parse_class_list()
    create_scrollable_list(root, class_list)

    root.mainloop()

if __name__ == '__main__':
    main()
