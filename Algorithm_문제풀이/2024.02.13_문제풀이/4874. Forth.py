

T = int(input())
for test_case in range(1, T+1):
    arr = input().split()   # 연산코드 입력하기
    stack = []  # 빈 스택 만들기

    # token을 arr에서 반복해서 돌려보자
    for token in arr:
        # 만약 token이 숫자라면
        if token.isdigit():
            stack.append(int(token))    # 스택에 추가해
        
        # token이 + - * / 중 하나라면
        if token == '+' or token == '-' or token == '*' or token == '/':
            # 근데 또 stack의 길이가 2 미만이면
            if len(stack) < 2:
                print(f'#{test_case} error') # error를 출력해
                break   # error 출력했으면 이제 밑에 if문은 하지말고 멈춰
            # 근데 stack의 길이가 2 이상이면
            else:
                # 숫자 2개를 꺼내서 +면 더하고, -면 빼고, *면 곱하고, /면 나눠
                # 그리고 계산한 결과를 다시 stack에 추가해
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
                    stack.append(int(b / a))   # 나누기는 소수점 안나오게 int로 써야 한다.
        # 만약 token이 . 이면
        if token == '.':
            # 근데 stack의 길이가 1이면?
            if len(stack) == 1: 
                print(f'#{test_case} {stack.pop()}')    # stack에 있는 그 숫자를 꺼내서 출력해
            # 근데 stack의 길이가 1이 아니라면? 계산할 수 없는 연산코드니까
            else:
                print(f'#{test_case} error')    # error를 출력해라
                
        





