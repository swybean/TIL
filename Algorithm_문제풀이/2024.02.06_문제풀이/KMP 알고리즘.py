def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)

## preprocessing
    # 일치한 개수 == 비교할 패턴 위치
    j = 0
    lps[0] = -1
    for i in range(1, M):
        # p[i] 이전에 일치한 개수
        lps[1] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    
    lps[M] = j

    # search
    i = 0   # 비교할 텍스트 위치
    j = 0   # 비교할 패턴 위치
    while i < N and j <= M:
        # 첫 글자가 불일치했거나, 일치하면
        if j == -1 or t[1] == p[j]:
            i += 1
            j += 1
        else:   # 불일치
            j = lps[j]
        # 패턴을 찾을 경우
        if j == M:
            # 패턴의 인덱스 출력
            print(i-M, end = ' ')
            j = lps[j]
    
t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t, p)
t = 'AABAACAADAABAABA'
p = 'AABA'
kmp(t, p)
t = 'AAAAABAAABA'
p = 'AAAA'
kmp(t, p)


'''
찾을 패턴 밑에 lps 리스트를 만들고
일치하면 1을, 불일치하면 0을 넣어둔다.
(인덱스 0번인 시작 위치는 -1)

'''
