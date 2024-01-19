
number_of_people = 0

print(f'현재 가입 된 유저 수 : {number_of_people}')

def increase_user():
    global number_of_people
    number_of_people += 1
    

increase_user()

def create_user(name, age, address):
    user_info = {'name':"", 'age':0, 'address':""}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    print(f"{name}님 환영합니다!")
    print(user_info)
    return user_info

result = create_user("홍길동", 30, "서울")

print(f'현재 가입 된 유저 수 : {number_of_people}')




