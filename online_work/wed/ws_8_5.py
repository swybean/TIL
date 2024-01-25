class Dog:
    sound = "멍멍"
    def __init__(self):
        pass




class Cat:
    sound = "야옹"
    def __init__(self):
        pass


# Dog, Cat
# Cat, Dog

class Pet(Cat, Dog):
    def __init__(self):
        super().__init__()

    
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'

pet = Pet()

result = str(pet)

print(result)


