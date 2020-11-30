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
class fa_wen_ji_guan(multiRow):
    def __init__(self,master,rownum):
        multiRow.__init__(self,master,rownum,"发文机关：")

    def check(self):
        if self.get()[0]=="":
            return  "发文机关不能为空。"
        else:
            return ""

class ji_guan_dai_zi(label):
    def __init__(self, master, rowNum, clomNum):
        label.__init__(self, master, "发文机关代字：", rowNum, clomNum)
    def check(self):
        if self.get()=="":
            return "发文机关代字不能为空。"
        else:
            return ""

class nian_fen(label):
    def __init__(self, master, rowNum, clomNum):
        label.__init__(self, master, "年份：", rowNum, clomNum)
    def check(self):
        s=self.get()
        if s == "":
            return "年份不能为空。"
        elif (not s.isdigit()) or (len(s)!=4):
            return "年份必须为4位阿拉伯数字。"
        else:
            return ""

class fa_wen_hao(label):
    def __init__(self, master, rowNum, clomNum):
        label.__init__(self, master, "发文号：", rowNum, clomNum)
    def check(self):
        s = self.get()
        if s == "":
            return "发文号不能为空。"
        elif not s.isdigit():
            return "发文号必须为阿拉伯数字。"
        else:
            return ""

class biao_ti(longlabel):
    def __init__(self, master, rowNum, clomNum):
        longlabel.__init__(self, master, "标题：", rowNum, clomNum)
    def check(self):
        s = self.get()
        if s == "":
            return "标题不能为空。"
        else:
            return ""

class cheng_wen_ri_qi(date):
    def __init__(self, master, rowNum, clomNum):
        date.__init__(self, master, "成文日期：", rowNum, clomNum)
    def check(self):
        s = self.get()
        if s == "":
            return "成文日期不能为空。"
        elif not self.checkDate():
            return "请输入正确格式的成文日期"
        else:
            return ""

class fu_jian(multiRow):
    def __init__(self,master,rownum):
        multiRow.__init__(self,master,rownum,"附件：")

    def check(self):
        return ""


class yin_fa_ri_qi(date):
    def __init__(self, master, rowNum, clomNum):
        date.__init__(self, master, "印发日期：", rowNum, clomNum)
    def check(self):
        s=self.get()
        if s != "":
            if not self.checkDate():
                return "请输入正确格式的成文日期"
        else:
            return ""

class chao_song(longlabel):
    def __init__(self, master, rowNum, clomNum):
        longlabel.__init__(self, master, "抄送机关：", rowNum, clomNum)
    def check(self):
        return ""

class yin_fa(longlabel):
    def __init__(self, master, rowNum, clomNum):
        longlabel.__init__(self, master, "印发机关：", rowNum, clomNum)
    def check(self):
        return ""



class tab(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        body = Frame(self)
        self.allWigets={}
        self.FrameBody=body
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        show_hide = Button(self, text="显示其他选项", command=lambda: self.show_other(), default=ACTIVE)
        show_hide.pack(padx=5, pady=5,anchor='e')
        self.hide_button=show_hide

        other_body=Frame(self)
        self.other_body=other_body
        self.other(other_body)
        self.is_hide=True

        self.main_text_body=Frame(self)
        self.allWigets["文件内容"] =maintext(self.main_text_body)
        self.main_text_body.pack()

    def body(self, master):

        pass

    def other(self,master):
        pass

    def apply(self):
        pass # override

    def show_other(self):
        if self.is_hide==True:
            self.main_text_body.forget()
            self.other_body.pack()
            self.main_text_body.pack()
            self.hide_button["text"]="隐藏其他选项"
            self.is_hide=False
        else:
            self.other_body.forget()
            self.hide_button["text"] = "显示其他选项"
            self.is_hide=True

    def hide_other(self):
        pass




if __name__ == '__main__':
    root = Tk()
    tab=tab(root)
    tab.pack(expand='yes', fill='x')
    print (tab.checkDate("2020年6月32日"))
    root.mainloop()
    pass
