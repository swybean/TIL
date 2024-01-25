# 아래 함수를 수정하시오.
def reverse_string(x):
    my_list=list(x)
    my_list.reverse()
    my_list2 = ''.join(my_list)
    return my_list2



result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
