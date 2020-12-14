from tkinter import  *
from tkinter import ttk
import const
import edit_hint

class baseWiget():

    def get(self):
        pass
    def set(self):
        pass
    def hint_message(self):
        return None

    def check2(self,s):
        return ""

    def check(self):
        return self.check2(self.get())

class multiRow(baseWiget):
    def __init__(self,master,rownum,text):
        self.FrameBody=master
        self.row_number=rownum
        self.list=[]
        self.text=text
        self.addline()
        Button(master, text="增加", command=self.addline).grid(row=rownum, column=4, sticky=E, padx=3, pady=3)
        Button(master, text="减少", command=self.deleterow).grid(row=rownum, column=5, sticky=W, padx=3, pady=3)

    def get(self):
        texts=[]
        for i in self.list:
            text=i["entry"].get()
            texts.append(text)
        return texts

    def set(self,data):
        n= len(data)-len(self.list)
        if n>0:
            for i in range(0,n):
                self.addline()
        elif n<0:
            for i in range(0,-n):
                self.deleterow()
        for i in range(len(data)):
            self.list[i]["text"].set(data[i])


    def addline(self):
        master = self.FrameBody
        line={}
        line["lable"]=Label(master, text=self.text)
        line["lable"].grid(row=self.row_number, column=0, sticky=E)
        v = StringVar()
        line["text"]=v
        line["entry"] = Entry(master, width=28,textvariable=v)
        line["entry"].grid(row=self.row_number, column=1, columnspan=3, padx=const.padx, pady=const.pady, sticky=W)
        line["entry"].bind("<Button-3>", lambda x: rightKey(x, line["entry"]))  # 绑定右键鼠标事件
        hintmsg=self.hint_message()
        if hintmsg!=None:
            edit_hint.ToolTip(line["entry"], msg=hintmsg, msgFunc=None, follow=True, delay=0)
        self.list.append(line)
        self.row_number = self.row_number + 1

    def deleterow(self):
        if len(self.list)>1:
            line=self.list.pop()
            line["lable"].destroy()
            line["entry"].destroy()
            self.row_number = self.row_number - 1

class label(baseWiget):
    def __init__(self,master,label_text,rowNum,clomNum):
        entry = Entry(master, width=8)
        entry.grid(row=rowNum, column=clomNum + 1, padx=const.padx, pady=const.pady, sticky=W)
        self.init(entry, master, label_text, rowNum, clomNum)

    def init(self,entry,master,label_text,rowNum,clomNum):
        Label(master, text=label_text).grid(row=rowNum, column=clomNum, sticky=E)
        v=StringVar()
        entry.config(textvariable=v)
        self.entry=v
        entry.bind("<Button-3>", lambda x: rightKey(x, entry))  # 绑定右键鼠标事件
        hintmsg=self.hint_message()
        if hintmsg!=None:
            edit_hint.ToolTip(entry, msg=hintmsg, msgFunc=None, follow=True, delay=0)

    def get(self):
        return self.entry.get()
    def set(self,data):
        self.entry.set(data)

class longlabel(label):
    def __init__(self, master, label_text, rowNum, clomNum):
        entry = Entry(master, width=38)
        entry.grid(row=rowNum, column=1, columnspan=5, padx=const.padx, pady=const.pady, sticky=W)
        self.init(entry, master, label_text, rowNum, clomNum)

class date(label):
    def __init__(self, master, label_text, rowNum, clomNum):
        entry = Entry(master, width=18)
        entry.grid(row=rowNum, column=1, columnspan=2, padx=const.padx, pady=const.pady, sticky=W)
        self.init(entry, master, label_text, rowNum, clomNum)

    def checkDate(self):#检测日期格式是否正确
        date=self.get()
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

class option(baseWiget):
    def __init__(self, master, label_text, rowNum, clomNum,values):
        Label(master, text=label_text).grid(row=rowNum, column=clomNum, sticky=E)
        chosenString = StringVar()
        cobobox = ttk.Combobox(master, width=5, textvariable=chosenString, state="readonly")
        hintmsg = self.hint_message()
        if hintmsg != None:
            edit_hint.ToolTip(cobobox, msg=hintmsg, msgFunc=None, follow=True, delay=0)
        cobobox['values'] = values  # 设置下拉列表的值
        cobobox.grid(column=clomNum + 1, row=rowNum, padx=const.padx, pady=const.pady,
                          sticky=W)  # 设置其在界面中出现的位置  column代表列   row 代表行
        cobobox.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        self.str=chosenString
        self.combox=cobobox


    def get(self):
        return self.str.get()

    def set(self,data):
        combox=self.combox["values"]
        for i in range(0,len(combox)):
            if data==combox[i]:
                self.combox.current(i)
                break



class maintext(baseWiget):
    def __init__(self, parent):
        Label(parent, text="*文件内容:").pack(side='top', anchor='w')
        box=Frame(parent)
        scrollbar = Scrollbar(box)
        scrollbar.pack(side=RIGHT, fill=Y)
        text=Text(box,width=55,height=15,yscrollcommand=scrollbar.set)
        text.pack( expand='yes', fill='x',padx=5,pady=5)
        scrollbar.config(command=text.yview)
        box.pack(expand='yes', fill='x')
        self.text=text
        text.bind("<Button-3>", lambda x: rightKey(x,text))  # 绑定右键鼠标事件
        hintmsg = self.hint_message()
        if hintmsg != None:
            edit_hint.ToolTip(text, msg=hintmsg, msgFunc=None, follow=True, delay=0)

    def get(self):
        return self.text.get('0.0','end')
    def set(self,data):
        self.text.delete('1.0', 'end')
        self.text.insert('1.0',data)
    def check(self):
        if self.get()=="\n":
            return "文件内容不能为空."
        else:
            return ""

menubar=0
def cut(editor, event=None):
    editor.event_generate("<<Cut>>")
def copy(editor, event=None):
    editor.event_generate("<<Copy>>")
def paste(editor, event=None):
    editor.event_generate('<<Paste>>')

def rightKey(event, editor):
    menubar.delete(0,END)
    menubar.add_command(label='剪切',command=lambda:cut(editor))
    menubar.add_command(label='复制',command=lambda:copy(editor))
    menubar.add_command(label='粘贴',command=lambda:paste(editor))
    menubar.post(event.x_root,event.y_root)
