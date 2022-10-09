'''
GitHub项目页：
https://github.com/PumpkinJui/Selector
'''

from tkinter import *
import tkinter.font as tkf
from random import choice
import os

def sel():
    global lt,intro
    if lab['text'] == intro:
        lab['font'] = ft1
    a = choice(lt)
    lab['text'] = a
    win.title('Selector - ' + a)

def sele(event):
    sel()

def exite(event):
    win.destroy()

if os.path.exists('list.txt'):
    ltr = open('list.txt','r')
    lt = ltr.read().splitlines()
    ltr.close()
    lt = set(lt)#去重
    lt = tuple(lt)#给定list时采用的元组
else:
    lt = ('0','1','2','3','4','5','6','7','8','9')#没有给定list时自动采用的元组

intro = '''单击“抽取”按钮或按 Enter 键，以随机抽取一个姓名
长按 Enter 键，以进行“更具有视觉效果”的随机抽取
单击“退出”按钮或按 Esc 键，以退出此程序'''#预设部分使用方法(完整见GitHub)

win = Tk()
win.title('Selector')#创建窗口
win.resizable(0,0)#锁定窗体尺寸

ft1 = tkf.Font(family='LXGW Bright GB',size=90,weight=tkf.BOLD)
ft2 = tkf.Font(family='LXGW Bright GB',size=48)
fti = tkf.Font(family='LXGW Bright GB',size=40,weight=tkf.BOLD)#预设字体样式

lab = Label(win,justify='center',text=intro,font=fti)
lab.grid(row=1,column=1,columnspan=2)#显示文本

bt1 = Button(win,text='抽取',font=ft2,command=sel)
bt2 = Button(win,text='退出',font=ft2,command=win.destroy)#绑定鼠标
bt1.grid(row=2,column=1)
bt2.grid(row=2,column=2)#显示按钮

win.bind('<Return>',sele)#绑定Enter键
win.bind('<Escape>',exite)#绑定Esc键

win.mainloop()
