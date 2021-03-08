import math
from .until import *

from win32com.client import Dispatch

class doc(base_doc):
    def __init__(self,data):
        base_doc.__init__(self)
        self.data=data
        self.setPage()

    def addFileNum(self):  # 份号
        self.setFont("仿宋", "三号")
        self.s.TypeText(self.data["份号"])
        self.s.TypeText("\n")

    def add_SecurityLevel_Time(self):  # 保密等级及保密期限
        level=self.data["保密等级"]
        time=self.data["保密期限"]
        if level == "无":
            pass
        else:
            self.setFont("黑体", "三号")
            self.s.TypeText(level)
            self.s.InsertSymbol(Font="黑体", CharacterNumber=9733, Unicode=True)  # 插入五角星
            self.s.TypeText(time)
        self.s.TypeText("\n")

    def add_emergency_level(self):
        str=self.data["紧急程度"]
        if str == "无":
            pass
        else:
            self.setFont("黑体", "三号")
            self.s.TypeText(str)
        self.s.TypeText("\n")

    def add_red_title(self):  # 添加大红头
        str=self.data["发文机关"]
        isRedPaper=self.data["是否使用红头纸"]
        s=self.s
        if isRedPaper == 1:
            self.setFont()
            return
        else:
            self.setFont("方正小标宋简体", "小初", "红色")
            self.s.ParagraphFormat.Alignment = 1  # 1是居中0 是靠左 2是靠右
            maxwidth = 15.6  # 表格最大宽度 单位cm 初号字正常宽度1.3 如果超过12个字就需要压缩字宽度

            maxlen = len(str[0])  # 找出字数最长的单位
            for i in str:
                if maxlen < len(i):
                    maxlen = len(i)
            maxlen = maxlen + 2

            if len(str) == 1:  # 单个单位行文
                s.Text = str[0] + "文件"
                if maxlen > 12:
                    s.Font.Scaling = int(12 * 100 / maxlen)
                s.MoveRight()
                s.TypeText("\n")
                s.Font.Scaling = 100

            else:  # 多个单位联合行文
                table = doc.Tables.Add(s.Range, len(str), 2)  # 创建有2列多行的一个表格
                table.Range.Rows.Alignment = 1
                cols = table.Columns
                if maxlen >= 12:  # 如果超过12个字符表格设置到最宽，列宽按比例分配
                    cols(1).Width = (14.84 * (maxlen - 2) / maxlen + 0.38) * cm_to_points
                    cols(2).Width = (14.84 * 2 / maxlen + 0.38) * cm_to_points
                else:
                    cols(1).Width = (15.6 * (
                                maxlen - 2) / 12 + 0.38) * cm_to_points  # 因为word生成的表格有个默认的左右边距0.19cm，所以需要加上0.38
                    cols(2).Width = (15.6 * 2 / 12 + 0.38) * cm_to_points

                cell = table.Cell(1, 2)  # 将第二列合为一个单元格
                for i in range(0, len(str) - 1):
                    cell.Merge(table.Cell(i + 2, 2))
                cell.VerticalAlignment = 1

                for i in range(0, len(str)):  # 第一列输入所有单位名称
                    s.Text = str[i]
                    if len(str[i]) + 2 >= 12:  # 字数超过10个则需要把字压扁
                        s.Font.Scaling = int(11.8 * 100 / (len(str[i]) + 2))
                    s.ParagraphFormat.Alignment = 4  # 分散对齐
                    s.MoveRight()
                    s.Font.Scaling = 100
                    s.MoveDown()

                cell.Select()
                s.Text = "文件"
                if maxlen >= 12:
                    s.Font.Scaling = int(11.8 * 100 / maxlen)
                s.MoveDown()

            self.setFont()
            s.TypeText("\n")

    def add_redfile_num(self):#添加发文机关代字文件号
        sybol=self.data["发文机关代字"]
        year=self.data["年份"]
        num=self.data["发文号"]
        isRedPaper=self.data["是否使用红头纸"]
        adjustNumber=self.data["高度调整"]
        s=self.s
        self.setFont()
        s.ParagraphFormat.Alignment = 1
        if isRedPaper == 1:
            s.TypeBackspace()
            s.ParagraphFormat.DisableLineHeightGrid = True
            s.ParagraphFormat.WordWrap = True
            s.ParagraphFormat.LineSpacingRule = 4  # 固定值
            row = 0
            while adjustNumber > 10.5:
                adjustNumber = adjustNumber - 10.5
                row = row + 1
            s.ParagraphFormat.LineSpacing = adjustNumber * 2.835
            s.TypeText("\n")
            s.ParagraphFormat.LineSpacingRule = 0  # 单倍行距
            s.ParagraphFormat.DisableLineHeightGrid = False
            s.ParagraphFormat.WordWrap = False
            s.TypeText("\n" * row)
            s.Text = sybol + "〔" + year + "〕" + num + "号"
            s.MoveRight()
            s.TypeText("\n")
            s.ParagraphFormat.DisableLineHeightGrid = True
            s.ParagraphFormat.WordWrap = True
            s.ParagraphFormat.LineSpacingRule = 4  # 固定值
            s.ParagraphFormat.LineSpacing = (10.5 - adjustNumber) * 2.835
            s.TypeText("\n")
            s.ParagraphFormat.LineSpacing = 29.7675
        else:
            s.Text = sybol + "〔" + year + "〕" + num + "号"
            cY = self.getPosY()  # 获取输入点所在的行数
            self.drawTheRedLine(cY + 28, s.Range)
            s.MoveRight()
            s.TypeText("\n")

    def add_title(self):  # 添加标题，行间距要调成固定值29.7675磅 不然会占用2行
        s=self.s
        str=self.data["标题"]
        self.setFont("方正小标宋简体", "二号")
        s.ParagraphFormat.Alignment = 1  # 居中
        s.ParagraphFormat.DisableLineHeightGrid = True
        s.ParagraphFormat.WordWrap = True
        s.ParagraphFormat.LineSpacingRule = 4  # 固定值
        s.ParagraphFormat.LineSpacing = 29.7675
        s.TypeText(str)

        s.TypeText("\n")
        self.setFont()
        s.ParagraphFormat.LineSpacingRule = 0  # 单倍行距
        s.ParagraphFormat.DisableLineHeightGrid = False
        s.ParagraphFormat.WordWrap = False
        


def add_red_num_and_qian_fa_ren(sybol,year,num,names,isRedPaper,adjustNumber,adjustNumber2):
    self.setFont()
    s.ParagraphFormat.Alignment = 0 #左对齐
    s.ParagraphFormat.AddSpaceBetweenFarEastAndDigit=False #这个选项为段落里自动调整中文与数字之间的距离，会在中文和数字间加了额外距离
    Names = names.split()
    # 把姓名分成2名一组，名字中间用空格隔开
    groupname = []
    for i in range(0, len(Names), 2):
        groupname.append(Names[i:i + 2])
    # 找到第一列名字最长长度
    max1 = 0
    for name in groupname:
        if len(name[0]) > max1:
            max1 = len(name[0])
    # 找到第二列名字最长长度
    max2 = 0
    for name in groupname:
        if len(name) == 2:
            if len(name[1]) > max2:
                max2 = len(name[1])
    # 插入空格使得名字对齐
    for name in groupname:
        n = max1 - len(name[0])
        name[0] = name[0] + n * "　"
        if len(name) == 2:
            n = max2 - len(name[1])
            name[1] = name[1] + n * "　"
    for i in range(0, len(groupname)):
        if len(groupname[i]) == 2:
            groupname[i] = groupname[i][0] + "　" + groupname[i][1]
        else:
            groupname[i] = groupname[i][0]
    if isRedPaper==1:
        s.TypeBackspace()
        s.ParagraphFormat.DisableLineHeightGrid = True
        s.ParagraphFormat.WordWrap = True
        s.ParagraphFormat.LineSpacingRule = 4  # 固定值
        row=0
        while adjustNumber>10.5:
            adjustNumber=adjustNumber-10.5
            row=row+1
        s.ParagraphFormat.LineSpacing =adjustNumber*2.835
        s.TypeText("\n")
        s.ParagraphFormat.LineSpacingRule = 0  # 单倍行距
        s.ParagraphFormat.DisableLineHeightGrid = False
        s.ParagraphFormat.WordWrap = False
        s.TypeText("\n"*row)
        typerednum(groupname,sybol,year,num,adjustNumber2)
        s.ParagraphFormat.DisableLineHeightGrid = True
        s.ParagraphFormat.WordWrap = True
        s.ParagraphFormat.LineSpacingRule = 4  # 固定值
        s.ParagraphFormat.LineSpacing = (10.5-adjustNumber) * 2.835
        s.TypeText("\n")
        s.ParagraphFormat.LineSpacing = 29.7675
    else:
        typerednum(groupname,sybol,year,num,False)
    s.ParagraphFormat.AddSpaceBetweenFarEastAndDigit = True



def add_content(str):
    self.setFont()
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
    self.setFont()
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
        add_line(s.Range, row_current-1+row_zhuson+row_chaoson, 0.7, 0)
        add_line(s.Range, row_current +row_zhuson+row_chaoson, 1, 0)
    else:
        if chaoson!="":
            s.Text="抄送："+chaoson
            add_line(s.Range, row_current - 1, 1, 0)
            s.MoveRight()
            s.TypeText("\n")
            s.Text = yinfa + " " * space + date + "印发"
            add_line( s.Range, row_current-1+row_chaoson, 0.7, 0)
            add_line( s.Range, row_current + row_chaoson, 1, 0)
        else:
            s.Text = yinfa + " " * space + date + "印发"
            add_line(s.Range, row_current - 1, 1, 0)
            add_line( s.Range, row_current , 1, 0)

