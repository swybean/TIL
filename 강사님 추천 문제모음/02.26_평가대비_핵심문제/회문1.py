T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(input())) for _ in range(8)]
    result = 0  # 길이가 일치하는 회문의 개수 저장할 변수

    # 각 행에 대한 회문 검사
    for i in range(8):  # i행에서 길이가 N인 문자열을 차례로 검사
        for j in range(8-N+1):  
            if arr[i][j:j+N] == arr[i][j:j+N][::-1]:    # 해당 문자열이 뒤집어도 같다면 회문이다.
                result += 1
    # 각 열에 대한 회문 검사
    for i in range(8-N+1):  # j열에서 길이가 N인 문자열을 차례로 검사
        for j in range(8):  
            vertical = ''   # 수직 문자열을 저장하기 위한 변수
            for x in range(i, i+N):     # 현재 열의 길이 N만큼 반복하여 문자열을 이어 붙임
                vertical += arr[x][j]   
            if vertical == vertical[::-1]:  # 뒤집어도 같다면 회문이다.
                result +=1
 
    print(f'#{tc} {result}')    
