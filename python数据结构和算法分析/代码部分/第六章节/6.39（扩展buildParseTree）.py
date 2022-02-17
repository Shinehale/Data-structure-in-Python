import operator

from pythonds import Stack
from pythonds import BinaryTree


def solve(Lis, exp):
    value = 0
    used = False
    for item in exp:
        if item not in "(+-*/) ":
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
        else:
            raise ValueError("Unknown Operator : " + item)
    return eTree


def evaluate(parseTree):
    Operators = {'+': operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    if leftC and rightC:
        fn = Operators[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()


S = input()
ans = evaluate(buildParseTree(S))
print(ans)
# (3+(45*5))
# (((4    * 8) / 6) - 3)
# >> 2.333
