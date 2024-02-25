T = int(input())
for tc in range(1, T+1):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))

    best = 0    # 가장 많은 글자의 수
    for i in str1:  # str1에서 문자 i를 반복순회
        now = 0     # 현재 문자 i가 str2에 얼마나 있는지 저장할 변수
        for j in str2:  # st2에서 문자 j를 반복순회
            if i == j:  # 만약 i와 j가 같은 문자라면
                now += 1    # now 1증가
                if best < now:  # 만약 now가 best보다 더 크면 best를 now값으로 변경
                    best = now
    
    print(f'#{tc} {best}')


