import math
cm_to_points = 28.35  # 1厘米为28.35磅
font_size={ "初号":42,
            "小初":36,
            "一号":26,
            "小一":24,
            "二号":22,
            "小二":18,
            "三号":16,
            "小三":15,
            "四号":14,
            "小四":12,
            "五号":10.5,
            "小五":9,
            "六号":7.5,
            "小六":6.5,
            "七号":5.5,
            "八号":5
            }
s=None
doc=None
def setFont(fontName="仿宋",size="三号",color="黑色"):
    s.font.Name=fontName
    if type(size)==type(1) or type(size)==type(1.5):
        s.font.size=size
    else:
        s.font.size=font_size[size]
    if color == "黑色":
        s.font.color=0
    elif color=="红色":
        s.font.color=255
    else:
        s.font.color=color
def inser_empty_row(n_row):
    s.TypeText("\n" * n_row)

def add_line(anchor,n,weight,color): #在文档中添加横线
    line_height=(33+10.5*n)*2.835 # 442.5/156
    line=doc.Shapes.AddLine(79, line_height, 521.5, line_height,anchor).line
    line.Weight=weight
    line.ForeColor.RGB=color

def setPage():#页面页面字号设置
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
    se = w.selection
    # 获取窗口的选择对象
    se.headerfooter.pagenumbers.startingnumber = 1
    # 设置起始页码
    se.headerfooter.pagenumbers.NumberStyle = 0
    # 设置页码样式为单纯的阿拉伯数字
    se.WholeStory()
    # 扩选到整个部分（会选中整个页眉页脚）
    se.Delete()
    # 按下删除键，这两句是为了清除原来的页码
    se.headerfooter.pagenumbers.Add(4)
    # 添加页面外侧页码
    se.MoveLeft(1, 2)
    # 移动到页码左边，移动了两个字符距离
    se.TypeText('— ')
    # 给页码左边加上一字线，注意不是减号
    se.MoveRight()
    # 移动到页码末尾，移动了一个字符距离
    # 默认参数是1（字符）
    se.TypeText(' —')
    se.WholeStory()
    # 扩选到整个页眉页脚部分，此处是必要的
    # 否则s只是在输入一字线后的一个光标，没有选择区域
    se.Font.Name = '宋体'
    se.Font.Size = 14
    # 页码字号为四号
    se.paragraphformat.rightindent = 21
    # 页码向左缩进1字符（21磅）
    se.paragraphformat.leftindent = 21
    # 页码向右缩进1字符（21磅）
    doc.Styles('页眉').ParagraphFormat.Borders(-3).LineStyle = 0
    # 页眉无底边框横线

    w.view.seekview = 0

def addFileNum(str):#份号
    setFont("仿宋","三号")
    s.TypeText(str)
    s.TypeText("\n")

def add_SecurityLevel_Time(level,time):#保密等级及保密期限
    if level=="无":
        pass
    else:
        setFont("黑体","三号")
        s.TypeText(level)
        s.InsertSymbol(Font = "黑体", CharacterNumber = 9733, Unicode = True) #插入五角星
        s.TypeText(time)
    s.TypeText("\n")

def add_emergency_level(str):
    if str=="无":
        pass
    else:
        setFont("黑体", "三号")
        s.TypeText(str)
    s.TypeText("\n")

def add_red_title(str): #添加大红头
    setFont("方正小标宋简体", "小初","红色")
    s.ParagraphFormat.Alignment=1#1是居中0 是靠左 2是靠右
    maxwidth=15.6 #表格最大宽度 单位cm 初号字正常宽度1.3 如果超过12个字就需要压缩字宽度

    maxlen=len(str[0])#找出字数最长的单位
    for i in str:
        if maxlen<len(i):
            maxlen=len(i)
    maxlen=maxlen+2

    if len(str)==1: #单个单位行文
        s.Text=str[0]+"文件"
        if maxlen>12:
            s.Font.Scaling=int(12*100/maxlen)
        s.MoveRight()
        s.TypeText("\n")
        s.Font.Scaling=100

    else:  #多个单位联合行文
        table=doc.Tables.Add(s.Range,len(str),2)  #创建有2列多行的一个表格
        table.Range.Rows.Alignment=1
        cols=table.Columns
        if maxlen>=12: #如果超过12个字符表格设置到最宽，列宽按比例分配
            cols(1).Width=(14.84*(maxlen-2)/maxlen+0.38)*cm_to_points
            cols(2).Width = (14.84*2/maxlen+0.38) * cm_to_points
        else:
            cols(1).Width = (15.6 * (maxlen-2) / 12+0.38) * cm_to_points  #因为word生成的表格有个默认的左右边距0.19cm，所以需要加上0.38
            cols(2).Width = (15.6 * 2 / 12+0.38) * cm_to_points

        cell=table.Cell(1,2) #将第二列合为一个单元格
        for i in range(0,len(str)-1):
            cell.Merge(table.Cell(i+2,2))
        cell.VerticalAlignment=1

        for i in range(0,len(str)): #第一列输入所有单位名称
            s.Text = str[i]
            if len(str[i])+2>=12:#字数超过10个则需要把字压扁
                s.Font.Scaling = int(11.8 * 100 / (len(str[i])+2))
            s.ParagraphFormat.Alignment = 4 #分散对齐
            s.MoveRight()
            s.Font.Scaling = 100
            s.MoveDown()

        cell.Select()
        s.Text="文件"
        if maxlen>=12:
            s.Font.Scaling=int(11.8*100/maxlen)
        s.MoveDown()

    setFont()
    s.TypeText("\n")

def add_redfile_num(sybol,year,num):
    setFont()
    s.ParagraphFormat.Alignment = 1
    s.TypeText(sybol)
    s.InsertSymbol(Font="仿宋", CharacterNumber=12308, Unicode=True)#输入六边形括号
    s.TypeText(year)
    s.InsertSymbol(Font="仿宋", CharacterNumber=12309, Unicode=True)
    s.TypeText(num+"号")
    s.TypeText("\n")

def add_title(str): #行间距要调成固定值29.75磅 不然会占用2行
    setFont("方正小标宋简体","二号")
    s.ParagraphFormat.Alignment = 1
    s.TypeText(str)
    s.TypeText("\n")

def add_content(str):
    setFont()
    s.ParagraphFormat.Alignment = 0
    s.TypeText(str)
    s.TypeText("\n")

def add_fujian_shuo_min(data):
    if data[0]=="":
        return
    else:
        s.TypeText("\n")
        s.TypeText(2 * chr(12288))  # 输入2个全角空格
        s.TypeText("附件：")
        if len(data)==1:
            s.ParagraphFormat.CharacterUnitFirstLineIndent = -5  # 悬挂5个字符
            s.ParagraphFormat.HangingPunctuation = True
            s.TypeText(data[0])
        else:
            s.ParagraphFormat.CharacterUnitFirstLineIndent = -6  # 悬挂3个字符
            s.ParagraphFormat.HangingPunctuation = True
            for i in range(1,len(data)+1):
                s.TypeText(str(i)+"."+data[i-1]+"\n"+5 * chr(12288))
        s.ParagraphFormat.CharacterUnitFirstLineIndent = 0  # 恢复正常段落格式
        s.ParagraphFormat.HangingPunctuation = False

def add_name_date(name,date):
    setFont()
    s.TypeText("\n\n")
    s.ParagraphFormat.Alignment = 2  #段落右对齐
    s.ParagraphFormat.WordWrap = False  #让行末的空格显示出来
    if len(name)==1:
        s.ParagraphFormat.Alignment = 2
        s.TypeText(name[0])
        s.TypeText(2*chr(12288))
        s.TypeText("\n")
        s.TypeText(date)
        s.TypeText(2*chr(12288))
        s.TypeText("\n")
    else:

        for text in name:
            n_col = s.Information(9)  # 获取输入点所在列数
            if n_col + len(text) + 4 > 28:
                s.TypeText("\n\n\n")
            s.TypeText(2*chr(12288))#输入2个全角空格
            s.TypeText(text)
            s.TypeText(2*chr(12288))
        n_col = s.Information(9)  # 获取输入点所在列数
        s.TypeText("\n"+date+"    \n")


def add_fujian(data):
    if data[0]=="":
        return
    else:
        for i in range(1,len(data)+1):
            s.InsertBreak(2)  # 插入分页符
            s.font.Name = '黑体'
            s.font.Size = 16
            s.ParagraphFormat.Alignment = 0
            if len(data)>1:
                s.TypeText("附件" +str(i)+ "\n\n")
            else:
                s.TypeText("附件" + "\n\n")
            s.font.Name = '黑体'
            s.font.Size = 22
            s.ParagraphFormat.Alignment = 1
            s.TypeText(data[i-1] + "\n")
            s.font.Name = '仿宋'
            s.font.Size = 16
            s.ParagraphFormat.Alignment = 0
            if len(data)>1:
                s.TypeText("\n"+2 * chr(12288) + "在此粘贴附件"+str(i)+"内容")
            else:
                s.TypeText("\n"+2 * chr(12288) + "在此粘贴附件内容")
        s.TypeText("\n")

def add_end(data):#添加版记 包括抄送 印发机关 印发日期
    zhuson=""
    chaoson=data["抄送机关"]
    if data["印发机关"]=="":
        yinfa=data["发文机关"][0]
    else:
        yinfa=data["印发机关"]
    if data["印发日期"]=="":
        date=data["成文日期"]
    else:
        date=data["印发日期"]
    s.ParagraphFormat.Alignment = 0
    space=59-len(yinfa)*2-3*2-(len(date)-3)-2-4 #计算印发机关和印发日期中间需要多少空格

    row_zhuson=math.ceil(len(zhuson)/27)#计算主送 需要的总行数，
    row_chaoson=math.ceil(len(chaoson)/27)#计算抄送 需要的总行数
    row_current = s.Information(10)#获取输入点所在的行数
    row_adjust = 22-row_zhuson-row_chaoson - row_current
    while row_adjust<0:#行数不够就加一页
        row_adjust=row_adjust+22

    s.TypeText("\n"*row_adjust)
    row_current = s.Information(10)#获取输入点所在的行数

    s.font.Name = '仿宋'
    # 字号设置为三号
    s.font.Size = 14
    s.ParagraphFormat.Alignment=3 #使用两端对齐看起来更整齐
    s.ParagraphFormat.CharacterUnitLeftIndent = 1
    s.ParagraphFormat.CharacterUnitRightIndent = 1
    s.ParagraphFormat.CharacterUnitFirstLineIndent = -3  # 悬挂3个字符
    s.ParagraphFormat.HangingPunctuation = True
    if zhuson!="":
        s.Text=s.Text="主送："+zhuson
        add_line(s.Range, row_current - 1, 1, 0)
        s.MoveRight()
        s.TypeText("\n")
        if chaoson!="":
            s.TypeText("抄送："+chaoson+"\n")
        s.Text = yinfa + " " * space + date + "印发"
        add_line(s.Range, row_current-1+row_zhuson+row_chaoson, 0.5, 0)
        add_line(s.Range, row_current +row_zhuson+row_chaoson, 1, 0)
    else:
        if chaoson!="":
            s.Text="抄送："+chaoson
            add_line(s.Range, row_current - 1, 1, 0)
            s.MoveRight()
            s.TypeText("\n")
            s.Text = yinfa + " " * space + date + "印发"
            add_line( s.Range, row_current-1+row_chaoson, 0.5, 0)
            add_line( s.Range, row_current + row_chaoson, 1, 0)
        else:
            s.Text = yinfa + " " * space + date + "印发"
            add_line(s.Range, row_current - 1, 1, 0)
            add_line( s.Range, row_current , 1, 0)
