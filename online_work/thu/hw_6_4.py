# 아래 함수를 수정하시오.
def add_item_to_dict(new_dict, x, y):
    new_dict = my_dict.copy()
    new_dict.setdefault('country', 'USA')
    
    return new_dict



my_dict = {'name': 'Alice', 'age': 25}

result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)


# 주어진 딕셔너리에서 특정 키와 값을 이용하여 항목을 추가하는 함수를 작성하시오.
# 딕셔너리와 키, 값의 쌍을 인자로 받아 항목을 추가한 새로운 딕셔너리를 반환해야 한다.
# 결과물 : {'name': 'Alice', 'age': 25, 'country': 'USA'}