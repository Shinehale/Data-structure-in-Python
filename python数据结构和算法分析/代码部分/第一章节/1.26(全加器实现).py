class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate" + \
                             self.getLabel() + "->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate" + \
                             self.getLabel() + "->"))
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


print("这个是八位全加器的类实现功能，请确保你输入的值在（0-255）之间")
R1=int(input("请输入第一个数:"))
R2=int(input("请输入第二个数:"))
s1=[0]*8
s2=[0]*8
pos=0
while (R1):
    s1[pos]=R1%2
    R1=R1//2
    pos+=1
pos=0
while (R2):
    s2[pos]=R2%2
    R2=R2//2
    pos+=1