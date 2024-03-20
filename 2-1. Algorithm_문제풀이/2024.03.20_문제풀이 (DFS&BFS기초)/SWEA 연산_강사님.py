'''
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.

사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 
최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.

단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.

예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.

[입력]

첫 줄에 테스트 케이스의 개수가 주어지고, 
다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다. 1<=N, M<=1,000,000, N!=M

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

def bfs(N, M):
    q = []              # 큐 생성
    q.append(N)         # 시작점 인큐
    visited = [0] * (1000001)   # visited 생성
    visited[N] = 1              # 시작점 표시
    
    while q:            # 큐에 탐색할 노드가 남아있으면
        t = q.pop(0)    # 디큐
        if t == M:
            return visited[t] - 1
        # t에 인접한 w, 방문한 적이 없으면
        if t - 10 > 0 and visited[t-10] == 0:
            q.append(t - 10)
            visited[t - 10] = visited[t] + 1

        if 0 < t -1 and visited[t - 1] == 0:
            q.append(t - 1)
            visited[t - 1] = visited[t] + 1
                                   
        if t + 1 <= 1000000 and visited[t + 1] == 0:
            q.append(t + 1)
            visited[t + 1] = visited[t] + 1

        if t * 2 <= 1000000 and visited[t * 2] == 0:
            q.append(t * 2)
            visited[t * 2] = visited[t] + 1
    return -1   # 생략 가능 (디버깅용 옵션)

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    print(f'#{test_case} {bfs(N, M)}')



'''
3
2 7
3 15
36 1007
 
#1 3
#2 4
#3 8
'''