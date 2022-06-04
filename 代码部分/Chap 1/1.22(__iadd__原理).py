"""
+=运算在使用过程中，如果没有定义__iadd__()方法
那么将直接error
但是如果返回值是NotImplemented
那么将调用__add__()方法
并且开始上1.21的顺序开始运行
"""

class A:
    def __init__(self,value):
        self.value=value
    def __iadd__(self, other):
        if isinstance(other,B):
            print("this is calling __iadd__ method!\n")
            newvalue=self.value+other.value
            return A(newvalue)
        else:
            return NotImplemented
    def __add__(self, other):
        print("This is calling __add__ method\n")
class B:
    def __init__(self,value):
        self.value=value
    def __add__(self, other):
        print("this is calling __add__ method of B")

class C:
    def __init__(self,value):
        self.value=value
    def __radd__(self, other):
        print("this is calling __radd__ method of C")

a1,a2=A(0),A(0)
b=B(0)
a1+=b
# >>This is calling __add__ method
c=C(0)
a1+=c
# >> This is calling __add__ method
b+=c
# >> this is calling __add__ method of B