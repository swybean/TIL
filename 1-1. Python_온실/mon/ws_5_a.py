N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.
for num in range(len(data_1)):
    arr_1.append(data_1[num])
print(arr_1)


M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'

arr_2 = data_2.split() # 공백기준으로 나눠서 arr_2에 할당

for number in arr_2:
    if int(number) % 2 != 0:
        print(number)



