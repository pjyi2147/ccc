def complete(exprlist):
    operand = 0
    operator = 0
    for i in exprlist:
        if i in "+-":
            operator += 1

        else:
            operand += 1

    return operand - 1 == operator


def prefix_postfix(prefix):
    prefix = prefix.split()
    index = 0
    operlist = []
    operandlist = []
    postfixlist = []
    while len(prefix) > 0:
        token = prefix.pop(0)
        if token in "+-":                   #when token is operator
            operlist.append(token)
            if len(operandlist) == 1:
                postfixlist.append(operandlist.pop())
            
            if prefix[0].isdigit() and prefix[1].isdigit():
                postfixlist.append(prefix.pop(0))
                postfixlist.append(prefix.pop(0))
                postfixlist.append(operlist.pop())              

        else:                               #when token is operand
            operandlist.append(token)
            
            if len(postfixlist) > 0:
                if complete(postfixlist):
                    postfixlist.append(operandlist.pop())

                elif not complete(postfixlist):
                    postfixlist.append(operlist.pop())
                    postfixlist.append(operandlist.pop())

    if len(operandlist) != 0 and len(operlist) != 0:
        if complete(postfixlist):
            for i in range(operandlist):
                postfixlist.append(operandlist.pop())
                postfixlist.append(operlist.pop())
                
            
    if len(operandlist) == 0 and len(operlist) != 0:
        for i in range(len(operlist)):
            postfixlist.append(operlist.pop())

        
    return " ".join(postfixlist)
    
print(prefix_postfix("+ - 5 + 4 3 2"))

print(prefix_postfix("+ - + 3 2 1 2"))
