def f(i, j, N, s):  # 시작위치 i, j와 배열 크기 N, 누적합 s를 함수에 입력한다.
    global min_v

    if i == N-1 and j == N-1:
        if min_v > s + arr[i][j]:
            min_v = s + arr[i][j]

    elif i >= N or j >= N:
        return

    else:
        f(i, j+1, N, s+arr[i][j])
        f(i+1, j , N, s+arr[i][j])


T = int(input())
for test_case in range(1, T+1):
    # N : 배열 크기, arr : 배열의 숫자들
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_v = 999       # 최소값 저장할 변수
    f(0, 0, N, 0)   # 함수 실행

    print(f'#{test_case} {min_v}')

'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1

#1 15
#2 18
#3 33
'''