'''
완전탐색 + 백트래킹

출력
1. 최소비용
2. 최소비용 식재료 번호 공백구분 + 오름차순
2-1. 만족하는 답이 없으면 -1 출력, 둘째줄 아무것도 출력 x
'''



N = int(input())    # 식재료의 개수 N
target = list(map(int, input().split())) # 최소 영양성분 리스트
arr = [list(map(int, input().split())) for _ in range(N)]   # 식재료 성분 + 가격 리스트


