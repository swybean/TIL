def my_multi(number_1, number_2):
    result_1 = number_1 * number_2
    return result_1

my_multi(2, 3)
print(my_multi(2, 3))

# 함수를 수정하고 호출 결과를 result_1 변수에 할당하여 출력하시오.


def is_negative(number):
    result_2 = number < 0
    return result_2

print(is_negative(3))

def default_arg_func(default='기본 값'):
    return default

result_3 = default_arg_func()
result_4 = default_arg_func('다른 값')

print(result_3)
print(result_4)

