def prefix_postfix(prefix):
    prefix = prefix.split()
    index = 0
    operlist = []
    operandlist = []
    postfixlist = []
    for token in prefix:
        if token in "+-":
            operlist.append(token)
            if prefix[index + 1].isdigit() and prefix[index + 2].isdigit(): 
                postfixlist.append(prefix[index + 1])
                postfixlist.append(prefix[index + 2])
                postfixlist.append(token)
                
            """    
            elif prefix[index + 1].isdigit() and not prefix[index + 2].isdigit():
            """
                
            
            
        index = index + 1
        
    return postfixlist