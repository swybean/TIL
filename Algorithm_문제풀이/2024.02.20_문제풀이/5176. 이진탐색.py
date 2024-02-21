
def inorder_traverse(i):
    global number
    if i <= N:
        inorder_traverse(i * 2)
        tree[i] = number
        number += 1
        inorder_traverse(i * 2 + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    number = 1

    inorder_traverse(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')













