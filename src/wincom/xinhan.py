
from .downfile import downfile
from .until import *
class xinhan(downfile):
    def __init__(self,data):
        doc.__init__(self,data)

    def add_xin_han_title(self,str, isredpaper):  # 绘制信函格式的大红头和上边下边的双红线
        str=self.data["发文机关"]
        isredpaper=self.data["是否使用红头纸"]
        self.s.TypeText("\n")
        shape = doc.Shapes.AddTextbox(1, 79.38, 3 * cm_to_points - 8.93, 442.26, 80,
                                      doc.Range(0, 0))  # 使用文本框来写大红头，大红头字距离上边3cm,要剪掉字上边的空白
        shape.Line.Visible = 0
        shape.RelativeHorizontalPosition = 1
        shape.RelativeVerticalPosition = 1
        textbox = shape.TextFrame
        textbox.MarginBottom = 0
        textbox.MarginTop = 0
        textbox.MarginRight = 0
        textbox.MarginLeft = 0
        textbox.HorizontalAnchor = 2
        textbox.TextRange.Text = str[0]
        textbox.TextRange.font.Name = "方正小标宋简体"
        textbox.TextRange.font.Size = font_size["小初"]
        textbox.TextRange.font.Color = 255
        textbox.TextRange.ParagraphFormat.Alignment = 1  # 1是居中0 是靠左 2是靠右
        maxlen = len(str[0])  # 找出字数最长的单位
        if maxlen > 12:
            textbox.TextRange.Font.Scaling = int(12 * 100 / maxlen)
        drawTheRedLine(139.0645, False)
        drawTheRedLine(143.0645, False, 1.5)
        drawTheRedLine(29.7 * cm_to_points - 2 * cm_to_points - 5, False, 1.5)
        drawTheRedLine(29.7 * cm_to_points - 2 * cm_to_points - 1, False)

        self.s.TypeText("\n")
        self.s.Font.Scaling = 100

    def add_redfile_num(self):(groupname, sybol, year, num, adjust):

        if len(groupname) > 1:
            # 计算需要的空格数一行总共28个全角字符 减去签发人4个末尾空格一个 再减去姓名字数
            if adjust == False:
                n = 23 - len(groupname[0])
                s.TypeText(n * chr(12288) + "签发人：")
            else:
                s.TypeText(adjust * " ")
            setFont("楷体")
            s.TypeText(groupname[0] + "\n")
            for i in range(1, len(groupname)):
                if i == len(groupname) - 1:
                    setFont("仿宋")
                    s.TypeText(chr(12288) + sybol + "〔" + year + "〕" + num + "号")
                    if adjust == False:
                        n = 46 - len(groupname[0]) * 2 - len(sybol) * 2 - len(num) - len(year)
                    else:
                        n = adjust - len(sybol) * 2 - len(num) - len(year) - 8
                    s.TypeText(n * " ")
                    s.Text = groupname[i]
                    setFont("楷体")
                else:
                    s.TypeText(adjust * " " + groupname[i] + "\n")
        else:
            s.TypeText(chr(12288) + sybol + "〔" + year + "〕" + num + "号")
            if adjust == False:
                n = 38 - len(sybol) * 2 - len(num) - len(year) - len(groupname[0]) * 2
                s.TypeText(n * " " + "签发人：")
            else:
                s.TypeText(adjust * " ")
            s.Text = groupname[0]
            setFont("楷体")
        if adjust == False:
            cY = getPosY()  # 获取输入点所在的高度
            drawTheRedLine(cY + 28, s.Range)
        s.MoveRight()
        s.TypeText("\n")