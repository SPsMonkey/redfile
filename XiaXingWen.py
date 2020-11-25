from tkinter import *
from tkinter import ttk
import const
from tab import *
import tkinter.messagebox


class Xiaxinwen(tab):
    def body(self, master):
        xia=self.allWigets
        # 一般用6位3号阿拉伯数字
        xia["份号"] = fen_hao(master,0,0)

        xia["保密等级"] = bao_mi_deng_ji(master,1,0)

        xia["保密期限"]=bao_mi_qi_xian(master,1,2)

        xia["紧急程度"]=jin_ji_cheng_du(master, 3,0)

        xia["发文机关代字"]=ji_guan_dai_zi(master,4,0)
        xia["年份"]=nian_fen(master,4,2)
        xia["发文号"]=fa_wen_hao(master,4, 4)
        #
        xia["发文机关"]=multiRow(master,5)
        xia["标题"]=biao_ti(master,50,0)
        xia["成文日期"]=cheng_wen_ri_qi(master, 51,0)
        xia["抄送机关"] = chao_song(master, 52, 0)
        xia["印发机关"] = yin_fa(master,53, 0)
        xia["印发日期"] = yin_fa_ri_qi(master, 54, 0)


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



