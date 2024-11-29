import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("MY first gui")

label = tk.Label(root,text="Hello World!", font=('Arial',10))

label.pack(padx=20,pady=20)

textbox=tk.Text(root,height=3,font=('Arial',16))
textbox.pack(padx=10,pady=10)

buttonframe=tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

btn1=tk.Button(buttonframe,text="1",font=('Arial',10))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)
btn1=tk.Button(buttonframe,text="2",font=('Arial',10))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)
btn1=tk.Button(buttonframe,text="3",font=('Arial',10))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)
btn1=tk.Button(buttonframe,text="4",font=('Arial',10))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)
btn1=tk.Button(buttonframe,text="5",font=('Arial',10))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)
btn1=tk.Button(buttonframe,text="6",font=('Arial',10))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)
btn1=tk.Button(buttonframe,text="7",font=('Arial',10))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)
btn1=tk.Button(buttonframe,text="8",font=('Arial',10))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)
btn1=tk.Button(buttonframe,text="9",font=('Arial',10))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)


root.mainloop()