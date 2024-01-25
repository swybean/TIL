# 아래 함수를 수정하시오.
def get_keys_from_dict(x):
    new_dict = x.keys()
    new_list = list(new_dict)
    return new_list
    
    






my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)


# 주어진 딕셔너리에서 모든 키를 리스트로 반환하는 함수를 작성하시오.
# 딕셔너리를 인자로 받아 모든 키를 담은 리스트를 반화해야 한다.
# 결과물 : ['name', 'age']