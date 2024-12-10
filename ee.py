 import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
  tkMessageBox.showwarning("Hello Python", "Hello World")

B = Tkinter.Button(top, text="Hello", command = helloCallBack)
top.mainloop()

import Tkinter
import tkMessageBox
top = Tkinter.Tk()
C = Tkinter.Canvas(top, bg="blue", height=250, width=300)
coord = 100,10,1000,1000
arc = C.create_arc(coord, start=0, extent=150, fill="red")
C.pack()
top.mainloop()