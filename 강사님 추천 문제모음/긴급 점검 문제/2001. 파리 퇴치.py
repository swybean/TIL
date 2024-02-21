T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())   # N은 배열 크기, M은 파리채 크기
    arr = [list(map(int, input().split())) for _ in range(N)]   # 배열 입력하기
    max_v = 0   # 최대 파리값 저장할 변수 설정

    for i in range(N - M + 1):      # i행과 j열 순회하기
        for j in range(N - M + 1):  # N-M+1은 MM칸의 왼쪽 위 인덱스까지만 가기 위한 범위
            s = 0                   # 현재 MM칸에서 퇴치한 파리수를 저장할 변수
            for p in range(M):              # MM칸 내에서 i행이 내려갈 범위 설정
                for q in range(M):          # MM칸 내에서 j열이 오른쪽으로 갈 범위 설정
                    s += arr[i + p][j + q]    # 변수s에 MM칸 내 파리수를 합치기
            if max_v < s:           # 만약 max_v가 s보다 작으면
                max_v = s           # s를 max_v로 바꾸기
    
    print(f'#{test_case} {max_v}')  # 프린트하기

'''
내 결과
#1   49
#2  159
#3  426
#4  557
#5  479
#6  918
#7  139
#8  904
#9  205 
#10 1198
'''
'''
나와야 하는 결과
#1 49
#2 159
#3 428
#4 620
#5 479
#6 941
#7 171
#8 968
#9 209
#10 1242
'''