# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    
    def __init__(self):
        Animal.num_of_animal += 1
        


class Dog(Animal):
    def __init__(self):
        super().__init__()
      
    def bark(self):
        print('멍멍!')


class Cat(Animal):
    def __init__(self, sound):
        super().__init__()
        self.sound = sound

    def meow(self):
        print('야옹!')


cat1 = Cat("야옹")
cat1.meow()
