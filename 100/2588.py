A = int(input())
B = list(int(input()))

result1 = A * int(B[0])
result2 = A * int(B[1])
result3 = A * int(B[2])
result4 = A * int(B)

print(result1, result2, result3, result4, sep='\n')