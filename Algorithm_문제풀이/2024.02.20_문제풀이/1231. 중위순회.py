def inorder_traverse(T):
    global yb
    if T:
        inorder_traverse(left[T])
        print(tree[T], end='')
        inorder_traverse(right[T])
 
 
for test_case in range(1, 11):
    n = int(input())
    yb = 0
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    tree = [0] * (n + 1)
 
    for i in range(n):
        input_list = input().split()
        # input_list[0] = 노드 번호, input_list[1] : 알파벳
        tree[int(input_list[0])] = input_list[1]
 
        if len(input_list) >= 3:
            left[int(input_list[0])] = int(input_list[2])
 
        if len(input_list) == 4:
            right[int(input_list[0])] = int(input_list[3])
 
    print(f'#{test_case} ', end='')
    inorder_traverse(1)
    print()













