from tkinter import  *

class tab(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        body = Frame(self,height=2, bd=1, relief="sunken")
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)
        self.maintext()
        self.buttonbox()


    def body(self, master):

        pass

    def maintext(self):
        Label(self, text="正文:").pack(side='top', anchor='sw')
        box=Frame(self)
        scrollbar = Scrollbar(box)
        scrollbar.pack(side=RIGHT, fill=Y)
        text=Text(box,width=30,height=10,yscrollcommand=scrollbar.set)
        text.pack( expand='yes', fill='x',padx=5,pady=5)
        scrollbar.config(command=text.yview)
        box.pack(expand='yes', fill='x')

    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons
        box = Frame(self)
        w = Button(box, text="确定", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="取消", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        box.pack()

    def ok(self, event=None):

        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        self.cancel()

    def cancel(self, event=None):

        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()



if __name__ == '__main__':
    root = Tk()
    tab=tab(root)
    tab.pack(expand='yes', fill='x')
    root.mainloop()
    pass
