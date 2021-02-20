from .tab import *
import tkinter.messagebox
from ..wincom import genredfile

class XinHan(tab):
    def body(self, master):
        xia=self.allWigets

        xia["发文机关"]=fa_wen_ji_guan(master,0)
        xia["标题"]=biao_ti(master,5,0)
        xia["成文日期"]=cheng_wen_ri_qi(master,6,0)


    def other(self,master):
        xia = self.allWigets
        xia["是否使用红头纸"]=is_red_paper(master,0,0)
        xia["调整参数"]=tiao_zhen_can_shu(master,0,2)
        xia["份号"] = fen_hao(master, 1, 0)
        xia["保密等级"] = bao_mi_deng_ji(master, 2, 0)
        xia["保密期限"] = bao_mi_qi_xian(master, 2, 2)
        xia["紧急程度"] = jin_ji_cheng_du(master, 1, 2)
        # 一般用6位3号阿拉伯数字
        xia["发文机关代字"]=ji_guan_dai_zi(master,3,0)
        xia["年份"]=nian_fen(master,3,2)
        xia["发文号"]=fa_wen_hao(master,3, 4)

        xia["抄送机关"] = chao_song(master, 4, 0)




    def check(self,data):
        error=""
        xia = self.allWigets
        for key in xia:
            e=xia[key].check()
            if e!="":
                error=error+e+"\n"
        return error


    def apply(self):
        data=self.getData()
        print(data)
        result=self.check(data)
        if result !="":
            tkinter.messagebox.showerror('错误', result)
        else:
            genredfile.gendown(data)
