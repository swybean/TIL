

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())    # N : 컨테이너 수, M : 트럭 수
    arr_weight = list(map(int, input().split()))    # 화물들의 무게
    arr_truck = list(map(int, input().split()))     # 트럭들의 적재용량

    arr_weight.sort()   # 오름차순 정렬
    arr_truck.sort()    # 오름차순 정렬

    result = 0      # 트럭에 최종적으로 실은 컨테이너 무게

    iren = 0        # result 가기전 변수
    now_result = 0  # 현재 트럭에 실어볼 컨테이너 무게

    for i in arr_weight:
        for j in arr_truck:
            if i <= j:
                now_result += i
                if iren < now_result:
                    iren = now_result


        








'''
3
3 2
1 5 3
8 3

5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5

10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13

#1 8
#2 45
#3 84
'''