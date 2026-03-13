def priority(ch):
    if ch == "^":
        return 3
    elif ch == '*' or ch == "/":
        return 2
    elif ch == '+' or ch == '-':
        return 1
    return -1

def checkOperand(ch):
    return ch.isalnum()

def infixToPostfix(exp):
    stack = []
    result = ""

    for ch in exp:
        if checkOperand(ch):
            result += ch
        
        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
            
        else:
            while stack and priority(ch) <= priority(stack[-1]):
                result += stack.pop()
            stack.append(ch)
    
    while stack:
        result += stack.pop()
    
    return result

expression = "a+b*(c^d-e)"
ans = infixToPostfix(expression)
print("ANS ->", ans)