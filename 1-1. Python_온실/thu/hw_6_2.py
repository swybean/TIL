# 아래 함수를 수정하시오.
def remove_duplicates_to_set(x):
    for num in x:
        if x.count(num) != 1:
            x.remove(num)
    x = set(x)
    return x





result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)



# 중복 요소 제거 후 셋으로 변환하는 함수를 작성하시오.
# 리스트를 인자로 받아 중복이 된 제거된 셋을 반환해야 한다.
# {1, 2, 3, 4, 5}