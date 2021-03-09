from win32com.client import Dispatch

data = {"份号": "234567", "保密等级": "紧急", "保密期限": "2年", "紧急程度": "特急",
        "发文机关": ["湖南省娄底市怀农业农村局", "县扶贫开发办", "县劳动与保障局"],
        "是否使用红头纸": "","高度调整":"2",
        "发文机关代字": "泸农发", "年份": "2019", "发文号": "6",
        "签发人":"李桂香 王大妈 张三 李四","签发人调整":"0",
        "标题": "XX县农业农村局关于什么",
        "文件内容": "局属各单位：\n根据。。。。。。。。。。\n\n\n\n\n\n\n\n\n\n\n\n结束",
        "成文日期": "2020年6月12日",
        "附件": ["湖北省武汉市事发地点发送到发送到杀对方水电费第三方第三方第三方士大夫地方", "湖北省武汉市事发地点发送到发送到杀对方水电费第三方第三方第三方士大夫地方"],
        "主送机关": "县畜牧局、中华人民共和国内蒙古、中国甘肃省那然色布斯台音布拉格农业综合执法局、中国甘肃省那然色布斯台音布拉格农业综合执法局",
        "抄送机关": "县畜牧局、中华人民共和国内蒙古、中国甘肃省那然色布斯台音布拉格农业综合执法局、中国甘肃省那然色布斯台音布拉格农业综合执法局",
        "印发机关": "县农业农村局",
        "印发日期": "2020年3月21日"}
from .  downfile  import *
from .  upfile import *
from .  xinhan import *
def gendown(data):
    rf=downfile(data)
    rf.addFileNum()
    rf.add_SecurityLevel_Time()
    rf.add_emergency_level()
    rf.add_red_title()
    rf.inser_empty_row(1)
    rf.add_redfile_num()
    rf.inser_empty_row(2)
    rf.add_title()
    rf.inser_empty_row(1)
    rf.add_content()
    rf.add_fujian_shuo_min()
    rf.add_name_date()
    rf.add_fujian()
    rf.add_end()

    #156/442.5 纸张mm数比线条单位比值  33+10.5x换算成
    #new_document.SaveAs("G:/python/win32com/3.docx")
    #new_document.Close()
    #app.Quit()
def genup(data):
    rf=upfile(data)
    rf.addFileNum()
    rf.add_SecurityLevel_Time()
    rf.add_emergency_level()
    rf.add_red_title()
    rf.inser_empty_row(1)
    rf.add_red_num_and_qian_fa_ren()
    rf.inser_empty_row(2)
    rf.add_title()
    rf.inser_empty_row(1)
    rf.add_content()
    rf.add_fujian_shuo_min()
    rf.add_name_date()
    rf.add_fujian()
    rf.add_end()

def genxinhan(data):
    rf=xinhan(data)
    rf.add_xin_han_title()


if __name__ == '__main__':


    genxinhan(data)