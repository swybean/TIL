T = int(input())
for tc in range(1, T+1):
    str1 = input()  
    str2 = input()

    if str1 in str2:    # str1이 str2안에 있으면
        result = 1      # result을 1로 설정
    else:               # 없으면 result는 0으로 설정
        result = 0

    print(f'#{tc} {result}')
