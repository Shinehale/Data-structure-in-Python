"""
the program can not solve the number beyond or equal 10
"""

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
            if token in "0123456789":
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
        return "".join("the expression has something wrong!")


def postfixEval(postfixExpr):
    ope = Stack()

    tokenList = []
    for i in range(len(postfixExpr)):
        tokenList.append(postfixExpr[i])
    try:
        for token in tokenList:
            if token in "0123456789":
                ope.push(int(token))
            else:
                operand2 = ope.pop()
                operand1 = ope.pop()
                result = doMath(token, operand1, operand2)
                ope.push(result)
        return ope.pop()
    except:
        return "".join("the expression you input has something wrong!!")


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


exp = input("Please input the expressions you want to calculate:\n")
solA = infixToPostfix(exp)
if solA[0] == "t":
    print(solA)
else:
    ans = postfixEval(solA)
    print(ans)