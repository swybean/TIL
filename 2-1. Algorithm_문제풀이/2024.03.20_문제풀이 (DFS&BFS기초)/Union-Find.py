# 1~6번까지 노드가 존재한다.


# 1. Make-Set(x) : 집합 만들기
# 자기자신이 대표인 데이터 6개가 리스트로 생성된다. 
# -> [0, 1, 2, 3, 4, 5, 6] 
# 이것이 무엇을 의미하냐? : "대표자 인덱스"를 의미한다.
def make_set(n):
    return [i for i in range(n)]

# 1~6번까지 사용하기 위해 7개를 생성 (0번은 버림, 없다고 생각하기)
parents = make_set(7)




# 2. FInd-Set(x) : 대표자를 찾아보자!
# 부모 노드를 보고, 부모 노드도 연결이 되어 있다면 다시 반복
# 언제까지 ? : 자기자신이 대표인 데이터를 찾을 때 까지
def find_set(x):
    # 기저조건 : 자기자신이 대표면 끝
    if parents[x] == x:
        return x
    
    # 위의 조건이 걸리지 않았다 == 대표자가 따로 있다.
    # 그니까 해당 부모 노드의 부모 노드를 보러 가기 위해 재귀한다.
    return find_set(parents[x])





# 3. Union(x, y) : 두 집합을 합치자!
def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 이미 같은 집합에 속해있다면 continue
    if x == y:
        return
    
    # 다른 집합이라면 합침
    # 예) 더 작은 루트노드에 합쳐라~
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


