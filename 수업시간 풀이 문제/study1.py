'''
문제 : 위에서 아래로
난이도 • I 풀이 시간 15분 | 시간 제한 1 초 | 메모리 제한 128MB 

하나의 수열에는 다양한 수가 존재한다. 
이러한 수는 크기에 상관없이 나열되어 있다. 
이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다. 
수열을 내림차순으로 정렬하는 프로그램을 만드시오.

입력 조건 
• 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다. (1 < N < 500)
• 둘째 줄부터 N + 1 번째 줄까지 N개의 수가 입력된다. 
• 수의 범위는 1 이상 100,000 이하의 자연수이다.

출력 조건 
• 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다.
동일한 수의 순서는 자유롭게 출력해도 괜찮다.

입력값 : 
3 
15
27
12
출력값 : 27 15 12
'''


N = int(input())     # N : 수의 개수, N을 입력한다.

# 입력한 N개의 수를 num_list에 입력한다.
# for _ in range(N)을 사용해서 N번 만큼 수를 입력할 수 있게 만들었다.
num_list = [int(input()) for _ in range(N)]

# 범위 range(N)까지를 반복하며 i를 찾는다.
for i in range(N):

    # 범위 range(i+1, N)까지 반복하며 j를 찾는다.
    # j는 i 다음 숫자여야 하기 때문에 범위를 range(i+1, N)으로 설정
    for j in range(i + 1, N):

        # num_list에서 i랑 j의 크기를 비교해봤는데 j가 더 큰 경우에는
        if num_list[i] < num_list[j]:
            
            # i랑 j의 위치를 바꾼다. 이걸 계속 for문에서 반복
            num_list[i], num_list[j] = num_list[j], num_list[i]

# 반복이 다 끝나면 num_list를 언패킹해서 []를 벗겨서 출력한다.
print(*num_list)

