from tkinter import  *
from tkinter import ttk
import const

class multiRow():
    def __init__(self,master,rownum):
        self.FrameBody=master
        self.row_number=rownum
        self.list=[]
        self.addline()
        Button(master, text="增加", command=self.addline).grid(row=rownum, column=4, sticky=E, padx=3, pady=3)
        Button(master, text="减少", command=self.deleterow).grid(row=rownum, column=5, sticky=W, padx=3, pady=3)

    def get(self):
        texts=[]
        for i in self.list:
            text=i["entry"].get()
            texts.append(text)
        return texts


    def addline(self):
        master = self.FrameBody
        line={}
        line["lable"]=Label(master, text="*发文机关：")
        line["lable"].grid(row=self.row_number, column=0, sticky=E)
        line["entry"] = Entry(master, width=28)
        line["entry"].grid(row=self.row_number, column=1, columnspan=3, padx=const.padx, pady=const.pady, sticky=W)
        self.list.append(line)
        self.row_number = self.row_number + 1

    def deleterow(self):
        if len(self.list)>1:
            line=self.list.pop()
            line["lable"].destroy()
            line["entry"].destroy()
            self.row_number = self.row_number - 1
        pass


class tab(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        body = Frame(self)
        self.FrameBody=body
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)
        self.maintext()
        self.buttonbox()


    def body(self, master):

        pass

    def maintext(self):
        Label(self, text="*文件内容:").pack(side='top', anchor='sw')
        box=Frame(self)
        scrollbar = Scrollbar(box)
        scrollbar.pack(side=RIGHT, fill=Y)
        text=Text(box,width=30,height=10,yscrollcommand=scrollbar.set)
        text.pack( expand='yes', fill='x',padx=5,pady=5)
        self.allWigets["文件内容"]=text
        scrollbar.config(command=text.yview)
        box.pack(expand='yes', fill='x')

    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons
        box = Frame(self)
        w = Button(box, text="点击生成", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=RIGHT, padx=5, pady=5)


        self.bind("<Return>", self.ok)

        box.pack()

    def ok(self, event=None):

        self.apply()

    def apply(self):
        pass # override



    def addLabel(self, master, label, rowNum,clomNum):
        Label(master, text=label).grid(row=rowNum,column=clomNum,sticky=E)
        entry = Entry(master,width=8)
        entry.grid(row=rowNum, column=clomNum+1,padx=const.padx,pady=const.pady,sticky=W)
        return entry

    def addLongLabel(self,master, label, rowNum,clomNum):
        Label(master, text=label).grid(row=rowNum, column=clomNum, sticky=E)
        entry = Entry(master, width=38)
        entry.grid(row=rowNum, column=1, columnspan=5, padx=const.padx, pady=const.pady, sticky=W)
        return entry

    def addDate(self,master, label, rowNum,clomNum):
        Label(master, text=label).grid(row=rowNum, column=clomNum, sticky=E)
        entry = Entry(master, width=18)
        entry.grid(row=rowNum, column=clomNum + 1, columnspan=3,padx=const.padx, pady=const.pady, sticky=W)
        return entry

    def addOption(self, master, label, rowNum, clomNum,values):
        Label(master, text=label).grid(row=rowNum,column=clomNum,sticky=E)
        number = StringVar()
        numberChosen = ttk.Combobox(master, width=5, textvariable=number, state="readonly")
        numberChosen['values'] = values  # 设置下拉列表的值
        numberChosen.grid(column=clomNum+1, row=rowNum,padx=const.padx,pady=const.pady,sticky=W)  # 设置其在界面中出现的位置  column代表列   row 代表行
        numberChosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        return number

    def checkDate(self,date):#检测日期格式是否正确
        y=date.split("年",1)
        if len(y[0])!=4:
            return False
        if not y[0].isdigit():
            return False

        m=y[1].split("月",1)
        if len(m[0])>2 or len(m[0])<1:
            return False
        if not m[0].isdigit():
            return False
        M=int(m[0])
        if M>12 or M<1:
            return False

        d=m[1].split("日",1)
        if len(d[0]) > 2 or len(d[0]) < 1:
            return False
        if not d[0].isdigit():
            return False
        M = int(d[0])
        if M > 31 or M < 1:
            return False

        if d[1]!="":
            return False
        return True



if __name__ == '__main__':


    root = Tk()
    tab=tab(root)
    tab.pack(expand='yes', fill='x')
    print (tab.checkDate("2020年6月32日"))
    root.mainloop()
    pass
