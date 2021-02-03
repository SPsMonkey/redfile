from tkinter import  *
from .redfileWigets import *
from tkinter import ttk

class fen_hao(label): #份号
    def __init__(self,master,rowNum,clomNum):
        label.__init__(self,master,"份号：",rowNum,clomNum)

    def check2(self,s):
        if s=="":
            return ""
        else:
            if not s.isdigit():
                return "份号必须是数字。"
            else:
                return ""
    def hint_message(self):
        return "公文印制份数的顺序号，涉密公文应当标注份号，一般为6位阿拉伯数字。\n例如：123456"

class bao_mi_deng_ji(option):
    def __init__(self, master, rowNum, clomNum):
        option.__init__(self, master, "保密等级：", rowNum, clomNum,("无", "绝密","机密","秘密" ))
    def hint_message(self):
        return "涉密公文应当根据涉密程度分别标注“绝密”“机密”“秘密”。"

class bao_mi_qi_xian(label):
    def __init__(self, master, rowNum, clomNum):
        label.__init__(self, master, "保密期限：", rowNum, clomNum)
    def hint_message(self):
        return "涉密公文应当根据情况标注保密期限。例如：1年"

class jin_ji_cheng_du(option):
    def __init__(self, master, rowNum, clomNum):
        option.__init__(self, master, "紧急程度：", rowNum, clomNum,("无", "特急","加急","特提","平急" ))
    def hint_message(self):
        return "公文送达和办理的时限要求。根据紧急程度，紧急公文应当分别标注“特急”“加急”，电报应当分别标注“特提”“特急”“加急”“平急”。"

class fa_wen_ji_guan(multiRow):
    def __init__(self,master,rownum):
        multiRow.__init__(self,master,rownum,"发文机关：")

    def check2(self,s):
        if s[0]=="":
            return  "发文机关不能为空。"
        else:
            return ""
    def hint_message(self):
        return "发文机关全称"

class ji_guan_dai_zi(label):
    def __init__(self, master, rowNum, clomNum):
        label.__init__(self, master, "发文机关代字：", rowNum, clomNum)
    def check2(self,s):
        if s=="":
            return "发文机关代字不能为空。"
        else:
            return ""
    def hint_message(self):
        return "填写发文机关代字"

class nian_fen(label):
    def __init__(self, master, rowNum, clomNum):
        label.__init__(self, master, "年份：", rowNum, clomNum)
    def check2(self,s):
        if s == "":
            return "年份不能为空。"
        elif (not s.isdigit()) or (len(s)!=4):
            return "年份必须为4位阿拉伯数字。"
        else:
            return ""
    def hint_message(self):
        return "填写发文年份。例如：2020"

class fa_wen_hao(label):
    def __init__(self, master, rowNum, clomNum):
        label.__init__(self, master, "发文号：", rowNum, clomNum)
    def check2(self,s):
        if s == "":
            return "发文号不能为空。"
        elif not s.isdigit():
            return "发文号必须为阿拉伯数字。"
        else:
            return ""
    def hint_message(self):
        return "填写发文顺序号。例如：20"
class qian_fa_ren(label):
    def __init__(self, master, rowNum, clomNum):
        label.__init__(self, master, "签发人：", rowNum, clomNum)
    def check2(self,s):
        if s == "":
            return "签发人不能为空。"
        else:
            return ""
    def hint_message(self):
        return "填写签发人姓名，多个人请用空格隔开。例如：李某某 张某某"

class biao_ti(longlabel):
    def __init__(self, master, rowNum, clomNum):
        longlabel.__init__(self, master, "标题：", rowNum, clomNum)
    def check2(self,s):
        if s == "":
            return "标题不能为空。"
        else:
            return ""
    def hint_message(self):
        return "填写文件标题，由发文机关名称、事由和文种组成。"

class cheng_wen_ri_qi(date):
    def __init__(self, master, rowNum, clomNum):
        date.__init__(self, master, "成文日期：", rowNum, clomNum)
    def check2(self,s):
        if s == "":
            return "成文日期不能为空。"
        elif not self.checkDate():
            return "请输入正确格式的成文日期"
        else:
            return ""
    def hint_message(self):
        return "署会议通过或者发文机关负责人签发的日期。联合行文时，署最后签发机关负责人签发的日期。例如：2020年1月1日"

class fu_jian(multiRow):
    def __init__(self,master,rownum):
        multiRow.__init__(self,master,rownum,"附件：")

    def hint_message(self):
        return "依次公文附件名称"

class yin_fa_ri_qi(date):
    def __init__(self, master, rowNum, clomNum):
        date.__init__(self, master, "印发日期：", rowNum, clomNum)
    def check2(self,s):
        if s != "":
            if not self.checkDate():
                return "请输入正确格式的成文日期"
        else:
            return ""
    def hint_message(self):
        return "公文的送印日期。例如：2020年1月1日。如不填写则默认与成文日期一致。"

class chao_song(longlabel):
    def __init__(self, master, rowNum, clomNum):
        longlabel.__init__(self, master, "抄送机关：", rowNum, clomNum)
    def hint_message(self):
        return "除主送机关外需要执行或者知晓公文内容的其他机关，应当使用机关全称、规范化简称或者同类型机关统称。名称之间用顿号隔开。"


class yin_fa(longlabel):
    def __init__(self, master, rowNum, clomNum):
        longlabel.__init__(self, master, "印发机关：", rowNum, clomNum)
    def hint_message(self):
        return "公文的送印机关名称。如不填写则默认与发文机关一致"

class is_red_paper(baseWiget):
    def __init__(self,master):
        checkvar=IntVar()
        check = Checkbutton(master, text="是否使用红头纸打印",variable = checkvar, \
                 onvalue = 1, offvalue = 0)
        check.pack(padx=5, pady=5, side="left", anchor='w')
        self.isCheck=checkvar
    def get(self):
        return self.isCheck.get()
    def set(self,data):
        self.isCheck.set(data)

class tab(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        body = Frame(self)
        self.allWigets={}
        self.FrameBody=body
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        middle_body=Frame(self)
        self.allWigets["是否使用红头纸"]=is_red_paper(middle_body)

        show_hide = Button(middle_body, text="显示其他选项", command=lambda: self.show_other(), default=ACTIVE)
        show_hide.pack(padx=5, pady=5,side="right",anchor='e')

        self.hide_button=show_hide
        middle_body.pack(expand='yes', fill='x')

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




if __name__ == '__main__':
    root = Tk()
    tab=tab(root)
    tab.pack(expand='yes', fill='x')
    print (tab.checkDate("2020年6月32日"))
    root.mainloop()
    pass
