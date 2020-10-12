from tkinter import *
from tkinter import ttk
import const
import tab


class Xiaxinwen(tab.tab):
    def body(self, master):
        xia={}
        # 一般用6位3号阿拉伯数字
        xia["份号"] = self.addLabel(master, "份号：", 0,0)

        xia["保密等级"] = self.addOption(master, "保密等级：", 1,0, ("无", "绝密","机密","秘密" ))

        xia["保密期限"]=self.addLabel(master, "保密期限：", 1,2)

        xia["紧急程度"]=self.addOption(master, "紧急程度：",3,0, ("无", "特急","加急","特提","平急" ))

        xia["发文机关代字"]=self.addLabel(master,"发文机关代字：",4,0)
        xia["年份"]=self.addLabel(master,"年份：",4,2)
        xia["发文号"]=self.addLabel(master, "发文号：", 4, 4)
        #
        xia["发文机关"]=[]
        self.row_number=4
        self.addRow()
        Button(master, text="增加",command=self.addRow).grid(row=5, column=4,sticky=E,padx=3,pady=3)
        Button(master,text="减少",command=self.deleterow).grid(row=5,column=5,sticky=W,padx=3,pady=3)


    def addLabel(self, master, label, rowNum,clomNum):
        Label(master, text=label).grid(row=rowNum,column=clomNum,sticky=E)
        entry = Entry(master,width=8)
        entry.grid(row=rowNum, column=clomNum+1,padx=const.padx,pady=const.pady,sticky=W)
        return entry

    def addOption(self, master, label, rowNum, clomNum,values):
        Label(master, text=label).grid(row=rowNum,column=clomNum,sticky=E)
        number = StringVar()
        numberChosen = ttk.Combobox(master, width=5, textvariable=number, state="readonly")
        numberChosen['values'] = values  # 设置下拉列表的值
        numberChosen.grid(column=clomNum+1, row=rowNum,padx=const.padx,pady=const.pady,sticky=W)  # 设置其在界面中出现的位置  column代表列   row 代表行
        numberChosen.current(2)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

    def addRow(self):
        master=self.FrameBody
        self.row_number=self.row_number+1
        Label(master, text="发文机关：").grid(row=self.row_number, column=0, sticky=E)
        entry = Entry(master, width=28)
        entry.grid(row=self.row_number, column=1,columnspan=3, padx=const.padx, pady=const.pady, sticky=W)
        pass

    def deleterow(self):
        pass