from tkinter import *
import tab

class Xiaxinwen(tab.tab):
    def body(self, master):
        Label(master, text="文件名:").grid(row=0)
        Label(master, text="文件路径:").grid(row=1)

        self.e1 = Entry(master)
        self.e2 = Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)