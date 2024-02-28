
T = int(input())
for test_case in range(1, T+1):
    S = list(input())
    ball = 0    # 공의 개수
    
    for i in range(len(S)-1):
        if S[i] == '(':
            if S[i+1] == '|':
                ball += 1 
            elif S[i+1] == ')':
                ball += 1
        elif S[i] == '|':
            if S[i+1] == ')':
                ball += 1 

    print(f'#{test_case} {ball}')

