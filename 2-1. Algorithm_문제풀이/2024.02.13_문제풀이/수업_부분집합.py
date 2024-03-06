def f(i, k):
    if i == k:
        for j in range(k):
            if bit[j]:      # bit[j]가 1이면
                print(arr[j], end=' ')
        print()
    else:
        for j in range(2):
            bit[i] = j
            f(i+1, k)
        #bit[i] = 1         << else문 버전2
        #f(i+1, k)
        #bit[i] = 0
        #f(i+1, k)



N = 4
arr = [1, 2, 3, 4]
bit = [0] * N   # bit[i]가 부분집합에 포함되었는지 나타내는 배열
f(0, N)         # bit[i]에 1 또는 0을 채우고, N개의 원소가 결정되면 부분집합을 출력


'''
출력값
    < 공집합
4     
3     
3 4   
2     
2 4   
2 3   
2 3 4 
1     
1 4   
1 3   
1 3 4
1 2
1 2 4
1 2 3
1 2 3 4
'''