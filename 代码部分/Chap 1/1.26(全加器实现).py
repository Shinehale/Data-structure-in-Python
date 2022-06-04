"""
大致实现思想就是：
只需要输入两个数，那么本程序将自动实现这样的全加器
并且直接输出最终的答案
并不会展示电路的组成，像一个黑盒
设Ai,Bi为值，Ci为进位值,Si为最终答案位
C[i]=(A[i]&B[i])^(C[i-1]&(A[i]^B[i]))
S[i]=A[i]^B[i]^C[i-1]
由上述式子可以看出一个全家器
至少要使用两个AndGate和三个XorGate
那么在一个全加器单元中
0、3进行直接读取值，剩下的接口都需要连接类
并且0、1、4号认为是异或门，2、3号认为是and门
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

    def __repr__(self):
        return str(self.label)


class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        label = self.getLabel()
        if self.pinA == None:
            return s1[label // 5]
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        label = self.getLabel()
        if self.pinB == None:
            return s2[label // 5]
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("Error:NO EMPTY PINS")


class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return a & b


class XorGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return a ^ b


class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

    def __repr__(self):
        return str(self.fromgate.getLabel()) + "  " + str(self.togate.getLabel())


print("这个是八位全加器的类实现功能，请确保你输入的值在（0-255）之间")
R1 = int(input("请输入第一个数:"))
R2 = int(input("请输入第二个数:"))
s1 = [0] * 8
s2 = [0] * 8
pos = 0
mp = []  # 表示电路图中的门
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
        if j == 2 or j == 3:
            mp.append(AndGate(label))
        else:
            mp.append(XorGate(label))
Ori = XorGate(-1)
for i in range(8):
    ls.append(Connector(mp[i * 5], mp[i * 5 + 1]))
    ls.append(Connector(mp[i * 5], mp[i * 5 + 2]))
    ls.append(Connector(mp[i * 5 + 2], mp[i * 5 + 4]))
    ls.append(Connector(mp[i * 5 + 3], mp[i * 5 + 4]))
    if i == 0:
        ls.append(Connector(Ori, mp[i * 5 + 1]))
        ls.append(Connector(Ori, mp[i * 5 + 2]))
        continue
    ls.append(Connector(mp[i * 5 - 1], mp[i * 5 + 1]))
    ls.append(Connector(mp[i * 5 - 1], mp[i * 5 + 2]))

ans = []
for i in range(8):
    ans.append(mp[i * 5 + 1].getOutput())
ans.append(mp[7 * 5 + 4].getOutput())
tot = 0
for i in range(9):
    tot += (2 ** i) * ans[i]
print(tot)
# 上述过程是基于反向操作得到的
# 但是使用了记忆化递归，速度和正向操作得到的相同
