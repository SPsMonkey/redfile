
from win32com.client import Dispatch

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

class doc():
    def __init__(self):
        app = Dispatch('word.Application')
        # 新建word文档
        app.Visible = True
        self.doc = app.Documents.Add()
        self.s = app.Selection

    def setFont(self,fontName="仿宋",size="三号",color="黑色"):
        self.s.font.Name=fontName
        if type(size)==type(1) or type(size)==type(1.5):
            self.s.font.size=size
        else:
            self.s.font.size=font_size[size]
        if color == "黑色":
            self.s.font.color=0
        elif color=="红色":
            self.s.font.color=255
        else:
            self.s.font.color=color
            
    def inser_empty_row(self,n_row):
        self.s.TypeText("\n" * n_row)
        
    def getPosY(self):#获取选择点距离上页面上边缘的磅数
        return self.s.Information(6)  #5就是x

    def add_line(self,anchor,n,weight,color): #在文档中添加横线
        line_height=(33+10.5*n)*2.835 # 442.5/156
        line=self.doc.Shapes.AddLine(79, line_height, 521.5, line_height,anchor).line
        line.Weight=weight
        line.ForeColor.RGB=color

    def drawTheRedLine(self,height,anchor,weight=3):
        if anchor==False:
            shape= self.doc.Shapes.AddLine(79, height, 521.5, height)
            line=shape.line
            shape.RelativeHorizontalPosition=1
            shape.RelativeVerticalPosition = 1
        else:
            line = self.doc.Shapes.AddLine(79.38, height, 521.64, height, anchor).line
        line.Weight = weight
        line.ForeColor.RGB = 255

    def setPage(self):#页面页面字号设置
        # 页面设置
    
        # 国家公文格式标准要求是上边距版心3.7cm
        # 但是如果简单的把上边距设置为3.7cm
        # 则因为文本的第一行本身有行距
        # 会导致实际版心离上边缘较远，上下边距设置为3.3cm
        # 是经过实验的，可以看看公文标准的图示
        # 版心指的是文字与边缘距离
        self.doc.PageSetup.TopMargin = 3.3 * cm_to_points
        # 上边距3.3厘米
        self.doc.PageSetup.BottomMargin = 3.3 * cm_to_points
        # 下边距3.3厘米
        self.doc.PageSetup.LeftMargin = 2.8 * cm_to_points
        # 左边距2.8厘米
        self.doc.PageSetup.RightMargin = 2.6 * cm_to_points
        # 右边距2.6厘米
    
        # 设置正常样式的字体
        # 是为了后面指定行和字符网格时
        # 按照这个字体标准进行
        self.doc.Styles(-1).Font.Name = '仿宋'
        # word中的“正常”样式字体为仿宋
        self.doc.Styles(-1).Font.NameFarEast = '仿宋'
        # word中的“正常”样式字体为仿宋
        self.doc.Styles(-1).Font.NameAscii = '仿宋'
        # word中的“正常”样式字体为仿宋
        self.doc.Styles(-1).Font.NameOther = '仿宋'
        # word中的“正常”样式字体为仿宋
        self.doc.Styles(-1).Font.Size = 16
        # word中的“正常”样式字号为三号
    
        self.doc.PageSetup.LayoutMode = 1
        # 指定行和字符网格
        self.doc.PageSetup.CharsLine = 28
        # 每行28个字
        self.doc.PageSetup.LinesPage = 22
        # 每页22行，会自动设置行间距
    
        # 页码设置
        self.doc.PageSetup.FooterDistance = 2.4 * cm_to_points
        # 页码距下边缘2.8厘米
        self.doc.PageSetup.DifferentFirstPageHeaderFooter = 0
        # 首页页码相同
        self.doc.PageSetup.OddAndEvenPagesHeaderFooter = 0
        # 页脚奇偶页相同
        w = self.doc.windows(1)
        # 获得文档的第一个窗口
        w.view.seekview = 4
        # 获得页眉页脚视图
        se = w.Selection
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
        self.doc.Styles('页眉').ParagraphFormat.Borders(-3).LineStyle = 0
        # 页眉无底边框横线
    
        w.view.seekview = 0
