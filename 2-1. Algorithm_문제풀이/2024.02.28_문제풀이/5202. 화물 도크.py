






T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 신청서 숫자 N
    arr = []            # 작업시간 저장할 리스트
    cnt = 1             # 최대 이용 가능한 화물차 수

    for _ in range(N):
        s, e = map(int, input().split())
        arr.append((s, e))
        arr.sort(key=lambda x:x[1]) 

    F = arr[0][1]

    for i in range(1, N):
        if arr[i][0] >= F:
            F = arr[i][1]
            cnt += 1
    
    print(f'#{test_case} {cnt}')






