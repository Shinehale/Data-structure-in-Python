from pythonds import Stack


class SStack(Stack):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        ans = []
        s = ""
        while self.size():
            ans.append(self.pop())
        for key in ans:
            s += str(key) + " "
        ans.reverse()
        for key in ans:
            self.push(key)
        if s == '':
            return "empty"
        else:
            return s

    def getname(self):
        return self.name


def moveDisk(fp, tp):
    print("moving disk from %s to %s" % (fp.getname(), tp.getname()))
    tar = fp.pop()
    tp.push(tar)


def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        print("the details of two Stack is: ", end="")
        print("%s    %s     %s" % (S1, S2, S3))
        moveTower(height - 1, withPole, toPole, fromPole)


N = int(input("请输入你想要计算的汉诺塔:\n"))
S1, S2, S3 = SStack("S1"), SStack("S2"), SStack("S3")
for i in range(N, 0, -1):
    if i == 0:
        continue
    else:
        S1.push(i)
moveTower(N, S1, S3, S2)
