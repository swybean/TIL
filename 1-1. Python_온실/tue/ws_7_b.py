# 아래에 코드를 작성하시오.




class Myth:
    type_of_myth = 0
    def __init__(self, name):
        self.name = name
        Myth.type_of_myth += 1
        print(name)

    @classmethod
    def num_myth(cls):
        print(f'현재까지 생선된 신화 수 : {cls.type_of_myth}')

    @staticmethod
    def description():
        print('신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')



myth1 = Myth('dangun')
myth2 = Myth('greek & rome')
Myth.num_myth()
Myth.description()


