# 내가 푼거

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(M):
        num1 = arr[0]
        arr = arr[1:] + [num1]

    print(f'#{test_case} {arr[0]}')


# 박주연님 코드 큐 사용한거
 
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
 
    # 큐 생성
    q = num_list
    front = 0
    # 삽입 및 삭제
    for _ in range(M):
        front = (front + 1) % N
    print(f'#{t} {q[front]}')





