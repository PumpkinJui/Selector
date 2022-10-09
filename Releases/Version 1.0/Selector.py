'''
已知问题：
1. 窗口会动
'''

from tkinter import *
import tkinter.font as tkf
import random

def sel():
    global lt,intro
    if lab['text'] == intro:
        lab['font'] = ft1
    a = random.choice(lt)
    lab['text'] = a
    win.title(a)

def sele(event):
    sel()

def exite(event):
    win.destroy()

lt = ('阿希达','安悦然','白沛林','白书嘉','董子萱','冯耀江','高洪泽',
      '高昕毓','宫宁','贵昊','郭倩','胡景皓','胡妤佳','季国婧',
      '贾晨','贾涵凝','贾晓雪','亢敏','孔令茹','郎佳伟','李璨',
      '李嘉仪','李静雯','李铠诺','李沛哲','李瑞鑫','李政辉','李智',
      '刘家慧','刘恺','刘芮','刘欣','鲁禹志','吕浩玚','石佳琪',
      '孙承楷','田岩松','佟雅茹','王悦','魏宁','武佳汶','徐雯',
      '许可鑫','杨光','杨靖','杨喻涵','伊博乐图','尹贺临','云柯',
      '张少阳','张硕','张天睿','张霄楠','张雅絮','张伊文','张怡',
      '张艺蓝','赵滨玮','周易龙')
intro = '单击“抽取”按钮或按Enter键，以随机抽取一个姓名\n单击“退出”按钮或按Esc键，以退出此程序'

win = Tk()
win.title('Selector')
ft1 = tkf.Font(family='LXGW Bright GB',size=72,weight=tkf.BOLD)
ft2 = tkf.Font(family='LXGW Bright GB',size=32)
fti = tkf.Font(family='LXGW Bright GB',size=36,weight=tkf.BOLD)
lab = Label(win,justify='center',text=intro,font=fti)
lab.grid(row=1,column=1,columnspan=2)
bt1 = Button(win,text='抽取',font=ft2,command=sel)
bt2 = Button(win,text='退出',font=ft2,command=win.destroy)
bt1.grid(row=2,column=1)
bt2.grid(row=2,column=2)
win.bind('<Return>',sele)
win.bind('<Escape>',exite)

win.mainloop()
