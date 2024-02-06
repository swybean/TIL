import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_sum = -2000000000
    min_sum = 2000000000

    for i in range(N-1):
        if arr[i] + arr[i+1] > max_sum:
            max_sum = arr[i] + arr[i+1]
        if arr[i] + arr[i+1] < min_sum:
            min_sum = arr[i] + arr[i+1]

    print(f'#{tc} {max_sum} {min_sum}')


'''
오답
채점용 input 파일로 채점한 결과 fail 입니다.
(오답 : 99개의 테스트케이스 중 79개가 맞았습니다.)
'''

