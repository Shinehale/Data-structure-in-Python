"""
NotImplemented 代表的意思是，这样的情况还没有实现，但是不代表是一种typeerror，可以等待别方法迂回实现
bool（NotImplemented） 将得到True
说明本身是一个常量

下面说明__radd__方法的原理：
举例子：
执行    a + b
若 a.__add__(b)方法没有定义 则 执行 b.__radd__(a)
若 a.__add__(b) 返回的是NotImplemented，则执行b.__radd__(a)
若执行到b,__radd__(b) 得到的还是NotImplemented，那么将返回Typeerror
否则输出上述计算的值
实例如下：
"""
class A:
    def __init__(self,value):
        self.value=value
    def __add__(self, other):
        if isinstance(other,A):
            print("this is comparing A\n")
        elif isinstance(other,B):
            print("this is comparing B\n")
        else:
            return NotImplemented

class B:
    def __init__(self,value):
        self.value=value
    def __radd__(self, other):
        print("this is using __radd__ method of class B")

class C:
    def __init__(self,value):
        self.value=value
    def __radd__(self,other):
        print("this is using __radd__ method of class C")
a=A(0)
b=B(0)
a+b
# >>this is comparing B

c=C(0)
b+c
# >>this is using __radd__ method of class C