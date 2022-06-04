"""
本代码将支持逻辑运算符的计算
! 来表示 not
example: ! 1 == not 1
& 表示and
^ 表示xor
| 表示or
"""
import operator

from pythonds import Stack
from pythonds import BinaryTree


def solve(Lis, exp):
    value = 0
    used = False
    for item in exp:
        if item not in "(+-*/) &|^!":
            used = True
            value = value * 10 + int(item)
        else:
            if used:
                Lis.append(value)
            used = False
            value = 0
            if item == " ":
                continue
            else:
                Lis.append(item)
    pos = 0
    while pos < len(Lis) - 1:
        if Lis[pos] == '!':
            Lis[pos], Lis[pos + 1] = Lis[pos + 1], Lis[pos]
            pos += 1
        pos += 1


def buildParseTree(fpExp):
    fplist = []
    solve(fplist, fpExp)
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for item in fplist:
        if item == "(":
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif item == '!':
            currentTree.setRootVal(item)
        elif isinstance(item, int):
            currentTree.setRootVal(item)
            parent = pStack.pop()
            currentTree = parent
        elif isinstance(item, str) and item in '+-*/':
            currentTree.setRootVal(item)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif item == ')':
            currentTree = pStack.pop()
        elif isinstance(item, str) and item in "&^|":
            currentTree.setRootVal(item)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        else:
            raise ValueError("Unknown Operator : " + item)
    return eTree


def evaluate(parseTree):
    Operators = {'+': operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, \
                 '^': operator.xor, '&': operator.and_, '|': operator.or_, '!': operator.not_ \
                 }
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    if leftC and rightC:
        fn = Operators[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    elif parseTree.getRootVal() == '!':
        if evaluate(leftC) != 0:
            return 0
        else:
            return 1
    else:
        return parseTree.getRootVal()


S = input()
ans = evaluate(buildParseTree(S))
print(ans)
# (((((3+4)*5)&7)^10)^((!7)+8))
# >> 1
