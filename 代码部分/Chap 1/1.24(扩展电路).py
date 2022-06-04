import sys


class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output=self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA==None:
            return int(input("Enter Pin A input for gate" + \
                         self.getLabel() + "->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB==None:
            return int(input("Enter Pin B input for gate" + \
                             self.getLabel() + "->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA==None:
            self.pinA=source
        elif self.pinB==None:
            self.pinB=source
        else:
            raise RuntimeError("Error:NO EMPTY PINS")

class UnaryGate(LogicGate):
    def __init__(self,n):
        super().__init__(n)
        self.pin=None

    def getPin(self):
        return int(input("Enter Pin input for gate" + \
                         self.getLabel() + "->"))


class AndGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)

    def performGateLogic(self):
        a=self.getPinA()
        b=self.getPinB()
        return a&b

class OrGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)

    def performGateLogic(self):
        a=self.getPinA()
        b=self.getPinB()
        return a|b


class NotGate(UnaryGate):
    def __init__(self,n):
        super().__init__(n)

    def performGateLogic(self):
        a=self.getPin()
        if a==1:return 0
        else:return 1

class XorGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)

    def performGateLogic(self):
        a=self.getPinA()
        b=self.getPinB()
        return a^b


class Connector:
    def __init__(self,fgate,tgate):
        self.fromgate=fgate
        self.togate=tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
