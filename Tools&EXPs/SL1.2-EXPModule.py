# Issue #6 的修复方法验证方案。
'''
import os
if os.path.exists('list.txt'):
    print('os 模块已找到 list.txt。')
if not os.path.exists('list.txt'):
    print('os 模块未找到 list.txt。')
print('if-else 结构验证完成。')
try:
    a = open('list.txt','r')
    a.close()
    print('list.txt 存在。')
except:
    print('list.txt 不存在。')
print('try-except 结构验证完成。')
ask = input('按下 Enter 键退出...')
'''

# Radiobutton 组件试用，已被实装。
'''
from tkinter import *

win = Tk()

def flash():
    manual.flash()
    auto.flash()

mode = StringVar()
mode.set(1)

manual = Radiobutton(win,text='手动',value=1,variable=mode,command=flash)
auto = Radiobutton(win,text='自动',value=0,variable=mode,command=flash)
manual.grid(row=1,column=1)
auto.grid(row=1,column=2)

win.mainloop()
'''
