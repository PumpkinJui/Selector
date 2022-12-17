# pygame 播放音效试用，已实装。
'''
from pygame import mixer as m
from tkinter import *

def sh():
    m.music.play()

def rl():
    got.play()

m.init()
m.music.load('Successful_Hit.wav')
got = m.Sound('Random_levelup.wav')

win = Tk()
win.title('SL1.4-EXPModule')
bt1 = Button(win,text='Successful_Hit',command=sh)
bt1.pack()
bt2 = Button(win,text='Random_levelup',command=rl)
bt2.pack()

win.mainloop()
