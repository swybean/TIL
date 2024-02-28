
T = int(input())

for test_case in range(1, T+1):
    N, D = map(int, input().split())    # N은 꽃밭 길이, D는 분무기 범위값

    arr = [1] * N   # 1로 가득찬 꽃밭 리스트 생성
    water = 0
    
    if 1 in arr:
        for i in range(D, N):
            for p in range(1, D+1):                       
                if 0 <= D-1-p < N and 0 <= D-1+p < N:      
                    if arr[i-1-p] == arr[i-1+p]:  
                        arr[i-1-p] = 0
                        arr[i-1+p] = 0
                        water += 1

    print(f'#{test_case} {water}')




'''


'''
