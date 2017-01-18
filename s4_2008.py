#3.27 Programming exercise #1
from pythonds.basic.stack import Stack

def infix_postfix(equation):
    prior = {}
    #setting priority of operators
    prior["("] = 1
    prior["+"] = 2
    prior["-"] = 2
    prior["*"] = 3
    prior["/"] = 3
    prior["%"] = 3
    prior["^"] = 4
    #parenthesis stack
    par = Stack()
    moredigit = ""
    postfixList = []
    index = 0
    for l in equation:
        if l == " ":
            pass

        elif l in "0123456789":
            while index < len(equation) - 1:
                if equation[index +1].isdigit() and index < len(equation):
                    moredigit = moredigit + l
                    break

                elif len(moredigit) > 0:
                    moredigit = moredigit + l
                    postfixList.append(moredigit)
                    moredigit = ""
                    break

                else:
                    #for one digit number
                    postfixList.append(l)    
                    break
                
            if index == len(equation) - 1:
                if len(moredigit) > 0:
                    #for when this is the last digit of the equation but this number has multiple digits
                    moredigit = moredigit + l
                    postfixList.append(moredigit)
                    moredigit = ""

                else:
                    postfixList.append(l)
            
        elif l.upper() in "ABCDEFGHIJKLNMOPQRSTUVWXYZ":
            #this also can only take 1 character 
            postfixList.append(l)

        elif l == "(":
            par.push(l)

        elif l == ")":
            topstack = par.pop()
            while topstack != "(":
                postfixList.append(topstack)
                topstack = par.pop()

        else:
            while (not par.isEmpty()) and prior[par.peek()] >= prior[l]:
                postfixList.append(par.pop())

            par.push(l)

        index = index + 1
        
    while not par.isEmpty():
        postfixList.append(par.pop())

    return " ".join(postfixList)


def postfixCal(postfixequa):
    postfixequa = postfixequa.split()
    operandStack = Stack()

    for token in postfixequa:
        if token.isdigit():
            operandStack.push(token)

        else:
            operand2 = int(operandStack.pop())
            operand1 = int(operandStack.pop())
            if token == '+':
                operandStack.push(operand1 + operand2)

            elif token == '-':
                operandStack.push(operand1 - operand2)

            elif token == '*':
                operandStack.push(operand1 * operand2)

            elif token == '/':
                #should return integer to the stack 
                operandStack.push(operand1 // operand2)

            elif token == '%':
                operandStack.push(operand1 % operand2)

            elif token == '^':
                operandStack.push(operand1 ** operand2)


    return operandStack.pop()    
                
    
def calculator(infixequa):
    return postfixCal(infix_postfix(infixequa))

for i in range(int(input())):
  lst = []
  for i in range(4):
    lst.append(int(input()))
  
  a = lst[0]
  b = lst[1]
  c = lst[2]
  d = lst[3]
  
  operlist = ['+', '-', '*', '/']
  string = ""
  numlist = []
  for i in range(4):
    for j in range(4):
      for k in range(4):
        string = str(a)+operlist[i]+str(b)+operlist[j]+str(c)+operlist[k]+str(d)
        value = calculator(string)
        
        if isinstance(value, int):
          if value <= 24:  
            numlist.append(value)
        
        
  print(max(numlist)) 
  
