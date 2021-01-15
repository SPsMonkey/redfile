from win32com.client import Dispatch
import  math
import RedFunc as rf
def start():
    app = Dispatch('word.Application')
    # 新建word文档
    app.Visible = True
    rf.doc = app.Documents.Add()
    rf.s= rf.doc.Application.Selection
    rf.setPage()

def gendown(data):
    start()
    rf.addFileNum(data["份号"])
    rf.add_SecurityLevel_Time(data["保密等级"],data["保密期限"])
    rf.add_emergency_level(data["紧急程度"])
    rf.add_red_title(data["发文机关"])
    rf.add_redfile_num(data["发文机关代字"],data["年份"],data["发文号"])
    row_current = rf.s.Information(10)  # 获取输入点所在的行数
    rf.add_line( rf.doc.Range(0,1), row_current, 3, 255)
    rf.add_title(data["标题"])
    rf.add_content(data["文件内容"])
    rf.add_fujian_shuo_min(data["附件"])
    rf.add_name_date(data["发文机关"],data["成文日期"])
    rf.add_fujian(data["附件"])
    rf.add_end(data)

    #156/442.5 纸张mm数比线条单位比值  33+10.5x换算成
    #new_document.SaveAs("G:/python/win32com/3.docx")
    #new_document.Close()
    #app.Quit()
def genup():
    start()

    pass
if __name__ == '__main__':

    data={"份号":"234567","保密等级":"紧急","保密期限":"2年","紧急程度":"特急",
          "发文机关":["湖南省娄底市湘潭农业农村局","县扶贫开发办","县劳动与保障局"],
          "发文机关代字":"泸农发","年份":"2019","发文号":"6",
          "标题":"XX县农业农村局关于什么",
          "文件内容":"局属各单位：\n根据。。。。。。。。。。\n\n\n\n\n\n\n\n\n\n\n\n结束",
          "成文日期":"2020年6月12日",
          "附件":["湖北省武汉市事发地点发送到发送到杀对方水电费第三方第三方第三方士大夫地方","湖北省武汉市事发地点发送到发送到杀对方水电费第三方第三方第三方士大夫地方"],
          "主送机关":"县畜牧局、中华人民共和国内蒙古、中国甘肃省那然色布斯台音布拉格农业综合执法局、中国甘肃省那然色布斯台音布拉格农业综合执法局",
          "抄送机关":"县畜牧局、中华人民共和国内蒙古、中国甘肃省那然色布斯台音布拉格农业综合执法局、中国甘肃省那然色布斯台音布拉格农业综合执法局",
          "印发机关":"县农业农村局",
          "印发日期":"2020年3月21日"}
    gendown(data)