import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("My Digital Clock")

def time():
    string =strftime("%H: %M: %S %p \n %D")
    label.config(text=string)
    label.after(1000,time)

canvas = tk.Canvas(root, width=300,height=300,background='white')
canvas.pack()
canvas.create_oval(10,10,290,290,fill='aqua',outline='black')

label= tk.Label(canvas,font=('calibri',20,'bold'),background='aqua',foreground='black')
label.place(relx=0.5,rely=0.5,anchor='center')
# label = tk.Label(root,font=('san-sarif',20, 'bold',"italic"),background='aqua',foreground='black')
# label.pack(anchor='center')

time()
root.mainloop()