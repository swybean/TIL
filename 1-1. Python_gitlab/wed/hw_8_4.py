# 사용자로부터 이름, 나이를 입력받아, 딕셔너리 형태로 저장하는 프로그램을 작성하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}
    

    def get_user_info(self):
        try:
            name = input('이름를 입력하세요:')
            age = int(input('나이를 입력하세요:'))
            self.user_data['이름'] = name
            self.user_data['나이'] = age
            print('사용자 정보:')
        except ValueError:
            print('나이는 숫자로 입력해야 합니다.')

    def display_user_info(self):
        try:
            print(f'이름: {self.user_data["이름"]}')
            print(f'나이: {self.user_data["나이"]}')
        except KeyError:
            print('사용자 정보가 입력되지 않았습니다.')


user = UserInfo()
user.get_user_info()
user.display_user_info()
