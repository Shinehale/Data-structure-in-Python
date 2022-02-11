from pythonds.basic import Deque


def palchecker(aString):
    deq = Deque()

    for ch in aString:
        if ch != " ":
            deq.addRear(ch)

    flag = True
    while deq.size() > 1 and flag:
        first = deq.removeFront()
        last = deq.removeRear()
        if first != last:
            flag = False

    return flag


S = input("请输入你想要判断的字符串:\n")
if palchecker(S):
    print("输入的字符串是回文串!")
else:
    print("输入的字符串不是回文串!")
