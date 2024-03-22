
T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 문제에서 N = 10으로 고정이긴함
    arr = [list(map(int, input().split())) for _ in range(N)]
    pig = 0     # 경보기에 감지되는 멧돼지 수를 저장할 변수, 0으로 초기화
    
    # 전체 arr 2차원배열 탐색하기
    for i in range(N):
        for j in range(N):

            # 1번: 처음 만나는 1은 밭의 가장 왼쪽 위 모서리야.
            if arr[i][j] == 1:
                # 왼쪽 위 모서리 경보기 범위를 탐색하면서 멧돼지(2)가 있으면 pig 수에 1 추가해
                for p in range(1, N):  
                    for di, dj in [[-1, 0], [0, -1]]:   # 왼쪽 위 모서리부터 왼쪽, 위쪽으로만 탐색하자
                        ni = i + (di * p)
                        nj = j + (dj * p)
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 2:
                                pig += 1

                # 2번: 밭의 가장 왼쪽 아래 모서리 찾으러 가자.
                # 처음 만난 1에서 아래로만 쭉 내려가는거야
                for p in range(1, N):
                    for di, dj in [[1, 0]]: # 아래로만 내려가
                        ni = i + (di * p)
                        nj = j + (dj * p)
                        if 0 <= ni < N and 0 <= nj < N:

                            # 쭉 내려가다가 0인 곳에 도착했어?
                            if arr[ni][nj] == 0: 
                                nj =  nj-1 # 그럼 그 전 자리를 arr[ni][nj]라고 하자.
                                
                                # 이제 경보기 범위를 탐색하면서 멧돼지(2)가 있는지 찾자.
                                for p in range(1, N):
                                    for di, dj in [[1, 0], [0, -1]]:
                                        ni = ni + (di * p)
                                        nj = nj + (dj * p)
                                        if 0 <= ni < N and 0 <= nj < N:
                                            if arr[ni][nj] == 2:
                                                pig += 1
    

                # 3번: 밭의 가장 오른쪽 위 모서리를 찾아볼까
                # 처음 만난 1에서 오른쪽로만 쭉 가는거야
                for p in range(1, N):
                    for di, dj in [[0, 1]]: # 오른쪽으만 가
                        ni = i + (di * p)
                        nj = j + (dj * p)
                        if 0 <= ni < N and 0 <= nj < N:

                            # 오른쪽으로 쭉 가다가 0인 곳에 도착했어?
                            if arr[ni][nj] == 0: 
                                ni = ni-1 # 그럼 그 전 자리를 arr[ni][nj]라고 하자.
                                
                                # 이제 경보기 범위를 탐색하면서 멧돼지(2)가 있는지 찾자.
                                for p in range(1, N):
                                    for di, dj in [[0, 1], [-1, 0]]:
                                        ni = ni + (di * p)
                                        nj = nj + (dj * p)
                                        if 0 <= ni < N and 0 <= nj < N:
                                            if arr[ni][nj] == 2:
                                                pig += 1


                # 4번: 밭의 가장 오른쪽 아래 모서리 찾으러 가자.
                # 1번에서 오른쪽으로 쭉 가
                for p in range(1, N):
                    for di, dj in [[0, 1]]: # 오른쪽으로만 가
                        ni = ni + (di * p)
                        nj = nj + (dj * p)
                        if 0 <= ni < N and 0 <= nj < N:
                            # 쭉 내려가다가 0인 곳에 도착했어?
                            if arr[ni][nj] == 0:
                                ni = ni-1 # 그럼 그 전 자리를 arr[ni][nj]라고 하자.
                                
                                # 거기서 밑으로 쭉가
                                for p in range(1, N):
                                    for di, dj in [[1, 0]]: # 밑으로만 가
                                        ni = i + (di * p)
                                        nj = j + (dj * p)
                                        if 0 <= ni < N and 0 <= nj < N:
                                            if arr[ni][nj] == 0:
                                                ni = ni-1 # 그럼 그 전 자리를 arr[ni][nj]라고 하자.
                                
                                                # 이제 경보기 범위를 탐색하면서 멧돼지(2)가 있는지 찾자.
                                                for p in range(1, N):
                                                    for di, dj in [[0, 1], [1, 0]]:
                                                        ni = ni + (di * p)
                                                        nj = nj + (dj * p)
                                                        if 0 <= ni < N and 0 <= nj < N:
                                                            if arr[ni][nj] == 2:
                                                                pig += 1     

    print(f'#{test_case} {pig}')




'''
2차원 리스트를 순회한다.
1인 지점을 만나면 1로 이루어진 밭을 찾는다.
밭의 4곳의 모서리의 인덱스를 찾는다.
-1번: 처음 1을 찾은게 왼쪽 위
-2번: 1번 1에서 오른쪽으로 쭉 가다가 0을 만나면 바로 직전 1이 오른쪽 위
-3번: 1번, 2번에서 찾은 1에서 아래로 쭉 가다가 마지막으로 나오는 1이 각각 왼쪽 아래, 오른쪽 아래

해당 4곳의 인덱스를 기준으로 잡아서
왼쪽 위 : 위, 왼쪽
왼쪽 아래 : 아래, 왼쪽
오른쪽 위 : 위, 오른쪽
오른쪽 아래 : 아래, 오른쪽
을 탐색해서 2(멧돼지)를 찾을때마다 pig 변수를 1씩 증가시킨다.
pig를 출력한다.
'''

'''
내답이
#1 57, #2 50, #3 59 이렇게 나옴
정답은
#1 2, #2 7, #3 2
'''
