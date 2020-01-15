from tkinter import *

#create a blanket window
root = Tk()
# label = Label(root, text = "Hello World")
# label.pack()

# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side = BOTTOM)

# button1 = Button(topFrame, text = "Button1", fg = "red")
# button2 = Button(topFrame, text = "Button2", fg = "orange")
# button3 = Button(topFrame, text = "Button3", fg = "yellow")
# button4 = Button(bottomFrame, text = "Button4", fg="green")
# button1.pack(side = LEFT)
# button2.pack(side = LEFT)
# button3.pack(side = LEFT)
# button4.pack(side = BOTTOM)

name = Label(root, text="Name")
passwd = Label(root, text="Password")
name_in = Entry(root)
passwd_in = Entry(root)

name.grid(row=0, sticky=E)
passwd.grid(row=1, sticky=E)
name_in.grid(row=0, column=1)
passwd_in.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me Login")
c.grid(columnspan=2)

#make sure your window constantly displayed
root.mainloop()
