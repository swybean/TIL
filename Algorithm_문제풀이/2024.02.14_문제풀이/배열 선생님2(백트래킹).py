def f(i, k, s): # i-1까지 선택한 원소의 합
    global cnt
    global min_v
    cnt += 1
    if i==k:
        if min_v > s:
            min_v = s
    elif s >= min_v:            # 여기서 최소값과 비교했는데 최소값 보다 더 크면 뒤에 숫자가 뭐가 오든 최소값은 안변하니
        return                  # 탐색을 더이상 하지 않는 것이 백트래킹.
                                # 예를 들면 최소값이 10일 때 첫번째, 두번째 숫자의 합이 10보다 크면 세번재 숫자는 뭐가 오든
                                # 10보다 이미 크니 탐색하지 않아버리는 것.
    else:
        for j in range(i, k):    # P[i]자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]     # P[i]<->P[j]
            f(i+1, k, s+arr[i][P[i]])
            P[i], P[j] = P[j], P[i]  # 교환전으로 복구

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    min_v = 100
    cnt = 0
    f(0, N, 0)
    #print(f'#{tc} {min_v} {cnt}')
    print(f'#{tc} {min_v}')

''' 
백트래킹 기법을 사용하기 위해서는 기본적으로 "완전탐색"을 하는 코드를 작성해야 한다.
완전탐색을 하는 코드를 짜고,
중간에 조건문을 추가해서 해당 조건에 걸리면 그 경우의 수는 더이상 탐색하지 않고
다음 경우의 수를 탐색하러 가서 시간과 메모리 사용을 줄이는 것이 백트래킹 기법이다.

위 코드에서 아래 부분이 백트래킹을 위한 조건문이다.
elif s >= min_v:
    return

'''







