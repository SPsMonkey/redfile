from tkinter import *
import tkinter.font as tf
import tkSimpleDialog
import webbrowser


def glink(event):
    webbrowser.open("https://github.com/SPsMonkey/redfile")

class MyDialog(tkSimpleDialog.Dialog):


    def body(self, master):
        Label(master, text="红头文件生成器").grid(row=0)
        Label(master, text="版本:1.0").grid(row=1)
        ft = tf.Font(family='Fixdsys', size=11, underline=1)
        Label(master, text="github地址:").grid(row=2)
        link=Label(master, text="https://github.com/SPsMonkey/redfile",fg="blue", font=ft,cursor="hand2")
        link.bind("<Button-1>",glink)
        link.grid(row=3)
  


    def apply(self):
        pass


    


