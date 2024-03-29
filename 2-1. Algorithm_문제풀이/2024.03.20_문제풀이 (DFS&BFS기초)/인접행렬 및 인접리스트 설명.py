# 1. 그래프를 코드로 표현

### 방식1 : 인접행렬
# V * V 배열을 활용해서 표현
# 갈 수 없다면 0, 있다면 1(혹은 가중치)을 저장

# 장점
# -노드 간의 연결 정보를 한 방에 확인 가능 
# -행렬곱을 이용해서 탐색이 쉽게 가능하다.
# -간선이 많을수록 유리

# 단점
# -노드 수가 커지면 메모리가 낭비된다
# -연결이 안된 것도 저장하기 때문에
# -노드 수 + 메모리 제한 반드시 확인할 것!!!!!!!

# 특징
# -양방향 그래프는 중앙 우하단 대각선 기준으로 대칭이 된다.
graph = [
    [0, 1, 0, 1, 0], # 0번 인덱스가 갈 수 있는 곳 : 1, 3번으로 갈 수 있다.
    [1, 0, 1, 0, 1], # 1번 인덱스가 갈 수 있는 곳 : 0, 2, 4번으로 갈 수 있다.
    [0, 1, 0, 0, 0], # 2번 인덱스가 갈 수 있는 곳 : 1번으로 갈 수 있다.
    [1, 0, 0, 0, 1], # 3번 인덱스가 갈 수 있는 곳 : 0, 4번으로 갈 수 있다.
    [0, 1, 0, 1, 0], # 4번 인덱스가 갈 수 있는 곳 : 1, 3번으로 갈 수 있다.
]


### 방식2 : 인접리스트 (권장하는 방식)
# V개의 노드가 갈 수 있는 정보만 저장

# 장점
# -메모리 사용량이 적다 (가장 큰 메리트)
# -탐색할 때 갈 수 있는 곳만 확인하기 때문에 시간적으로 효율적

# 단점
# -특정 노드 간 연결 여부를 확인하는데 시간이 걸린다.

graph = [
    [1, 3],     # 0번 인덱스가 갈 수 있는 곳 : 1, 3번으로 갈 수 있다.
    [0, 2, 4],  # 1번 인덱스가 갈 수 있는 곳 : 0, 2, 4번으로 갈 수 있다.
    [1],        # 2번 인덱스가 갈 수 있는 곳 : 1번으로 갈 수 있다.
    [0, 4],     # 3번 인덱스가 갈 수 있는 곳 : 0, 4번으로 갈 수 있다.
    [1, 3],     # 4번 인덱스가 갈 수 있는 곳 : 1, 3번으로 갈 수 있다.
]



### 방식3 : 연결리스트 (잘 쓰이지 않음)
# -잘 안쓰이는 이유 : 몇 개가 연결될 지 잘 모름 -> 구현이 어려움

