'''
GitHub 项目页：
https://github.com/PumpkinJui/Selector
当前版本：
Selector 1.3.1 Public Tester
'''
# 请勿使用 -w 选项打包。

from tkinter import *
import tkinter.font as tkf
import tkinter.messagebox as msgbx
from random import choice,randint
from time import sleep
import traceback

def sel():# 更换新的显示内容
    global lt,intro
    if lab['text'] == intro:# 更换字体样式
        lab['font'] = ft1
    if mode.get() == '1':# 手动模式
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

def sele(event):# 键盘适配特制
    sel()

def exite(event):# 键盘适配特制
    win.destroy()

def flash():# 刷新选择
    manual.flash()
    auto.flash()

try:
    print('开始读取。')
    ltr = open('list.txt','r')# ANSI 编码读取
    print('成功打开文件，当前使用 ANSI 编码。')
    lt = ltr.read().splitlines()
    print('成功读取数据。')
    print(lt)
    if lt == []:# 列表为空时抛出错误
        raise
    lt = set(lt)# 去重
    print('已将列表转化为集合。')
    print(lt)
    lt = tuple(lt)# 给定 ANSI 编码 list 时采用的元组
    print('已将集合转化为元组，将进入 GUI 构建。')
    print(lt)
except RuntimeError as e:# 列表为空
    print('文件为空，将显示警告消息框。')
    print('错误代码：' + str(e))
    traceback.print_exc()
    msgbx.showwarning('读取异常','您提供的 list.txt 文件为空！')# 向用户显示警告消息框
    lt = ('0','1','2','3','4','5','6','7','8','9')# 给定空 ANSI 编码 list 时自动采用的元组
except UnicodeDecodeError as e:# 非 ANSI 编码
    try:
        print('文件不是 ANSI 编码。')
        print('错误代码：' + str(e))
        traceback.print_exc()
        ltr = open('list.txt','r',encoding='utf-8')# UTF-8 编码读取
        print('成功打开文件，当前使用 UTF-8 编码。')
        lt = ltr.read().splitlines()
        print('成功读取数据。')
        print(lt)
        if lt == []:# 列表为空时抛出错误
            raise
        lt = set(lt)# 去重
        print('已将列表转化为集合。')
        print(lt)
        lt = tuple(lt)# 给定 UTF-8 编码 list 时采用的元组
        print('已将集合转化为元组，将进入 GUI 构建。')
        print(lt)
    except RuntimeError as e:# 列表为空
        print('文件为空，将显示警告消息框。')
        print('错误代码：' + str(e))
        traceback.print_exc()
        msgbx.showwarning('读取异常','您提供的 list.txt 文件为空！')# 向用户显示警告消息框
        lt = ('0','1','2','3','4','5','6','7','8','9')# 给定空 ANSI 编码 list时自动采用的元组
    except UnicodeDecodeError as e:# 非 UTF-8 编码
        print('文件既不是 ANSI 编码又不是 UTF-8 编码，将显示警告消息框。')
        print('错误代码：' + str(e))
        traceback.print_exc()
        msgbx.showwarning('读取异常','您提供的 list.txt 文件既不是 ANSI 编码又不是 UTF-8 编码，\n程序无法读取！')
        # 上一行：向用户显示警告消息框
        lt = ('0','1','2','3','4','5','6','7','8','9')# 给定其他编码 list 时自动采用的元组
except FileNotFoundError as e:
    print('未能成功打开文件，因为文件不存在。')
    print('错误代码：' + str(e))
    traceback.print_exc()
    lt = ('0','1','2','3','4','5','6','7','8','9')# 没有给定 list 时自动采用的元组
except Exception as e:
    print('出现了未知错误。')
    print('错误代码：' + str(e))
    traceback.print_exc()
    lt = ('0','1','2','3','4','5','6','7','8','9')# 出现未知错误时自动采用的元组
finally:
    try:
        ltr.close()
        print('成功关闭文件。')
    except Exception as e:
        print('未能关闭文件，因为文件并未被打开过。')
        print('错误代码：' + str(e))
        traceback.print_exc()

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
