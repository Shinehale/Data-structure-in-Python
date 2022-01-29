"""
在实践中发现__str__()和__repr__()有着很大的关系

__repr__方法的作用是打印类的详细信息的
具体可参照实例

二者实现的顺序：
在子类中使用_ _str_ _,先找子类的_ _str_ _
没有的话要向上找,只要父类不是object,就执行父类的_ _str_ _
但是如果除了object之外的父类都没有_ _str_ _方法
就执行子类的_ _repr_ _方法
如果子类也没有,
还要向上继续找父类中的_ _repr_ _方法.
一直找不到 再执行object类中的_ _str_ _方法
"""


class card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        print("have called the __repr__ method already!")
        return "face:" + str(self.face) + " suit:" + str(self.suit)


Card1 = card(12, 3)
print(Card1)
# >> have called the __repr__ method already!
# >> face:12 suit:3
