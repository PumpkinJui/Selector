'''
GitHub 项目页：
https://github.com/PumpkinJui/Selector
当前版本：
Selector 1.2.x
'''

from tkinter import *
import tkinter.font as tkf
from random import choice,randint
from time import sleep

def sel():# 更换新的显示内容
    global lt,intro
    if lab['text'] == intro:# 更换字体样式
        lab['font'] = ft1
    if mode.get() == '1':# 手动模式
        x = randint(0,2)
        if x == 1:
            lab['text'] = '亢敏'
            win.title('Selector - 亢敏')
        elif x == 2:
            lab['text'] = '张少阳'
            win.title('Selector - 张少阳')
        else:
            a = choice(lt)
            lab['text'] = a
            win.title('Selector - ' + a)
    if mode.get() == '2':# 自动模式
        ti = randint(5,50)
        for i in range(ti):
            a = choice(lt)
            lab['text'] = a
            win.title('Selector - ' + a)
            sleep(0.1)
        x = randint(0,2)
        if x == 1:
            lab['text'] = '亢敏'
            win.title('Selector - 亢敏')
        elif x == 2:
            lab['text'] = '张少阳'
            win.title('Selector - 张少阳')

def sele(event):# 键盘适配特制
    sel()

def exite(event):# 键盘适配特制
    win.destroy()

def flash():# 刷新选择
    manual.flash()
    auto.flash()

lt = ('阿希达','安悦然','白沛林','白书嘉','董子萱','冯耀江','高洪泽',
      '高昕毓','宫宁','贵昊','郭倩','胡景皓','胡妤佳','季国婧',
      '贾晨','贾涵凝','贾晓雪','亢敏','孔令茹','郎佳伟','李璨',
      '李嘉仪','李静雯','李铠诺','李沛哲','李瑞鑫','李政辉','李智',
      '刘家慧','刘恺','刘芮','刘欣','鲁禹志','吕浩玚','石佳琪',
      '孙承楷','田岩松','佟雅茹','王悦','魏宁','武佳汶','徐雯',
      '许可鑫','杨光','杨靖','杨喻涵','伊博乐图','尹贺临','云柯',
      '张少阳','张硕','张天睿','张霄楠','张雅絮','张伊文','张怡',
      '张艺蓝','赵滨玮','周易龙')# 预设姓名元组(本班专享)

intro = '''单击“抽取”按钮或按 Enter 键，以随机抽取一个姓名
长按上方任一键，以进行“更具有视觉效果”的随机抽取
单击“退出”按钮或按 Esc 键，以退出此程序'''# 预设简要使用说明(完整见 GitHub)

win = Tk()
win.title('Selector')# 创建窗口
win.resizable(0,0)# 锁定窗体尺寸

ft1 = tkf.Font(family='LXGW Bright GB',size=80,weight=tkf.BOLD)# 显示姓名时 Label 的字体样式
ft2 = tkf.Font(family='LXGW Bright GB',size=48)# 按钮的字体样式
ft3 = tkf.Font(family='LXGW Bright GB',size=24)# 单选按钮的字体样式
fti = tkf.Font(family='LXGW Bright GB',size=36,weight=tkf.BOLD)# 显示简要使用说明时 Label 的字体样式

lab = Label(win,justify='center',text=intro,font=fti)
lab.grid(row=1,column=1,columnspan=2)# 显示文本

mode = StringVar()
mode.set(1)# 自动设置手动模式

manual = Radiobutton(win,text='手动模式',font=ft3,value=1,variable=mode,command=flash)
auto = Radiobutton(win,text='自动模式',font=ft3,value=2,variable=mode,command=flash)
manual.grid(row=2,column=1)
auto.grid(row=2,column=2)# 显示单选按钮

bt1 = Button(win,text='抽取',font=ft2,command=sel,repeatdelay=1000,repeatinterval=50)
bt2 = Button(win,text='退出',font=ft2,command=win.destroy)# 绑定鼠标
bt1.grid(row=3,column=1,sticky=NSEW)
bt2.grid(row=3,column=2,sticky=NSEW)# 显示按钮

win.bind('<Return>',sele)# 绑定 Enter 键
win.bind('<Escape>',exite)# 绑定 Esc 键

win.mainloop()
