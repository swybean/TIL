K = 3
N = 7
arr = [0, 1, 0, 1, 1, 1, 0]

count = 0
ans = 0

for i in range(N):
    if arr[i] == 0:
        if count == K:
            ans += 1
        count = 0
    else:   # arr[i] == 1인 경우
        count += 1
        if i==N-1:   # (and count == K:를 붙이면 아래 if count == K:대신 쓸수 있음)
            if count == K:
                ans += 1
print(ans)


    # if arr[i] == 1:
    #     count += 1
    # elif arr[i] == 0 or i== N-1:




########## 1번 풀이
# 0을 만나면 0으로 초기화
# 1을 만나면 +1
# 위 예시로 보면 count가 0, 1, 0, 1, 2, 3순으로 변한다.

# count = K 일 때 단어가 들어갈 수 있다.
# ans : 단어가 들어갈 수 있는 자리 개수
# ans = 0으로 설정, count = K 일때 ans += 1을 하면 된다.
# 딱 맞아 떨어지는 곳에만 단어가 들어갈 수 있는점 유의하기


########### 2번 풀이
# count를 0을 만나면 0으로 초기화, 1을 만나면 +1
# 초기화 전에 count = k인지 확인하고 초기화
# if를 사용해서 같으면 ans를 + 1하고 초기화, 아니면 그냥 초기화
# 그러나 마지막이 111로 끝나 0을 만나지 않으면 ans+1을 안하기에
# 마지막일 때도 count=k인지 확인을 하게 설정하거나
# 마지막 줄 뒤에 0인 줄을 추가해둔다.



