

T = int(input())
for tc in range(1,T+1):

    N = int(input())

    # N 이 10의 배수로 주어짐

    # 그림그려보면 f(30) 부터 쌤이 말씀한 규칙있음 -> 재귀함수 만들것
    #f(30) = f(20) + 2 * f(10)
    #f(40) = f(30) + 2 * f(20)
    #f(50) = f(40) + 2 * f(30)
    # ...반복됨

    #재귀함수
    def f(N):
        # 규칙 없는 부분 f(10)과 f(20) 은 그냥 주기
        if N == 10:
            return 1
        if N == 20:
            return 3

        # N이 30일때부터는 규칙 있음
        else:
            return f(N-10) + f(N-20) * 2

    print(f'#{tc} {f(N)}')