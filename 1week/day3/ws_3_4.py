def create_user(name, age, address):
    user_info = {'name':"", 'age':0, 'address':""}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    print(f"{name}님 환영합니다!")
    return user_info

names = ["김시습", "허균", "남영로", "임제", "박지원"]
ages = [20, 16, 52, 36, 60]
addresses = ["서울", "강릉", "조선", "나주", "한성부"]

user_list = list(map(create_user, names, ages, addresses))

print(user_list)