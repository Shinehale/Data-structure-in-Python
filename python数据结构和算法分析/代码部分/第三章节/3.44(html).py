"""
本程序使用sys获取命令行参数进行执行
python 3.44(html).py html.txt
进入对应目录，执行上述命令行参数即可
"""
import sys
from pythonds.basic import Stack
import re

m1 = r"</([a-z]+)>"
m2 = r"<([a-z]+)>"
file = open(sys.argv[1], "r+")
R = file.readlines()
file.close()
S = Stack()
flag = True
for item in R:
    if item[0] != '<':
        continue
    if item[1] != '/':
        op = re.findall(m2, item)
        if len(op) == 0:
            continue
        S.push(op[0])
    else:
        op = re.findall(m1, item)
        now = S.pop()
        if now != op[0]:
            flag = False
            break
        else:
            continue
if flag:
    print("this html txt is logical!")
else:
    print("this html txt has something wrong!")
