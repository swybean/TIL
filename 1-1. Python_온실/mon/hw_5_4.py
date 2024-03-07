# 아래 함수를 수정하시오.
def find_min_max(x):
    min(x)
    max(x)
    return min(x), max(x)

# min() max() sort() 빼고 다시 구하기


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
