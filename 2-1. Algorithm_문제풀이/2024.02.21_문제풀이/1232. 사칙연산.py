
def calculate(num):
    while num >= 1:
        if len(parent[num]) != 0:
            if tree[num] == '+':
                tree[num] = tree[parent[num][0]] + tree[parent[num][1]]
                num -= 1
            elif tree[num] == '-':
                tree[num] = tree[parent[num][0]] - tree[parent[num][1]]
                num -= 1
            elif tree[num] == '*':
                tree[num] = tree[parent[num][0]] * tree[parent[num][1]]
                num -= 1
            else:
                tree[num] = tree[parent[num][0]] // tree[parent[num][1]]
                num -= 1
        else:
            tree[num] = int(tree[num])
            num -= 1
  
for test in range(1, 11):
    N = int(input())
    tree = [''] * (N+1)
    parent = [[] for _ in range(N+1)]
    for _ in range(N):
        a = input().split()
        if len(a) == 4:
            parent[int(a[0])].append(int(a[2]))
            parent[int(a[0])].append(int(a[3]))
            tree[int(a[0])] = a[1]
        else:
            tree[int(a[0])] = a[1]
  
    calculate(N)
  
    print(f'#{test} {tree[1]}')