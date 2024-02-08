import sys
sys.stdin = open('input3.txt', 'r')

############### 선생님 강의 실습 버전1 ################

# 함수 제작
def dfs(start, end):  # 출발과 도착
    # visited, stack 생성 및 초기화
    visited = [0] * 100
    stack = []
    visited[start] = 1  # 시작점 방문표시
    v = start           # 현재 방문 위치
    while True:         # 탐색

        # 현재 방문위치 v에 인접하고 방문안한 w면
        if A[v] != -1 and visited[A[v]] == 0: 
            stack.append(v) # 지나간 칸을 스택에 저장하고 이동
            v = A[v]
            visited[v] = 1  # 방문했다는 표시

        # 인접 도시가 있는데 방문했던 곳이면
        elif B[v] != -1 and visited[B[v]] == 0: # 두번째 도시가 있는지 확인
                stack.append(v)
                v = B[v]
                visited[v] = 1

        # 지나온 곳에서 다시 탐색
        else:   
            if stack:   # 지나온 곳이 남아있으면
                v = stack.pop()
            else:       # 출발지까지 거슬러와서 가능한 모든 곳을 확인한 경우
                break   # whilte True:를 종료
        if v == end:
            return 1
    return 0    # 99번에 한 번도 도착한 적이 없으면 0 반환



for _ in range(10):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    ########### 문제에 있는 '데이터 저장 가이드' 처럼 풀어주신 코드 ###########

    A = [-1] * 100   # A[i] i에 인접한 도시번호
    B = [-1] * 100   # B[i] i에 인접한 도시번호
    # -1로 한건 0으로 돌아올 수도 있기 때문에 -1로 설정
    # 확실하게 문제에서 0으로 돌아올 수 없다하면 0으로 해도 됨

    #for i in range(E):  # 순서쌍 개수만큼 가져오는 방법
    for i in range(0, E*2, 2): # 순서쌍 2개씩 가져오는 방법
        # n1->n2 도로가 있음
        n1, n2 = arr[i], arr[i+1]   #(arr[i]는 0 2 4 6, arr[i+1]은 1 3 5 7을 가져오는 것)
       
        if A[n1] == -1:
            A[n1] = n2
        else:
            B[n1] = n2

    print(f'#{tc} {dfs(0,99)}')

'''
출력값 아래처럼 나와야 함 -> 성공!
#1 1
#2 1
#3 1
#4 0
#5 1
#6 1
#7 0
#8 0
#9 0
#10 0
'''