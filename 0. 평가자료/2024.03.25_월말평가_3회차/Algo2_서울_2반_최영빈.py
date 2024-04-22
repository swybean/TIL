

T = int(input())
for test_case in range(1, T+1):
    N, V = map(int, input().split())    # N은 섬의 수, V는 예산
    arr = list(map(int, input().split()))   # 다리에 대한 건설비용 리스트

    now_sum = 0     # 현재까지 사용한 건설비용의 합계
    cnt = 0         # 건설한 다리의 수

    for i in range(N):  # 리스트 길이만큼 반복해서 i를 순회할건데

        # 만약 현재까지 건설비용 합 + 이번에 건설할지 고민하는 다리(i)의 비용을 합친 합계가 예산보다 작거나 같으면
        if now_sum + arr[i] <= V:
            now_sum += arr[i]       # num_sum에 해당 다리를 건설할 비용을 추가하고
            cnt += 1                # 건설한 다리 개수 cnt도 1을 증가시킨다.

    print(f'#{test_case} {cnt} {now_sum}')

