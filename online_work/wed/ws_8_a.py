data = {'name': '홍길동'}

if 'age' in data:
    result = data['age']
    print(result)
else:
    print('data에는 age라는 키가 없습니다.')
    data['age'] = 30
    print(data)



arr = ['반갑', '하세요', '안녕']

result = arr[:-1]

while result:
    print(result.pop())

print(result)

try:
    result.pop()
except IndexError:
    print('더 이상 pop 할 수 없습니다.')



word = '3.15'
try:
    print(int(word))
except ValueError:
    print('정수로 변환 가능한 값을 입력해 주세요.')



