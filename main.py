import tkinter as tk
from XiaXingWen import Xiaxinwen
from tkinter import ttk
from tkinter import filedialog
import json
import redfileWigets
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
def open_peizhi():
    filename=tk.filedialog.askopenfilename(title='加载配置',filetypes=[('red files','.redfile'), ('all files', '.*')])
    if filename=="":
        return
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
    pass

def addMenu(root):
    menubar = tk.Menu(root)

    # create a pulldown menu, and add it to the menu bar
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="加载配置", command=open_peizhi)
    filemenu.add_command(label="保存配置", command=save_peizhi)
    menubar.add_cascade(label="文件", menu=filemenu)

    # create more pulldown menus
    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=hello)
    editmenu.add_command(label="Copy", command=hello)
    editmenu.add_command(label="Paste", command=hello)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="关于", command=hello)
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

if __name__ == '__main__':
    root = tk.Tk()
    addMenu(root)
    tabs={}
    tabview=ttk.Notebook(root)

    tab3=Xiaxinwen(tabview)
    tabs["下行文"]=tab3
    tabview.add(tab3,text="下行文")
    tabview.pack(expand = True, fill = tk.BOTH)

    buttonbox(root)
    #set_win_center(root, 450, 600)
    root.mainloop()
