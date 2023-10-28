'''
GitHub 项目页：
https://github.com/PumpkinJui/Selector
当前版本：
Selector 1.4.2 Public
'''



from tkinter import *
import tkinter.font as tkf
import tkinter.messagebox as msgbx
from pygame import mixer as m
from random import choice,randint
from time import sleep
from re import sub,match
from traceback import print_exc as exc



dointro = True
lt = []



def sel():# 更换新的显示内容
    global lt,intro
    if lab['text'] == intro:# 更换字体样式
        lab['font'] = ft1
    if mode.get() == '1':# 手动模式
        a = choice(lt)
        lab['text'] = a
        win.title('Selector - ' + a)
    if mode.get() == '2':# 自动模式
        ti = randint(5,25)
        for i in range(ti):
            a = choice(lt)# 产生
            if i != ti - 1:# 不在最后一次执行
                mus1()# 播放中间音效
                win.title('Selector - ' + a)
                sleep(0.3)# 延时
        while m.get_busy():# 给出足够时间完全播放
            pass
        win.title('Selector - ' + a)
        lab['text'] = a# 更改 Label 的显示
        mus2()# 播放最终音效


def ltprocess(ltr):
    global lt
    lt = ltr.read().splitlines()
    if lt == []:# 列表为空时抛出错误
        raise TabError
    rmblank()

    ltf = []# 去除注释并还原 “\#” 后的列表
    for i in lt:
        j = sub(r'\s*(?<!\\)#.*','',i)# 去除注释
        k = sub(r'\\#','#',j)# 还原 “\#”
        ltf.append(k)
    lt = ltf

    rmblank()
    if lt == []:# 不包含有效内容时抛出错误
        raise RuntimeError
    lt = tuple(lt)


def rmblank():
    global lt
    lt = set(lt)# 去重
    lt = list(lt)
    ltd = []# 去空白元素
    for i in lt:
        if match(r'^\s*$',i) != None:
            ltd.append(i)
    for i in ltd:
        lt.remove(i)


def sele(event):# 键盘适配特制
    sel()


def exite(event):# 键盘适配特制
    win.destroy()


def flash1():# 刷新模式选择
    manual.flash()
    auto.flash()
    if mode.get() == '1':# 手动模式
        muson['state'] = DISABLED
        musoff['state'] = DISABLED
    if mode.get() == '2' and musload():# 自动模式
        muson['state'] = NORMAL
        musoff['state'] = NORMAL


def flash2():# 刷新音乐选择
    muson.flash()
    musoff.flash()


def musload():# 判断音乐是否全部加载
    if not load1 and not load2:
        return False# 啥都没加载
    else:
        return True


def mus1():# 播放中间音效
    if muson['state'] == NORMAL and mus.get() == '1' and load1:# 自动模式，音效启用，中间音效加载
        m.music.play()


def mus2():# 播放最终音效
    sleep(0.1)
    if muson['state'] == NORMAL and mus.get() == '1' and load2:# 自动模式，音效启用，最终音效加载
        gt.play()
    elif muson['state'] == NORMAL and mus.get() == '1' and load1:# 自动模式，音效启用，中间音效加载
        for j in range(3):
            sleep(0.1)
            m.music.play()# 连续三次播放中间音效，以代替未加载的最终音效



try:
    ltr = open('list.txt','r')# ANSI 编码读取
    ltprocess(ltr)
except TabError:# 列表为空
    msgbx.showwarning('非法的文件内容','您提供的 list.txt 文件为空！')
    lt = ('0','1','2','3','4','5','6','7','8','9')
except RuntimeError:# 列表处理后为空
    msgbx.showwarning('非法的文件内容','您提供的 list.txt 文件不包含有效的抽取内容！')
    lt = ('0','1','2','3','4','5','6','7','8','9')
except UnicodeDecodeError:# 非 ANSI 编码
    try:
        ltr = open('list.txt','r',encoding='utf-8')# UTF-8 编码读取
        ltprocess(ltr)
    except TabError:# 列表为空
        msgbx.showwarning('非法的文件内容','您提供的 list.txt 文件为空！')
        lt = ('0','1','2','3','4','5','6','7','8','9')
    except RuntimeError:# 列表处理后为空
        msgbx.showwarning('非法的文件内容','您提供的 list.txt 文件不包含有效的抽取内容！')
        lt = ('0','1','2','3','4','5','6','7','8','9')
    except UnicodeDecodeError:# 非 UTF-8 编码
        msgbx.showwarning('读取异常','您提供的 list.txt 文件既不是 ANSI 编码又不是 UTF-8 编码，\n程序无法读取！')
        # 上一行：向用户显示警告消息框
        lt = ('0','1','2','3','4','5','6','7','8','9')# 给定其他编码 list 时自动采用的元组
except FileNotFoundError:
    lt = ('0','1','2','3','4','5','6','7','8','9')# 没有给定 list 时自动采用的元组
except:
    esc = open('esc.log','a')
    exc(file=esc)
    esc.write('\n在 https://github.com/PumpkinJui/Selector/issues/new 进行反馈。\n')
    esc.write('如果您无法打开该网页，也可以发邮件至 feedback@pumpkinjui.aleeas.com。\n')
    esc.write('反馈时请将此文件作为附件上传。也可以将此文件中的内容复制至反馈的文本区域。\n\n\n')
    esc.close()# 错误日志
    intro = '''出现了未知错误。
错误信息已经保存至程序目录下的“esc.log”文件中。
更多信息请自行打开该文件查看。'''
    dointro = False# 关闭原有简要使用说明的显示
    lt = ('0','1','2','3','4','5','6','7','8','9')# 出现未知错误时自动采用的元组
finally:
    try:
        ltr.close()
    except:
        pass



if dointro:
    intro = '''单击“抽取”按钮或按 Enter 键，以随机抽取一个姓名
长按上方任一键，以进行“更具有视觉效果”的随机抽取
单击“退出”按钮或按 Esc 键，以退出此程序'''# 预设简要使用说明(完整见 GitHub)

win = Tk()
win.title('Selector')# 创建窗口
win.resizable(0,0)# 锁定窗体尺寸

ft1 = tkf.Font(family='LXGW Bright GB',size=80,weight=tkf.BOLD)# 显示姓名时 Label 的字体样式
ft2 = tkf.Font(family='LXGW Bright GB',size=48)# 按钮的字体样式
ft3 = tkf.Font(family='LXGW Bright GB',size=24)# 模式选择的字体样式
ft4 = tkf.Font(family='LXGW Bright GB',size=20)# 音效开关的字体样式
fti = tkf.Font(family='LXGW Bright GB',size=36,weight=tkf.BOLD)# 显示简要使用说明时 Label 的字体样式

lab = Label(win,justify='center',text=intro,font=fti)
lab.grid(row=1,column=1,columnspan=2)# 显示文本

mode = StringVar()
mode.set(1)# 自动设置手动模式

manual = Radiobutton(win,text='手动模式',font=ft3,value=1,variable=mode,command=flash1)
auto = Radiobutton(win,text='自动模式',font=ft3,value=2,variable=mode,command=flash1)
manual.grid(row=2,column=1)
auto.grid(row=2,column=2)# 显示单选按钮

bt1 = Button(win,text='抽取',font=ft2,command=sel,repeatdelay=1000,repeatinterval=50)
bt2 = Button(win,text='退出',font=ft2,command=win.destroy)# 绑定鼠标
bt1.grid(row=4,column=1,sticky=NSEW)
bt2.grid(row=4,column=2,sticky=NSEW)# 显示按钮

win.bind('<Return>',sele)# 绑定 Enter 键
win.bind('<Escape>',exite)# 绑定 Esc 键


m.init()# 音乐初始化—自动模式专享
try:
    m.music.load('Successful_Hit.ogg')# 过程
    load1 = True
except:
    load1 = False
try:
    gt = m.Sound('Random_Levelup.ogg')# 结果
    load2 = True
except:
    load2 = False

mus = StringVar()
mus.set(1)# 自动设置音效开
if not musload():
    mus.set(2)# 啥都没加载，自动设置音效关
else:
    m.music.set_volume(0.01)# 设置音量大小为 0.01
    gt.set_volume(0.01)# 这样即使电脑主音量开到了 50 也不会很吵

muson = Radiobutton(win,text='音效开',font=ft4,value=1,variable=mus,command=flash2,state=DISABLED)
musoff = Radiobutton(win,text='音效关',font=ft4,value=2,variable=mus,command=flash2,state=DISABLED)
muson.grid(row=3,column=1)
musoff.grid(row=3,column=2)# 显示单选按钮


win.mainloop()
