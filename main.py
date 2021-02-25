import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
import os

from src.interface.XiaXingWen import Xiaxinwen
from src.interface.ShangXingWen import Shangxinwen
from src.interface.XinHan import XinHan
from src.interface import redfileWigets
from src.interface import about_dialog
from simpleConfig import *

def set_win_center(root, curWidth='', curHight=''):
    #设置窗口大小，并居中显示
    #:param root:主窗体实例
    #:param curWidth:窗口宽度，非必填，默认200
    #:param curHight:窗口高度，非必填，默认200
    #:return:无
    if not curWidth:
        '''获取窗口宽度，默认200'''
        curWidth = root.winfo_width()
    if not curHight:
        '''获取窗口高度，默认200'''
        curHight = root.winfo_height()
    # 获取屏幕宽度和高度
    scn_w, scn_h = root.maxsize()
    # print(scn_w, scn_h)

    # 计算中心坐标
    cen_x = (scn_w - curWidth) / 2
    cen_y = (scn_h - curHight) / 2
    # print(cen_x, cen_y)

    # 设置窗口初始大小和位置
    size_xy = '%dx%d+%d+%d' % (curWidth, curHight, cen_x, cen_y)
    root.geometry(size_xy)
def hello():
    pass
def open_peizhi(filename=None):
    if filename==None:
        fname=tk.filedialog.askopenfilename(title='加载配置',filetypes=[('red files','.redfile'), ('all files', '.*')])
        if fname=="":
            return
    else:
        fname=filename
    with open(fname) as file_obj:
        data = json.load(file_obj)
    tabclass=data["公文种类"]
    del data["公文种类"]
    tabs[tabclass].setData(data)
    if filename==None:
        tabview.select(tabs[tabclass])
        write_config("main", tabsname[tabclass], fname)

def save_peizhi():
    filename=tk.filedialog.asksaveasfilename(title='保存配置', defaultextension=".redfile",
                                    filetypes=[('red files', '.redfile'), ('all files', '.*')])
    if filename=="":
        return
    Current_tab = tabview.tab(tabview.select(), "text")
    data=tabs[Current_tab].getData()
    data["公文种类"]=Current_tab
    with open(filename, 'w') as file_obj:
        json.dump(data, file_obj, indent=2, ensure_ascii=False)

def about():
    about_dialog.MyDialog(root)

def addMenu(root):
    menubar = tk.Menu(root)

    # create a pulldown menu, and add it to the menu bar
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="加载配置", command=open_peizhi)
    filemenu.add_command(label="保存配置", command=save_peizhi)
    menubar.add_cascade(label="文件", menu=filemenu)

    # create more pulldown menus
    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="关闭输入提示", command=hello)
    menubar.add_cascade(label="选项", menu=editmenu)

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="关于", command=about)
    menubar.add_cascade(label="帮助", menu=helpmenu)

    # display the menu
    root.config(menu=menubar)

    redfileWigets.menubar = tk.Menu(root, tearoff=False)  # 添加右键菜单

def ok(tabview):
    Current_tab=tabview.tab(tabview.select(), "text")
    tabs[Current_tab].apply()

def buttonbox(root):
    # add standard button box. override if you don't want the
    # standard buttons
    box = tk.Frame(root)
    gen = tk.Button(box, text="点击生成", width=10, command=lambda: ok(tabview), default=tk.ACTIVE)
    gen.pack(side=tk.RIGHT, padx=5, pady=5)
    box.pack()




def getkey(dic,value):
    for key in dic:
        if dic[key] == value:
            return key

def closeWindow():
    Current_tab = tabview.tab(tabview.select(), "text")
    write_config("main", "current_tab", tabsname[Current_tab])
    root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("公文生成器")
    addMenu(root)
    tabs={}
    tabsname={}
    tabview=ttk.Notebook(root)

    tab1=Xiaxinwen(tabview)
    tabs["下行文"]=tab1
    tabsname["下行文"]="xia_xing_wen"
    tabview.add(tab1,text="下行文")

    tab2 = Shangxinwen(tabview)
    tabs["上行文"] = tab2
    tabsname["上行文"] = "shang_xing_wen"
    tabview.add(tab2, text="上行文")

    tab3=XinHan(tabview)
    tabs["信函"] = tab3
    tabsname["信函"] = "xin_han"
    tabview.add(tab3, text="信函")

    tabview.pack(expand=True, fill=tk.BOTH)



    buttonbox(root)
    #set_win_center(root, 450, 600)
    for key in tabsname:
        filepath=read_config("main",tabsname[key],"")
        if  os.path.exists(filepath):
            open_peizhi(filename=filepath)
    ishint=read_config("main","is_hint","true")
    ctab=read_config("main", "current_tab","xia_xing_wen")
    tabview.select(tabs[getkey(tabsname,ctab)])
    root.protocol('WM_DELETE_WINDOW', closeWindow)
    root.mainloop()
