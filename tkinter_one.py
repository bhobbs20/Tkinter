
import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry("600x600")
        self.master.title("learning tkinter")


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()