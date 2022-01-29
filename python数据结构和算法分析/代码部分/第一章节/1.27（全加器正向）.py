"""
如果想正向实现全加器
那么就直接考虑，在类初始化的时候
直接就构建值，并且在构建过程中，直接实现Connector类的作用
下面是重构代码:
"""
class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None
        if n == -1:
            self.output = 0

    def getLabel(self):
        return self.label

    def getOutput(self):
        if self.output != None:
            return self.output
        else:
            self.output = self.performGateLogic()
            return self.output


class BinaryGate(LogicGate):
    def __init__(self, n,a,b):
        super().__init__(n)
        self.pinA = a
        self.pinB = b

    def getPinA(self):
        return self.pinA

    def getPinB(self):
        return self.pinB

class AndGate(BinaryGate):
    def __init__(self, n,a,b):
        super().__init__(n,a,b)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return a & b


class XorGate(BinaryGate):
    def __init__(self, n,a,b):
        super().__init__(n,a,b)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return a ^ b


print("这个是八位全加器的类实现功能，请确保你输入的值在（0-255）之间")
R1 = int(input("请输入第一个数:"))
R2 = int(input("请输入第二个数:"))
s1 = [0] * 8
s2 = [0] * 8
pos = 0
mp = []  # 表示电路图中的门的值
ls = []  # 表示电路图中的连线
while R1:
    s1[pos] = R1 % 2
    R1 = R1 // 2
    pos += 1
pos = 0
while R2:
    s2[pos] = R2 % 2
    R2 = R2 // 2
    pos += 1
for i in range(8):
    for j in range(5):
        label = i * 5 + j
        if j==0:
            mp.append(XorGate(label,s1[i],s2[i]).getOutput())
        elif j == 3:
            mp.append(AndGate(label,s1[i],s2[i]).getOutput())
        elif j == 1:
            if i==0:
                mp.append(XorGate(label,mp[0],0).getOutput())
            else:
                mp.append(XorGate(label,mp[i*5],mp[i*5-1]).getOutput())
        elif j == 2:
            if i==0:
                mp.append(AndGate(label,mp[0],0).getOutput())
            else:
                mp.append(AndGate(label,mp[i*5],mp[i*5-1]).getOutput())
        else:
            mp.append(XorGate(label,mp[i*5+2],mp[i*5+3]).getOutput())


ans = []
for i in range(8):
    ans.append(mp[i * 5 + 1])
ans.append(mp[7 * 5 + 4])
tot = 0
for i in range(9):
    tot += (2 ** i) * ans[i]
print(tot)