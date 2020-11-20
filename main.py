import tkinter as tk
from XiaXingWen import Xiaxinwen
from tkinter import ttk

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
def addMenu(root):
    menubar = tk.Menu(root)

    # create a pulldown menu, and add it to the menu bar
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=hello)
    filemenu.add_command(label="Save", command=hello)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # create more pulldown menus
    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=hello)
    editmenu.add_command(label="Copy", command=hello)
    editmenu.add_command(label="Paste", command=hello)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=hello)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # display the menu
    root.config(menu=menubar)

if __name__ == '__main__':
    root = tk.Tk()
    addMenu(root)
    tabview=ttk.Notebook(root)


    tab3=Xiaxinwen(tabview)
    tabview.add(tab3,text="下行文")


    tabview.pack(expand = True, fill = tk.BOTH)
    set_win_center(root, 500, 600)
    root.mainloop()
