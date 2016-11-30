def prefix_postfix(prefix):
    prefix = prefix.split()
    index = 0
    operlist = []
    operandlist = []
    postfixlist = []
    for i in range(len(prefix)):
        token = prefix[i]
        if token in "+-":
            operlist.append(token)
            if len(operandlist) == 1:
                postfixlist.append(operandlist.pop())
        
        else:
            if len(operandlist) == 2:
                postfixlist.append(operandlist.pop(0))
                postfixlist.append(operandlist.pop(0))
                postfixlist.append(operlist.pop())
                
            operandlist.append(token)
            
    if len(operandlist) == 1:
        postfixlist.append(operlist.pop())
        postfixlist.append(operandlist.pop())
    
    for i in operlist:
        postfixlist.append(i)
        
    return " ".join(postfixlist)