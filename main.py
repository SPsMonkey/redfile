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

if __name__ == '__main__':
    root = tk.Tk()
    tabview=ttk.Notebook(root)

    tab1=tk.Frame(tabview)
    tabview.add(tab1, text='Label')

    tab2 = tk.Frame(tabview)
    tabview.add(tab2, text='Button')

    tab3=Xiaxinwen(tabview)
    tabview.add(tab3,text="test")

    label1 = tk.Label(tab1, text='标签1')
    label1.pack()
    button1 = tk.Button(tab2, text='按钮1', width=20)
    button1.pack()

    tabview.pack(expand = True, fill = tk.BOTH)
    set_win_center(root, 300, 300)
    root.mainloop()
