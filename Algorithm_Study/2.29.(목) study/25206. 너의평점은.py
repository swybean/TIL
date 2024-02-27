grade_dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0':2.0, 
             'D+':1.5,'D0': 1.0, 'F': 0.0}


major_score = 0     # 전공과목별 (학점 × 과목평점)의 합
total_credit = 0    # 총학점

for _ in range(20): # 과목수는 20개라고 문제에서 주어짐
    subject, credit, grade = input().split()    # 과목명, 학점, 성적 입력

    if grade != 'P':    # 패논패 과목이 아닌 경우에만
        total_credit += float(credit)   # 총학점에 학점 추가하기 (실수형으로)
        major_score += float(credit) * grade_dic[grade] # 전공과목별 합에 추가하기

result = major_score / total_credit # 결과는 전공과목별 합 나누기 총학점
round_result = round(result, 6)     # 소수점 6자리까지 반올림

print(round_result)