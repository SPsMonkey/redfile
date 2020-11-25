from tkinter import  *
from redfileWigets import *
from tkinter import ttk
import const
class fen_hao(label): #份号
    def __init__(self,master,rowNum,clomNum):
        label.__init__(self,master,"份号：",rowNum,clomNum)

    def check(self):
        s=self.get()
        if not s.isdigit():
            return "份号必须是数字。"
        else:
            return ""

class bao_mi_deng_ji(option):
    def __init__(self, master, rowNum, clomNum):
        option.__init__(self, master, "保密等级：", rowNum, clomNum,("无", "绝密","机密","秘密" ))
    def check(self):
        return ""

class bao_mi_qi_xian(label):
    def __init__(self, master, rowNum, clomNum):
        label.__init__(self, master, "保密期限：", rowNum, clomNum)
    def check(self):
        return ""
class jin_ji_cheng_du(option):
    def __init__(self, master, rowNum, clomNum):
        option.__init__(self, master, "紧急程度：", rowNum, clomNum,("无", "特急","加急","特提","平急" ))
    def check(self):
        return ""

class ji_guan_dai_zi(label):
    def __init__(self, master, rowNum, clomNum):
        label.__init__(self, master, "发文机关代字：", rowNum, clomNum)
    def check(self):
        if self.get()=="":
            return "发文机关代字不能为空。"

class nian_fen(label):
    def __init__(self, master, rowNum, clomNum):
        label.__init__(self, master, "年份：", rowNum, clomNum)
    def check(self):
        pass
class fa_wen_hao(label):
    def __init__(self, master, rowNum, clomNum):
        label.__init__(self, master, "发文号：", rowNum, clomNum)
    def check(self):
        pass

class biao_ti(longlabel):
    def __init__(self, master, rowNum, clomNum):
        longlabel.__init__(self, master, "标题：", rowNum, clomNum)
    def check(self):
        pass

class cheng_wen_ri_qi(date):
    def __init__(self, master, rowNum, clomNum):
        date.__init__(self, master, "成文日期：", rowNum, clomNum)
    def check(self):
        pass
class yin_fa_ri_qi(date):
    def __init__(self, master, rowNum, clomNum):
        date.__init__(self, master, "印发日期：", rowNum, clomNum)
    def check(self):
        pass

class chao_song(longlabel):
    def __init__(self, master, rowNum, clomNum):
        longlabel.__init__(self, master, "抄送机关：", rowNum, clomNum)
    def check(self):
        pass

class yin_fa(longlabel):
    def __init__(self, master, rowNum, clomNum):
        longlabel.__init__(self, master, "印发机关：", rowNum, clomNum)
    def check(self):
        pass

class tab(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        body = Frame(self)
        self.allWigets={}
        self.FrameBody=body
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)
        self.allWigets["文件内容"] =maintext(self)



    def body(self, master):

        pass



    def apply(self):
        pass # override




if __name__ == '__main__':
    root = Tk()
    tab=tab(root)
    tab.pack(expand='yes', fill='x')
    print (tab.checkDate("2020年6月32日"))
    root.mainloop()
    pass
