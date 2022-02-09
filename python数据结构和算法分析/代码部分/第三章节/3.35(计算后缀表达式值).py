from pythonds.basic import Stack as St


def postfixEval(postfixExpr):
    ope = St()

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


exp = input()
ans = postfixEval(exp)
print(ans)
