from win32com.client import Dispatch
cm_to_points = 28.35  # 1厘米为28.35磅

def add_line(doc,anchor,n,weight,color):
    line_height=(33+10.5*n)*2.835 # 442.5/156
    line=doc.Shapes.AddLine(79, line_height, 521.5, line_height,anchor).line
    line.Weight=weight
    line.ForeColor.RGB=color


def setPage(doc):#页面页面字号设置
    # 页面设置

    # 国家公文格式标准要求是上边距版心3.7cm
    # 但是如果简单的把上边距设置为3.7cm
    # 则因为文本的第一行本身有行距
    # 会导致实际版心离上边缘较远，上下边距设置为3.3cm
    # 是经过实验的，可以看看公文标准的图示
    # 版心指的是文字与边缘距离
    doc.PageSetup.TopMargin = 3.3 * cm_to_points
    # 上边距3.3厘米
    doc.PageSetup.BottomMargin = 3.3 * cm_to_points
    # 下边距3.3厘米
    doc.PageSetup.LeftMargin = 2.8 * cm_to_points
    # 左边距2.8厘米
    doc.PageSetup.RightMargin = 2.6 * cm_to_points
    # 右边距2.6厘米

    # 设置正常样式的字体
    # 是为了后面指定行和字符网格时
    # 按照这个字体标准进行
    doc.Styles(-1).Font.Name = '仿宋'
    # word中的“正常”样式字体为仿宋
    doc.Styles(-1).Font.NameFarEast = '仿宋'
    # word中的“正常”样式字体为仿宋
    doc.Styles(-1).Font.NameAscii = '仿宋'
    # word中的“正常”样式字体为仿宋
    doc.Styles(-1).Font.NameOther = '仿宋'
    # word中的“正常”样式字体为仿宋
    doc.Styles(-1).Font.Size = 16
    # word中的“正常”样式字号为三号

    doc.PageSetup.LayoutMode = 1
    # 指定行和字符网格
    doc.PageSetup.CharsLine = 28
    # 每行28个字
    doc.PageSetup.LinesPage = 22
    # 每页22行，会自动设置行间距

    # 页码设置
    doc.PageSetup.FooterDistance = 2.4 * cm_to_points
    # 页码距下边缘2.8厘米
    doc.PageSetup.DifferentFirstPageHeaderFooter = 0
    # 首页页码相同
    doc.PageSetup.OddAndEvenPagesHeaderFooter = 0
    # 页脚奇偶页相同
    w = doc.windows(1)
    # 获得文档的第一个窗口
    w.view.seekview = 4
    # 获得页眉页脚视图
    s = w.selection
    # 获取窗口的选择对象
    s.headerfooter.pagenumbers.startingnumber = 1
    # 设置起始页码
    s.headerfooter.pagenumbers.NumberStyle = 0
    # 设置页码样式为单纯的阿拉伯数字
    s.WholeStory()
    # 扩选到整个部分（会选中整个页眉页脚）
    s.Delete()
    # 按下删除键，这两句是为了清除原来的页码
    s.headerfooter.pagenumbers.Add(4)
    # 添加页面外侧页码
    s.MoveLeft(1, 2)
    # 移动到页码左边，移动了两个字符距离
    s.TypeText('— ')
    # 给页码左边加上一字线，注意不是减号
    s.MoveRight()
    # 移动到页码末尾，移动了一个字符距离
    # 默认参数是1（字符）
    s.TypeText(' —')
    s.WholeStory()
    # 扩选到整个页眉页脚部分，此处是必要的
    # 否则s只是在输入一字线后的一个光标，没有选择区域
    s.Font.Name = '宋体'
    s.Font.Size = 14
    # 页码字号为四号
    s.paragraphformat.rightindent = 21
    # 页码向左缩进1字符（21磅）
    s.paragraphformat.leftindent = 21
    # 页码向右缩进1字符（21磅）
    doc.Styles('页眉').ParagraphFormat.Borders(-3).LineStyle = 0
    # 页眉无底边框横线

    w.view.seekview = 0

def addFileNum(s,str):#份号
    s.font.Name = '仿宋'
    # 字号设置为三号
    s.font.Size = 16
    s.TypeText(str)
    s.TypeText("\n")

def add_SecurityLevel_Time(s,level,time):#保密等级及保密期限
    s.font.Name = '黑体'
    # 字号设置为三号
    s.font.Size = 16
    s.TypeText(level)
    s.InsertSymbol(Font = "黑体", CharacterNumber = 9733, Unicode = True)
    s.TypeText(time)
    s.TypeText("\n")

def add_emergency_level(s,str):
    s.font.Name = '黑体'
    # 字号设置为三号
    s.font.Size = 16
    s.TypeText(str)
    s.TypeText("\n")

def add_red_title(s,str):
    s.font.Name = '方正小标宋简体'
    # 字号设置为三号
    s.font.Size = 36
    s.font.color=255
    s.ParagraphFormat.Alignment=1#1是居中0 是靠左 2是靠右
    if len(str)==1:
        s.TypeText(str[0]+"文件")
        s.TypeText("\n")
    else:
        pass
    s.font.Size = 16
    s.TypeText("\n\n")

def add_redfile_num(s,sybol,year,num):
    s.font.Name = '仿宋'
    # 字号设置为三号
    s.font.Size = 16
    s.font.color = 0
    s.ParagraphFormat.Alignment = 1
    s.TypeText(sybol)
    s.InsertSymbol(Font="仿宋", CharacterNumber=12308, Unicode=True)
    s.TypeText(year)
    s.InsertSymbol(Font="仿宋", CharacterNumber=12309, Unicode=True)
    s.TypeText(num+"号")
    s.TypeText("\n\n\n")

def add_title(s,str):
    s.font.Name = '方正小标宋简体'
    # 字号设置为三号
    s.font.Size = 22
    s.font.color = 0
    s.ParagraphFormat.Alignment = 1
    s.TypeText(str)
    s.TypeText("\n\n")

def add_content(s,str):
    s.font.Name = '仿宋'
    # 字号设置为三号
    s.font.Size = 16
    s.font.color = 0
    s.ParagraphFormat.Alignment = 0
    s.TypeText(str)

def add_name_date(s,name,date):
    s.font.Name = '仿宋'
    # 字号设置为三号
    s.font.Size = 16
    s.font.color = 0
    s.TypeText("\n\n\n")
    s.ParagraphFormat.Alignment = 2
    s.TypeText(name)
    s.TypeText("\b\b\b\b\n")
    s.TypeText(date)
    s.TypeText("\b\b\b\b\n")

def add_end(d,s,chaoson,yinfa,date):#添加版记 包括抄送 印发机关 印发日期
    s.ParagraphFormat.Alignment = 0
    s.font.Name = '仿宋'
    # 字号设置为三号
    s.font.Size = 14
    table=d.Tables.Add(s.Range,2,1)
    table.LeftPadding=14
    table.RightPadding = 14
    # -3是底边-1 是顶边 -5是中间的水平边
    topborder=table.Borders(-1)
    topborder.LineStyle=1
    topborder.LineWidth=4
    bottomborder=table.Borders(-3)
    bottomborder.LineStyle = 1
    bottomborder.LineWidth = 4
    midborder=table.Borders(-5)
    midborder.LineStyle = 1
    midborder.LineWidth = 2
    s.TypeText("抄送："+chaoson)
    s.MoveDown()
    s.TypeText("印发机关："+yinfa+"印发日期："+date+"印发")



def gen(data):
    app = Dispatch('word.Application')
    # 新建word文档
    app.Visible = True
    doc = app.Documents.Add()

    setPage(doc)
    selection = doc.Application.Selection
    addFileNum(selection, data["份号"])
    add_SecurityLevel_Time(selection, data["保密等级"],data["保密期限"])
    add_emergency_level(selection,data["紧急程度"])
    add_red_title(selection,data["发文机关"])
    add_redfile_num(selection,data["发文机关代字"],data["年份"],data["发文号"])
    add_title(selection,data["标题"])
    add_line(doc, doc.Range(0,1), 8, 3, 255)
    add_content(selection,data["文件内容"])
    add_name_date(selection,data["发文机关"][0],data["成文日期"])
    add_end(doc,selection,data["抄送机关"],data["印发机关"],data["印发日期"])



    #156/442.5 纸张mm数比线条单位比值  33+10.5x换算成



    #new_document.SaveAs("G:/python/win32com/3.docx")
    #new_document.Close()
    #app.Quit()
if __name__ == '__main__':

    data={"份号":"234567","保密等级":"紧急","保密期限":"2年","紧急程度":"特急",
          "发文机关":["XX县农业农村局"],
          "发文机关代字":"泸农发","年份":"2019","发文号":"6",
          "标题":"XX县农业农村局关于什么",
          "文件内容":"局属各单位：\n根据。。。。。。。。。。\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
          "成文日期":"2020年6月12日",
          "抄送机关":"XX县畜牧局",
          "印发机关":"XX县农业农村局",
          "印发日期":"2020年3月21日"}
    gen(data)