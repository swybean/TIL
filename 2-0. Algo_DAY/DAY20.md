재귀 함수 : 특정 시점으로 돌아오는 게 핵심!

재귀함수 팁  
1. 파라미터 바로 작성 X  
구조를 먼저 잡으면 자연스럽게 필요한 변수들이 보인다.



백트래킹은 완전탐색 + 가지치기  
그래서 시간복잡도 계산이 힘들다.  
1번 : 완전탐색 경우의 수를 계산  
2번 : 가지치기를 했을 때 대략적인 감소를 예측


---

예시 문제  
1,2,3으로 이루어진 순열을 만들자  

```python
arr = [i for i in range(1, 4)]
visited = [0] * 3

def dfs(level):
    # 기저조건
    # 이 문제에서는 3개를 뽑았을 때 까지 반복
    if level == 3:
        print(visited)
        return
    
    # 들어가기 전
    # 다음 재귀 호출
    # - 다음에 갈 수 있는 곳들은 어디인가?
    # - 이 문제에서는 1, 2, 3 세 가지 경우의 수가 존재 
    # 기본 코드
    visited[level] = arr[0]
    dfs(level +1)

    visited[level] = arr[1]
    dfs(level +1)

    visited[level] = arr[2]
    dfs(level +1)

    # 반복문
    for i in range(1, 4):
        visited[level] = arr[i]
        dfs(level + 1)

    # 재귀 갔다와서 할 로직

dfs(0)
```

---

순열 문제  
123, 132, 213, 231, 312, 321 등 중복된 숫자 사용없이 만들기  
조건 : 숫자는 한 번만 사용해라!

```python
arr = [i for i in range(1, 4)]
visited = [0] * 3

def dfs(level):
    for i in range(len(arr)):
        # 여기는 못가! (가지치기)
        # 백트래킹 팁
        # 갈 수 없는 경우를 조건으로 활용하는게 좋다.
        # 아래 코드처럼 갈 수 없을 때 continue
        if arr[i] in path:
            continue

        visited[level] = arr[i]
        dfs(level + 1)

        # 갔다와서 할 로직
        # 기존 방문을 초기화
        visited[level] = 0

dfs(0)
```

---






