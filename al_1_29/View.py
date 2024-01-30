T = 10


for text_case in range(1, T+1):
    N = int(input())   # 건물 개수
    high = list(map(int, input().split()))



'''
ans = 0   # 조망권의 합
for i : 2 -> N-3   # 양쪽 2칸씩은 건물을 짓지 못하기 때문에
양쪽 4개 [h(i-2) h(i-1) h(i+1) h(i+2)] 중 가장 높은 곳의 높이가
h의 높이보다 낮으면 h는 조망권이 확보되는 것이다.

'''






