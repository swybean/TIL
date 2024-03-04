"""
답안 예시)
5 2 3
7 3 4 1 5

문제 조건)
- N개의 블록을 쌓아 2개의 탑을 만들려고 함
- 첫 번째 탑은 M1층, 두 번째 탑은 M2층 --> M1 + M2 = N ex) N = 5, M1 + M2 = 5
- 각 블록의 무게는 서로 다를 수 잇으며, 블록을 쌓을 때는 무게 x층 만큼의 비용 발생
- ex. 1층 -> 블록의 무게 x 1 / 2층 -> 블록의 무게 x 2 / 3층 -> 블록의 무게 x 3 = total_cost
- 따라서, N, M1, M2가 주어질 때, 이때 최소 비용을 구해라!!!!
"""


T = int(input())
for tc in range(1, T + 1):
    N, M1, M2 = map(int, input().split())
    N_list = list(map(int, input().split()))

    N_list.sort(reverse=True)                  # 내림차순으로 정렬
    m1_list = []                               # m1에 해당하는 블록의 무게를 담을 빈 리스트 생성
    m2_list = []                               # m2에 해당하는 블록의 무게를 담을 빈 리스트 생성

    if M1 >= M2:                               # 만약, m1층이 더 크다면,
        for i in range(M2*2):                  # m2층만큼 돌면서 m1_list와 m2_list 번갈아 값을 부여해줌
            if i % 2 == 0:
                m1_list.append(N_list[i])
            if i % 2 == 1:
                m2_list.append(N_list[i])

        for j in m1_list:                      # 이때, m1_list에 있는 값들은
            N_list.remove(j)                   # N_list에서 제거

        for j in m2_list:                      # 이때, m2_list에 있는 값들은
            N_list.remove(j)                   # N_list에서 제거

        for k in N_list:                       # 그리고 나서, N_list에 남은 값들을
            m1_list.append(k)                  # 층이 더 큰, m1_list에 추가

    if M1 < M2:                                # m2층이 더 크다면,
        for i in range(M1*2):                  # 위의 방법과 동일 -> 단, 이때는 층이 더 큰 m2_list에 추가
            if i % 2 == 0:
                m2_list.append(N_list[i])
            if i % 2 == 1:
                m1_list.append(N_list[i])

        for j in m1_list:
            N_list.remove(j)

        for j in m2_list:
            N_list.remove(j)

        for k in N_list:
            m2_list.append(k)

    m1_list.sort(reverse=True)                 # 다시, 오름차순으로 정렬
    m2_list.sort(reverse=True)                 # 다시, 오름차순으로 정렬

    total_cost_m1 = 0
    cnt_m1 = 1
    for j in m1_list:                          # m1_list에 해당하는, 즉 블록의 무게에
        total_cost_m1 += j * cnt_m1            # 각각의 층에 해당하는 값을 곱함 --> 곧, m1에 해당하는 총 비용
        cnt_m1 += 1

    total_cost_m2 = 0
    cnt_m2 = 1
    for j in m2_list:                          # m2_list 해당하는, 즉 블록의 무게에
        total_cost_m2 += j * cnt_m2            # 각각의 층에 해당하는 값을 곱함 --> 곧, m2에 해당하는 총 비용
        cnt_m2 += 1

    total_cost = total_cost_m1 + total_cost_m2

    print(f'#{tc} {total_cost}')

