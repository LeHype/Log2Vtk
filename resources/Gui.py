import tkinter as tk

def add_four_entries():
    global root, my_list_of_entries
    for _ in range(4):
        my_list_of_entries.append(tk.Entry(root))
        my_list_of_entries[-1].pack()

def Inputs():
    root = tk.Tk()
    my_list_of_entries = list()
    tk.Button(root, text="Add 4 more", command=add_four_entries).pack()
    tk.mainloop()