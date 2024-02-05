'''
1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

주어질 숫자는 30을 넘지 않는다.
'''


N = int(input())
     
num = 1
num_list = []

for i in range(1, N+1):
    if i * 2 > num:
        num_list + [i]
    print(num_list)







