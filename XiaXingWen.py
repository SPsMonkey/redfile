from tkinter import *
from tkinter import ttk
import const
import tab
import tkinter.messagebox

class Xiaxinwen(tab.tab):
    def body(self, master):
        xia={}
        # 一般用6位3号阿拉伯数字
        xia["份号"] = self.addLabel(master, "份号：", 0,0)

        xia["保密等级"] = self.addOption(master, "保密等级：", 1,0, ("无", "绝密","机密","秘密" ))

        xia["保密期限"]=self.addLabel(master, "保密期限：", 1,2)

        xia["紧急程度"]=self.addOption(master, "紧急程度：",3,0, ("无", "特急","加急","特提","平急" ))

        xia["发文机关代字"]=self.addLabel(master,"*发文机关代字：",4,0)
        xia["年份"]=self.addLabel(master,"*年份：",4,2)
        xia["发文号"]=self.addLabel(master, "*发文号：", 4, 4)
        #
        xia["发文机关"]=tab.multiRow(master,5)
        xia["标题"]=self.addLongLabel(master,"*标题：",50,0)
        xia["成文日期"]=self.addDate(master, "*成文日期：",51,0)
        xia["抄送机关"] = self.addLongLabel(master, "抄送机关：", 52, 0)
        xia["印发机关"] = self.addLongLabel(master, "*印发机关：", 53, 0)
        xia["印发日期"] = self.addDate(master, "*印发日期：", 54, 0)
        self.allWigets=xia

    def getData(self):
        xia=self.allWigets
        data={}
        data["份号"]=xia["份号"].get()
        data["保密等级"] = xia["保密等级"].get()
        data["保密期限"] = xia["保密期限"].get()
        data["紧急程度"] = xia["紧急程度"].get()

        data["发文机关代字"] = xia["发文机关代字"].get()
        data["年份"] = xia["年份"].get()
        data["发文号"] = xia["发文号"].get()

        data["发文机关"] = xia["发文机关"].get()

        data["标题"] = xia["标题"].get()

        data["成文日期"] = xia["成文日期"].get()
        data["抄送机关"] = xia["抄送机关"].get()
        data["印发机关"] = xia["印发机关"].get()
        data["印发日期"] = xia["印发日期"].get()

        data["文件内容"]=xia["文件内容"].get('0.0','end')
        return data

    def check(self,data):
        error=""
        if not data["份号"].isdigit():
            error=error+"份号必须是数字。\n"

        if data["发文机关代字"]=="":
            error = error + "发文机关代字 不能为空。\n"

        if data["年份"]=="":
            error = error + "年份 不能为空。\n"
        else:
            if (not data["年份"].isdigit())or len(data["年份"])!=4 :
                error = error + "请输入正确的年份。\n"

        if data["发文号"]=="":
            error = error + "发文号 不能为空。\n"
        else:
            if not data["发文号"].isdigit():
                error = error + "请输入正确的发文号。\n"

        if data["发文机关"][0]=="":
            error = error + "发文机关 不能为空。\n"

        if data["标题"]=="":
            error = error + "标题 不能为空。\n"

        if data["成文日期"]=="":
            error = error + "成文日期 不能为空。\n"
        else:
            if not self.checkDate(data["成文日期"]):
                error = error + "请输入正确格式的成文日期。\n"

        if data["印发机关"]=="":
            error = error + "印发机关 不能为空。\n"

        if data["印发日期"]=="":
            error = error + "印发日期 不能为空。\n"
        else:
            if not self.checkDate(data["印发日期"]):
                error = error + "请输入正确格式的印发日期。\n"

        if data["文件内容"]=="\n":
            error = error + "文件内容 不能为空。\n"
        return error






    def apply(self):
        data=self.getData()
        print(data)
        result=self.check(data)
        if result !="":
            tkinter.messagebox.showerror('错误', result)
        else:
            pass



