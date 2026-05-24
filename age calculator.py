import tkinter as tk
from datetime import date

def get_age():
    
    age = date.today().year - int(y.get())
    res.config(text="Age: " + str(age))

root = tk.Tk()
root.title("Age Calc")


tk.Label(root, text="Enter Birth Year:").pack()
y = tk.Entry(root)
y.pack()


tk.Button(root, text="Calculate", command=get_age).pack()

res = tk.Label(root, text="")
res.pack()

root.mainloop()
