from tkinter import *
from tkinter import ttk

import tab


class Xiaxinwen(tab.tab):
    def body(self, master):
        # 一般用6位3号阿拉伯数字
        fenhao = self.addLabel(master, "份号：", 0,0)

        miji = self.addOption(master, "保密等级：", 1,0, ("无", "绝密","机密","秘密" ))

        self.addLabel(master, "保密期限：", 1,2)

        self.addOption(master, "紧急程度：",3,0, ("无", "特急","加急","特提","平急" ))

        self.addLabel(master,"发文机关代字：",4,0)
        self.addLabel(master,"年份：",4,2)
        self.addLabel(master, "发文号：", 4, 4)
        #
        self.addLabel(master, "发文机关：", 5,0)
        self.row_number=5
        Button(master, text="增加",command=self.addRow(master)).grid(row=5, column=2)



    def addLabel(self, master, label, rowNum,clomNum):
        Label(master, text=label).grid(row=rowNum,column=clomNum,sticky=E)
        entry = Entry(master,width=8)
        entry.grid(row=rowNum, column=clomNum+1,padx=3,pady=3,sticky=W)
        return entry

    def addOption(self, master, label, rowNum, clomNum,values):
        Label(master, text=label).grid(row=rowNum,column=clomNum,sticky=E)
        number = StringVar()
        numberChosen = ttk.Combobox(master, width=6, textvariable=number, state="readonly")
        numberChosen['values'] = values  # 设置下拉列表的值
        numberChosen.grid(column=clomNum+1, row=rowNum,padx=3,pady=3,sticky=W)  # 设置其在界面中出现的位置  column代表列   row 代表行
        numberChosen.current(2)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

    def addRow(self,master):
        self.row_number=self.row_number+1
        self.addLabel(master, "发文机关：", self.row_number, 0)
        pass