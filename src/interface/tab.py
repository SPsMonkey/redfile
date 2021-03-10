from tkinter import  *
from .redfileWigets import *
from .edit_hint import hintmsg,itemname
from tkinter import ttk

class fen_hao(label): #份号
    def __init__(self,master,rowNum,clomNum):
        self.name = itemname["份号"]
        label.__init__(self,master,self.name+"：",rowNum,clomNum)
    def check2(self,s):
        if not s.isdigit():
            return "份号必须是数字。"
        else:
            return ""

class bao_mi_deng_ji(option):
    def __init__(self, master, rowNum, clomNum):
        self.name = itemname["保密等级"]
        option.__init__(self, master, self.name+"：", rowNum, clomNum,("无", "绝密","机密","秘密" ))

class bao_mi_qi_xian(label):
    def __init__(self, master, rowNum, clomNum):
        self.name=itemname["保密期限"]
        label.__init__(self, master, self.name+"：", rowNum, clomNum)

class jin_ji_cheng_du(option):
    def __init__(self, master, rowNum, clomNum):
        self.name=itemname["紧急程度"]
        option.__init__(self, master,self.name+"：", rowNum, clomNum,("无", "特急","加急","特提","平急" ))

class fa_wen_ji_guan(multiRow):
    def __init__(self,master,rownum):
        self.name=itemname["发文机关"]
        multiRow.__init__(self,master,rownum,self.name+"：")

    def check2(self,s):
        return ""

class ji_guan_dai_zi(label):
    def __init__(self, master, rowNum, clomNum):
        self.name = itemname["机关代字"]
        label.__init__(self, master, self.name+"：", rowNum, clomNum)

    def check2(self,s):
        return ""

class nian_fen(label):
    def __init__(self, master, rowNum, clomNum):
        self.name = itemname["年份"]
        label.__init__(self, master, self.name+"：", rowNum, clomNum)
    def check2(self,s):
        if (not s.isdigit()) or (len(s)!=4):
            return "年份必须为4位阿拉伯数字。"
        else:
            return ""

class fa_wen_hao(label):
    def __init__(self, master, rowNum, clomNum):
        self.name = itemname["发文号"]
        label.__init__(self, master, self.name+"：", rowNum, clomNum)
    def check2(self,s):
        if not s.isdigit():
            return "发文号必须为阿拉伯数字。"
        else:
            return ""

class qian_fa_ren(label):
    def __init__(self, master, rowNum, clomNum):
        self.name = itemname["签发人"]
        label.__init__(self, master,self.name+ "：", rowNum, clomNum)
    def check2(self,s):
        return ""

class biao_ti(longlabel):
    def __init__(self, master, rowNum, clomNum):
        self.name = itemname["标题"]
        longlabel.__init__(self, master, self.name+"：", rowNum, clomNum)
    def check2(self,s):
        return ""

class cheng_wen_ri_qi(date):
    def __init__(self, master, rowNum, clomNum):
        self.name = itemname["成文日期"]
        date.__init__(self, master, self.name+"：", rowNum, clomNum)
    def check2(self,s):
        if not self.checkDate():
            return "请输入正确格式的成文日期"
        else:
            return ""

class fu_jian(multiRow):
    def __init__(self,master,rownum):
        self.name = itemname["附件"]
        multiRow.__init__(self,master,rownum,self.name+"：")

class yin_fa_ri_qi(date):
    def __init__(self, master, rowNum, clomNum):
        self.name = itemname["印发日期"]
        date.__init__(self, master, self.name+"：", rowNum, clomNum)
    def check2(self,s):
        if not self.checkDate():
            return "请输入正确格式的成文日期"
        else:
            return ""

class chao_song(longlabel):
    def __init__(self, master, rowNum, clomNum):
        self.name = itemname["抄送机关"]
        longlabel.__init__(self, master,self.name+ "：", rowNum, clomNum)

class yin_fa(longlabel):
    def __init__(self, master, rowNum, clomNum):
        self.name = itemname["印发机关"]
        longlabel.__init__(self, master, self.name+"：", rowNum, clomNum)

class is_red_paper(baseWiget):
    def __init__(self,master,rownum,columnnum):
        baseWiget.__init__(self)
        checkvar=IntVar()
        self.name = itemname["红头纸"]
        check = Checkbutton(master, text=self.name,variable = checkvar, \
                 onvalue = 1, offvalue = 0)
        check.grid(row=rownum, column=columnnum,columnspan=2, padx=5, pady=5, sticky=W)
        self.isCheck=checkvar
    def get(self):
        return self.isCheck.get()
    def isempty(self):
        return False
    def set(self,data):
        self.isCheck.set(data)
class tiao_zhen_can_shu(label): #份号
    def __init__(self,master,rowNum,clomNum):
        self.name = itemname["高度调整"]
        label.__init__(self,master,self.name+"：",rowNum,clomNum)

    def check2(self,s):
        return ""
    def get(self):
        num=label.get(self)
        if isFloat(num)==False:
            num=0
        fnum=float(num)
        if fnum<0:
            fnum=0.0
        return fnum
class tiao_zhen_can_shu2(label): #份号
    def __init__(self,master,rowNum,clomNum):
        self.name = itemname["签发人调整"]
        label.__init__(self,master,self.name+"：",rowNum,clomNum)

    def check2(self,s):
        return ""

    def get(self):
        num = label.get(self)
        if num=="":
            return 0
        fnum = int(num)
        return fnum

class tab(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        body = Frame(self)
        self.allWigets={}
        self.FrameBody=body
        wegets={}
        self.body(body,wegets)
        for w in wegets:
            wegets[w].required=True
            self.allWigets[w]=wegets[w]
        body.pack(padx=5, pady=5)

        show_hide = Button(body, text="显示其他选项", command=lambda: self.show_other(), default=ACTIVE)
        show_hide.grid(row=100, column=4,columnspan=2,padx=5, pady=5,sticky=E)

        self.hide_button=show_hide


        other_body=Frame(self)
        self.other_body=other_body
        self.other(other_body,self.allWigets)
        self.is_hide=True

        self.main_text_body=Frame(self)
        self.allWigets["文件内容"] =maintext(self.main_text_body)
        self.main_text_body.pack()

    def body(self, master,wegets):

        pass

    def other(self,master,wegets):
        pass

    def apply(self):
        pass # override

    def getData(self):
        xia=self.allWigets
        data={}
        for key in xia:
            data[key]=xia[key].get()
        return data

    def setData(self,data):
        xia=self.allWigets
        for key in data:
            xia[key].set(data[key])

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


