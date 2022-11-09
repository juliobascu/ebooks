from tkinter import *

class Ventana(Frame):
    def __init__(self,master=None):
        super().__init__(master,width=680, height=260)
        self.master=master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0,width=93, height=259)