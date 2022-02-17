from pythonds import BinaryTree


def printexp(tree):
    leftC = tree.getLeftChild()
    rightC = tree.getRightChild()
    if leftC is None and rightC is None:
        sVal = str(tree.getRootVal())
    else:
        sVal = '(' + printexp(leftC) + tree.getRootVal() + printexp(rightC) + ')'
    return sVal


T = BinaryTree('*')
T.insertLeft("+")
L = T.getLeftChild()
L.insertLeft(4)
L.insertRight(5)
T.insertRight(7)
print(printexp(T))
