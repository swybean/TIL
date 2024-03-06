# 부모, 왼쪽, 오른쪽 순으로 진행
def make_tree(num):
    while num <= N:
        i = num
        tree[i] = num_list[i - 1]
        while i > 1:
            if tree[i] < tree[i//2]:
                tree[i], tree[i//2] = tree[i//2], tree[i]
            i//=2
        num += 1
 
Test = int(input())
 
for test in range(1, Test + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    tree = [0] * (N+1)
 
    tree[1] = num_list[0]
    make_tree(2)
 
    result = 0
    while N > 1:
        N //= 2
        result += tree[N]
 
    print(f'#{test} {result}')









