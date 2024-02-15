

T = 10
for test_case in range(1, T+1):
    tc_num = int(input())
    arr = list(map(int, input().split()))
    i = 1   # 맨 앞 숫자를 감소시킬 수(1~5) 변수 생성

    while True:
        num = arr.pop(0) - i  # 맨 앞 숫자를 꺼내와서 1만큼 감소시키기
        if num < 0:
            num = 0     # 뒤로간 숫자가 0보다 작아지면 0으로 유지하기
        arr.append(num) # arr 맨 뒤에 암호로 다시 추가하기

        if num <= 0: 
            break     # 마지막 숫자가 0보다 작아지는 경우 반복문 종료
        i += 1        # 다음 반복문에서 숫자를 감소 시킬 수를 1만큼 증가시키기

        # 싸이클당 5번만 하니까 6번째가 되면 다시 i = 1로 설정
        if i > 5:
            i = 1

    print(f'#{test_case}', *arr)

