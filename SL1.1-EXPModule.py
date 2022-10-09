#EXP-1，从文件中读取名称列表并去重。
#被实际应用到 Public 版本。
'''
import random as r
ltr = open('list.txt','r')
lt = ltr.read().splitlines()
ltr.close()
print(lt)
lt = set(lt)
print(lt)
lt = tuple(lt)
print(lt)
print(r.choice(lt))
'''

#EXP-2，将列表中的所有元素转为 str 类型。
#后来证明从文件读出来的默认就是 str 类型，不需要。
'''
lto = [0,1,2,3,4,5,6,7,8,9,'10']
lt = []
for i in lto:
    if not isinstance(i,str):
        lt.append(str(i))
    else:
        lt.append(i)
print(lto)
print(lt)
'''
