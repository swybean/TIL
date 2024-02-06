####### 초보자 회문 함수 사용
def f(txt):
    N = len(txt)
    ans = 1  # 회문이라 가정
    for i in range(N // 2):  # 비교 횟수 결정
        if txt[i] != txt[N - 1 - i]:  # 비교
            return 0
    return 1
 
T = int(input())
for tc in range(1, T+1):
    txt = input()
    ans = f(txt)
    print(f'#{tc} {ans}')

####### 초보자 회문 함수 미사용
T = int(input())
for tc in range(1, T+1):
    txt = input()
    N = len(txt)
    ans = 1                 # 회문이라 가정
    for i in range(N//2):   # 비교 횟수 결정
        if txt[i] != txt[N-1-i]:    # 비교
            ans = 0
            break
    print(f'#{tc} {ans}')  


###### 가장 빠른 문자열 타이핑 
T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    # 1번 풀이
    N = A.count(B)
    print(N)
    print(f'#{tc}', len(A)-N*len(B)+N)
    
    # 2번 풀이
    print(f'#{tc}', len(A.replace(B, 'b')))



###### 회문(제출용)
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 문장 개수와 길이 / M은 부분적으로 조사할 길이
    arr = [input() for _ in range(N)]
    result = ''  # 여기에 미리 result를 만들어놔야 한다.
# 가로 탐색
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j: j+M] == arr[i][j: j+M][::-1]: #  i 행에서 j부터 j+M 까지의 부분 문자열이 뒤집은것과 같다면
                result = arr[i][j : j+M]    # result를 구했으면 반복을 탈출해야한다.
                break # for j를 탈출하는 break
        else:
            continue    # for i를 실행시키라는 의미
        break   # 이중 for문을 끝내야 하는 문제 : 한 번 답을 구하면 끝내야 하는 문제, 더 돌면 답이 바뀔 수 있는 문제
# break 말고 아예 함수로 만들어서 return 시키는 방법도 있다.

# 세로 탐색
    for i in range(N-M+1):
        for j in range(N):
            # 세로축만 모은 단어 생성
            vertical = ''
            for x in range(i, i+M):
                vertical += arr[x][j]
            if vertical == vertical[::-1]:
                result = vertical
                break
        else:
            continue
        break               
    print(f'#{tc} {result}')



##### 회문(제출용) 강사님이 올리신 함수 버전
def f(N, M):
    for i in range(N):
        for j in range(N - M + 1):
            if arr[i][j: j + M] == arr[i][j: j + M][::-1]:  # i 행에서 j부터 j+M 까지의 부분 문자열이 뒤집은것과 같다면
                result = arr[i][j: j + M]
                return result
 
    # 세로 탐색
    for i in range(N - M + 1):
        for j in range(N):
            # 세로축만 모은 단어 생성
            vertical = ''
            for x in range(i, i + M):
                vertical += arr[x][j]
            if vertical == vertical[::-1]:
                result = vertical
                return result
    return 0
 
 
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N은 문장 개수와 길이 / M은 부분적으로 조사할 길이
    arr = [input() for _ in range(N)]
    result = f(N, M)
 
 
    print(f'#{tc} {result}')


###### 회문(제출용) 강사님 버전2
def palin(n, m, block): # 원저자 : 장지현님, 첫 행에 회문이 있어도 답을 찾을 수 있도록 수정한 코드
    ansRow = -1
    startIdx = 0
    endIdx = 0
 
    for i in range(n):
        for a in range(n - m + 1):
            cnt = 0
            for b in range(m // 2):
 
                if block[i][a + b] == block[i][(m + a) - 1 - b]:
                    cnt += 1
 
            if cnt == m // 2:
                ansRow = i
                startIdx = a
                endIdx = m + a
 
                ans = []
                for word in range(startIdx, endIdx):
                    ans.append(block[ansRow][word])
                return ans
    return 0
 
 
T = int(input())
for tc in range(1, T + 1):
    lenarr, lenpat = map(int, input().split())
    blockR = [list(input()) for _ in range(lenarr)]
 
    # 가로 함수값
    ansRow = palin(lenarr, lenpat, blockR)
 
    # 세로
    # 2차원 배열 초기화
    blockC = [[0] * lenarr for _ in range(lenarr)]
 
    for x in range(lenarr):
        for y in range(lenarr):
            blockC[x][y] = blockR[y][x]
 
    # 세로 함수값
    ansCol = palin(lenarr, lenpat, blockC)
 
    if ansRow:
        print(f'#{tc}', end=" ")
        for letter in range(len(ansRow)):
            print(ansRow[letter], end="")  # 1 TLMMHOOOHMMLT
        print()
    else:
        print(f'#{tc}', end=" ")
        for letter in range(len(ansCol)):
            print(ansCol[letter], end="")
        print()





##### 구간합
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    min_v = 1000000
    max_v = 0

    s = 0 #구간의 합
    for i in range(M):
        s += arr[i]

    min_v = max_v = s

    for i in range(N-M):    # 이미 계산된 구간의 합에서 제외한 맨 앞 원소
        s -= arr[i]
        s += arr[i+M]       # 현재 구간 다음 원소를 구간에 추가
        if min_v > s:
            min_v = s
        if max_v < s:
            max_v = s
    
    print(f'#{tc} {max_v - min_v}')



