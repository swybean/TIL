# 탁호준님 코드리뷰

T = 10
for tc in range(1, T+1):
    input()
    array = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0     # 맨 앞에서 초기화 해야 한다.
    for i in range(100):
        sum = 0     # 열의 합은 한개의 행 안에서 행이 바뀌면 초기화 해야 한다.
        for j in range(100):    # 열의 합을 구하는 작업
            sum += array[i][j]
        if max_sum < sum:   # 기존 최대보다 크니? 그래? 그럼 바꿔
            max_sum = sum
 

    for j in range(100):        # 위와 같은 방식으로 한다.
        sum = 0         # 이 sum은 이 for문안에서 쓰이고 끝났다.
        for i in range(100):
            sum += array[i][j]
        if max_sum < sum:
            max_sum = sum

# 위 for i, j는 형태가 똑같다. 따라서 포문은 그대로 두고 어레이ij ji로 해도 동일하게 사용할 수 있다.

    sum1 = 0    
    sum2 = 0
    for i in range(100):        # 대각선을 계산할 때
        sum1 += array[i][i]
        sum2 += array[99-i][i]  # 고정된 값에서 행을 빼면 왼쪽, 오른쪽 아래로 간다.
    if sum1 > sum2:             # 누가 더 크니?
        sum = sum1              # 얘는 더 바깥 인덴트에서 만들어진 적이 없는 sum이다.
    else:
        sum = sum2
 
    if max_sum < sum:           # 이 이프문을 기준으로 보면 sum은 위에 sum보다 더 바깥쪽에서 쓰이고 잇는것이다.
        max_sum = sum           # 틀린 거는 없지만 코딩 많이 한 사람이 보면 좀 불편하다.
 
    print(f'#{tc} {max_sum}')

#    if max_sum < sum1
#    if max_sum < sum2 이런식으로 이프문 2개를 써도된다.



'''
 기본 : 행 따로, 열 따로 계산하는 것


 '''

# 2번째 코드리뷰 : 누구껀지 모르겠음....ㅠ


# 이중for문 하나로 처리할 수 있다.
# 합은 따로 따로 더해야 한다.
# 최대값을 구하는 것이기 때문에 더할 때마다 커졌니? -> 여러번 갱신된다.
# 최소값은 이렇게 들어가면 오류가 난다. 인텐트를 하나 밖으로 뺀다. (if문 2개짜리) -> 원래는 탭 한번 더함


    for i in range(10):
        arr[i] list(map(int, input().split()))

        max_sum = 0
        corss_sum_1 = 0
        corss_sum_2 = 0
        for i in range(10):
            row_sum = 0
            col_sum = 0

        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        if max_sum < row_sum:
            max_sum = row_sum
        if max_sum < col_sum:
            max_sum = col_sum

        corss_sum_1 += arr[i][i]
        corss_sum_2 += arr[i][99 - i]
    if max_sum < corss_sum_1:
        max_sum = corss_sum_1
    if max_sum < corss_sum_2:
        max_sum = corss_sum_2


####### 3번째 코드리뷰 : 권장하지 않는다.
        


    max_sum = []
    for c in range(100):
        max_sum.append(sum([ic[] for i in arr]))    # 열의 합
        max_sum.append(sum(arr[c]))                 # 행의 합

    max_sum.append(sum([arr[i][i] for i in range(100)]))
    max_sum.append(sum([arr[99-i][0+i] for i in range(100)]))