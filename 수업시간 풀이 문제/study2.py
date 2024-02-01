'''
N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 
각 학생의 이름과 성적 정보가 주어졌을때 성적이 낮은순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.

입력 조건 
• 첫 번째 줄에 학생의 수 N이 입력된다. (1 < N < 100,000)
• 두 번째 줄부터 N + 1 번째 줄에는 학생의 이름을 나타내는 문자열 A와 
  학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다. 
• 문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.

출력 조건 
• 모든 학생의 이름을 성적이 낮은 순서대로 출력한다.
• 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.

입력값 : 2 / 홍길동 95 / 이순신 77
출력값 : 이순신 홍길동
'''

N = int(input())

student_score = [list(input().split()) for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        if student_score[i] > student_score[j]:
            student_score[i], student_score[j] = student_score[j], student_score[i]

for student_name in student_score:
    print(student_name[0], end=' ')






'''
# N : 학생의 수, N을 입력한다.
N = int(input())

# 이름, 성적 순으로 student_score list를 만든다.
# 입력을 N번 만큼 해야 하기 때문에 for _ in range(N)을 사용
student_score = [list(input().split()) for _ in range(N)]

# 범위 range(N)까지를 반복하며 i를 찾는다.
for i in range(N):

    # 범위 range(i+1, N)까지 반복하며 j를 찾는다.
    # j는 i 다음 숫자여야 하기 때문에 범위를 range(i+1, N)으로 설정
    for j in range(i + 1, N):
    
        # student_score에서 성적을 비교해야 된다.
        # 이름, 성적 순으로 저장되어 있으니 [i][1]와 [j][1]를 비교해서 [i][1]가 더 큰 경우에
        if student_score[i][1] > student_score[j][1]:
        
            # i와 j의 위치를 바꾼다. (낮은 순으로 정렬해야하기 때문에)
            student_score[i], student_score[j] = student_score[j], student_score[i]

# 그냥 출력하면 이름, 성적이 같이 나와서 안 됐다.
# 따라서 student_name을 for문을 이용해 student_score에서 찾는다.
# 찾은 student_name에서 이름이 인덱스 0, 성적이 인덱스 1이기 때문에 인덱스 0을 출력한다.
# 그냥 출력하면 두 줄로 나와서 end=' '를 붙여서 공백 한 칸을 주고 한 줄에 이어서 나오게 한다.
for student_name in student_score:
    print(student_name[0], end=' ')
'''

