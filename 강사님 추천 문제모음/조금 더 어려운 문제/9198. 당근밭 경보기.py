T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 문제에서 N = 10으로 고정이긴함
    arr = [list(map(int, input().split())) for _ in range(N)]
    pig = 0     # 경보기에 감지되는 멧돼지 수를 저장할 변수, 0으로 초기화
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                



'''
2차원 리스트를 순회한다.
1인 지점을 만나면 1로 이루어진 밭을 찾는다.
밭의 4곳의 모서리의 인덱스를 찾는다.
해당 4곳의 인덱스를 기준으로 잡아서
왼쪽 위 : 위, 왼쪽
왼쪽 아래 : 아래, 왼쪽
오른쪽 위 : 위, 오른쪽
오른쪽 아래 : 아래, 오른쪽
을 탐색해서 2(멧돼지)를 찾을때마다 pig 변수를 1씩 증가시킨다.
pig를 출력한다.
'''



