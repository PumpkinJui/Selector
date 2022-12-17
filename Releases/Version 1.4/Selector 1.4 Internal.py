'''
GitHub 项目页：
https://github.com/PumpkinJui/Selector
当前版本：
Selector 1.4 Internal
'''

from tkinter import *
import tkinter.font as tkf
from pygame import mixer as m
from random import choice,randint
from time import sleep

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
    m.music.load('Successful_Hit.wav')# 过程
    load1 = True
except:
    load1 = False
try:
    gt = m.Sound('Random_levelup.wav')# 结果
    load2 = True
except:
    load2 = False

mus = StringVar()
mus.set(1)# 自动设置音效开
if not musload():
    mus.set(2)# 啥都没加载，自动设置音效关

muson = Radiobutton(win,text='音效开',font=ft4,value=1,variable=mus,command=flash2,state=DISABLED)
musoff = Radiobutton(win,text='音效关',font=ft4,value=2,variable=mus,command=flash2,state=DISABLED)
muson.grid(row=3,column=1)
musoff.grid(row=3,column=2)# 显示单选按钮

win.mainloop()
