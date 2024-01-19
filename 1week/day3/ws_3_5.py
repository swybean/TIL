number_of_people = 0
number_of_book = 100

def increase_user():
    pass

def rental_book(info): # 매개인자가 info라는 딕셔너리가 들어가야 함!
    decrease_book(info['age']//10)
    print(f"{info['name']}님이 {info['age']//10}권의 책을 대여하였습니다.")

def decrease_book(num):
    global number_of_book
    number_of_book -= num
    print(f'남은 책의 수 : {number_of_book}')

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def create_user(NAME,AGE,ADDRESS):
    user_info ={'name':NAME,'age':AGE,'address':ADDRESS}
    return user_info

many_user = list(map(lambda name, age, address: create_user(name,age,address),name,age,address))
info = map((lambda many_user :{'name':many_user['name'], 'age': many_user['age']}),many_user)
list(map(lambda name : print(f"{name}님 환영합니다."),name)) #환영인사
list(map(rental_book, info))

#print(list(info))