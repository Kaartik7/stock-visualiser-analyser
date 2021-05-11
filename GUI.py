from stocks import visualise
import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
comp_var = tk.StringVar()

def submit():
    name = comp_var.get()
    visualise(name)

name_label = tk.Label(root, text='Company ticker symbol', font=('calibre', 14, 'bold'))

comp_entry = tk.Entry(root, textvariable=comp_var, font=('calibre', 14, 'bold'))
submit_button = tk.Button(root, text='Submit', command=submit)

# method
name_label.grid(row=0, column=0)
comp_entry.grid(row=0, column=1)
submit_button.grid(row=2, column=1)
root.mainloop()
