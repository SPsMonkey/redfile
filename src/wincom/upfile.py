from .downfile import downfile
class upfile (downfile):
    def __init__(self,data):
        downfile.__init__(self,data)

    def typerednum(self,groupname, sybol, year, num, adjust):
        s=self.s
        if len(groupname) > 1:
            # 计算需要的空格数一行总共28个全角字符 减去签发人4个末尾空格一个 再减去姓名字数
            if adjust == False:
                n = 23 - len(groupname[0])
                s.TypeText(n * chr(12288) + "签发人：")
            else:
                s.TypeText(adjust * " ")
            self.setFont("楷体")
            s.TypeText(groupname[0] + "\n")
            for i in range(1, len(groupname)):
                if i == len(groupname) - 1:
                    self.setFont("仿宋")
                    s.TypeText(chr(12288) + sybol + "〔" + year + "〕" + num + "号")
                    if adjust == False:
                        n = 46 - len(groupname[0]) * 2 - len(sybol) * 2 - len(num) - len(year)
                    else:
                        n = adjust - len(sybol) * 2 - len(num) - len(year) - 8
                    s.TypeText(n * " ")
                    s.Text = groupname[i]
                    self.setFont("楷体")
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
            self.setFont("楷体")
        if adjust == False:
            cY = self.getPosY()  # 获取输入点所在的高度
            self.drawTheRedLine(cY + 28, s.Range)
        s.MoveRight()
        s.TypeText("\n")

    def add_red_num_and_qian_fa_ren(self):
        sybol=self.data["发文机关代字"]
        year=self.data["年份"]
        num=self.data["发文号"]
        names=self.data["签发人"]
        isRedPaper=self.data["是否使用红头纸"]
        adjustNumber=self.data["高度调整"]
        adjustNumber2=self.data["签发人调整"]
        self.setFont()
        s=self.s
        s.ParagraphFormat.Alignment = 0  # 左对齐
        s.ParagraphFormat.AddSpaceBetweenFarEastAndDigit = False  # 这个选项为段落里自动调整中文与数字之间的距离，会在中文和数字间加了额外距离
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
            self.typerednum(groupname, sybol, year, num, adjustNumber2)
            s.ParagraphFormat.DisableLineHeightGrid = True
            s.ParagraphFormat.WordWrap = True
            s.ParagraphFormat.LineSpacingRule = 4  # 固定值
            s.ParagraphFormat.LineSpacing = (10.5 - adjustNumber) * 2.835
            s.TypeText("\n")
            s.ParagraphFormat.LineSpacing = 29.7675
        else:
            self.typerednum(groupname, sybol, year, num, False)
        s.ParagraphFormat.AddSpaceBetweenFarEastAndDigit = True

