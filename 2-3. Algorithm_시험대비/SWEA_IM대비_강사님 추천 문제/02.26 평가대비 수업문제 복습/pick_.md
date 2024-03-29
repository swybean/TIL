# 큐와 스택

1. queue
    - 특성 : 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조이다.
    - 큐의 뒤에서는 삽입, 앞에서는 삭제만 이루어지는 구조
    - 선입선출구조 (FIFO)
        - 큐에 삽입한 순서대로 원소가 저장. 가장 먼저 삽입(first in)된 원소는 가장 먼저 삭제(first out)된다.

1. stack
    - 특성 : 삽입과 삭제의 위치가 제한적인 자료구조이다.
    - 스택에 저장된 자료는 ‘선형 구조’를 갖는다
        - 선형 구조: 자료간의 관계가 1대 1의 관계를 갖는다
        - 비선형 구조: 자료간의 관계가 1대 N의 관계를 갖는다 (트리)
    - 후입선출구조(LIFO)
        - 스택에 삽입된 순서대로 저장. 가장 나중에 삽입(last in)된 원소가 가장 먼저 삭제(first out) 된다.
    

# 백트래킹

- 해를 찾는 도중에 막히면(즉 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법
- 최적화 (optimization) 문제와 결정 (decison) 문제를 해결할 수 있음
    - 미로찾기, n-Queen, map coloring, 부분 집합의 합 문제 등
    

# 트리 (tree)

- 특징 : 비선형 구조
- 원소들 간에 1:n 관계를 가지는 자료구조
- 원소들 간에 계층관계를 가지는 계층형 자료구조
- 한 개 이상의 노드로 이루어진 유한 집합

## 이진 트리

- 모든 노드들이 2개의 서브 트리를 갖는 특별한 형태의 트리
- 각 노드가 자식 노드를 최대 2개 까지만 가질 수 있는 트리이다
    - 왼쪽 자식 노드 (left child node) / 오른쪽 자식 노드 (right child node)
- 레벨 i 에서의 노드의 최대 개수는 2^i 개
- 높이가 h인 이진트리가 가질 수 있는 노드의 최소 개수는 (h+1)개
최대 개수는 (2^h+1 -1)개 이다.
- 종류 : 포화 이진 트리, 완전 이진 트리, 편향 이진 트리
- 이진트리 - 순회
    
    1) 전위 순회 (preorder traversal) : VLR
    
    2) 중위 순회 (inorder traversal) : LVR
    
    3) 후위 순회 (postorder traversal) : LRV