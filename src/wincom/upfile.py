from .downfile import downfile
class upfile (downfile):
    def __init__(self):
        pass

    def add_red_num_and_qian_fa_ren(sybol, year, num, names, isRedPaper, adjustNumber, adjustNumber2):
        self.setFont()
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
            typerednum(groupname, sybol, year, num, adjustNumber2)
            s.ParagraphFormat.DisableLineHeightGrid = True
            s.ParagraphFormat.WordWrap = True
            s.ParagraphFormat.LineSpacingRule = 4  # 固定值
            s.ParagraphFormat.LineSpacing = (10.5 - adjustNumber) * 2.835
            s.TypeText("\n")
            s.ParagraphFormat.LineSpacing = 29.7675
        else:
            typerednum(groupname, sybol, year, num, False)
        s.ParagraphFormat.AddSpaceBetweenFarEastAndDigit = True

