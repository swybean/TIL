

T = int(input())
for test_case in range(1, T+1):
    arr = input().split()   
    stack = [] 

    for token in arr:
        if token.isdigit():
            stack.append(int(token))    
        
        if token == '+' or token == '-' or token == '*' or token == '/':
            if len(stack) < 2:
                print(f'#{test_case} error')
                break
            else:
                if token == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b + a)    
                if token == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                if token == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b * a)
                if token == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))  
                     
        if token == '.':
            if len(stack) == 1: 
                print(f'#{test_case} {stack.pop()}') 
            else:
                print(f'#{test_case} error')    
                
        





