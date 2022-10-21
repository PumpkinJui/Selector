# Issue #6 的修复方法验证方案。
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
