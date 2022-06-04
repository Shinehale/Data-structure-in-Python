"""
在使用Stack库的时候应该注意需要
安装pythonds库才能使用和导入
"""
import string

from pythonds.basic import Stack


def infixToPostfix(infixexpr):
    prec = {}
    prec['*'] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixList = []
    tokenList = []

    for i in range(len(infixexpr)):
        tokenList.append(infixexpr[i])

    try:
        for token in tokenList:
            if token in string.ascii_uppercase:
                postfixList.append(token)
            elif token == "(":
                opStack.push(token)
            elif token == ")":
                topToken = opStack.pop()
                while topToken != "(":
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and \
                        (prec[opStack.peek()] >= prec[token]):
                    postfixList.append((opStack.pop()))
                opStack.push(token)

        while not opStack.isEmpty():
            postfixList.append(opStack.pop())

        return "".join(postfixList)

    except:
        return "".join("the expression is something wrong!")


ans = infixToPostfix("A*B*C*D+E+F")
print(ans)
