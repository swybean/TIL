op = {')':'(', '}':'{'}   

T = int(input())
for tc in range(1, T+1):
    arr = input()
    result = 1
    stack = []

    for i in arr:
        if i in '{(':
            stack.append((i))
        elif i in '})':
            if not stack:
                result = 0
                break
            else:
                j = stack.pop()
                if j != op[i]:
                    result = 0
                    break
    else:
        if stack:
            result =0

    print(f'#{tc} {result}')       
        


