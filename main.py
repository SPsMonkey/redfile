import tkinter as tk
from XiaXingWen import Xiaxinwen
from ShangXingWen import Shangxinwen
from tkinter import ttk
from tkinter import filedialog
import json
import redfileWigets
import about_dialog
import configparser
import os

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
        filename=tk.filedialog.askopenfilename(title='加载配置',filetypes=[('red files','.redfile'), ('all files', '.*')])
        if filename=="":
            return
        write_config("main","peizhi",filename)
    with open(filename) as file_obj:
        data = json.load(file_obj)
    Current_tab = tabview.tab(tabview.select(), "text")
    tabs[Current_tab].setData(data)

def save_peizhi():
    filename=tk.filedialog.asksaveasfilename(title='保存配置', defaultextension=".redfile",
                                    filetypes=[('red files', '.redfile'), ('all files', '.*')])
    if filename=="":
        return
    Current_tab = tabview.tab(tabview.select(), "text")
    data=tabs[Current_tab].getData()
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

def create_config():
    config = configparser.ConfigParser()
    config['main'] = {'peizhi': ' ','is_hint':'true'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def read_config(section,key):
    if not os.path.exists('config.ini'):
        create_config()
    config = configparser.ConfigParser()
    config.read('config.ini')
    if not (section in config.sections()):
        config.add_section(section)
    if not(key in config[section]):
        if key=="peizhi":
            config.set(section,key," ",)
        if key=="is_hint":
            config.set(section, key, 'true', )
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    result=config[section][key]
    return result


def write_config(section,key,value):
    config = configparser.ConfigParser()
    config[section] = {key: value}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


if __name__ == '__main__':
    root = tk.Tk()
    addMenu(root)
    tabs={}
    tabview=ttk.Notebook(root)

    tab1=Xiaxinwen(tabview)
    tabs["下行文"]=tab1
    tabview.add(tab1,text="下行文")

    tab2 = Shangxinwen(tabview)
    tabs["上行文"] = tab2
    tabview.add(tab2, text="上行文")
    tabview.pack(expand=True, fill=tk.BOTH)

    buttonbox(root)
    #set_win_center(root, 450, 600)
    filepath=read_config("main","peizhi")
    if  os.path.exists(filepath):
        open_peizhi(filename=filepath)
    ishint=read_config("main","is_hint")

    root.mainloop()
