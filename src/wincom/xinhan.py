
from .downfile import downfile
from .until import *
class xinhan(downfile):
    def __init__(self,data):
        downfile.__init__(self,data)

    def add_xin_han_title(self):  # 绘制信函格式的大红头和上边下边的双红线
        str=self.data["发文机关"]
        isredpaper=self.data["是否使用红头纸"]
        self.s.TypeText("\n")
        shape = self.doc.Shapes.AddTextbox(1, 79.38, 3 * cm_to_points - 8.93, 442.26, 80,
                                      self.doc.Range(0, 0))  # 使用文本框来写大红头，大红头字距离上边3cm,要剪掉字上边的空白
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
        self.drawTheRedLine(139.0645, False)
        self.drawTheRedLine(143.0645, False, 1.5)
        self.drawTheRedLine(29.7 * cm_to_points - 2 * cm_to_points - 5, False, 1.5)
        self.drawTheRedLine(29.7 * cm_to_points - 2 * cm_to_points - 1, False)

        self.s.TypeText("\n")
        self.s.Font.Scaling = 100

