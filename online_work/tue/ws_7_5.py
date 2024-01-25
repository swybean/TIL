# 아래 클래스를 수정하시오.
class Shape:
     def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

     def __str__(self):
         return f'shape: width={self.num1}, height={self.num2}'

shape1 = Shape(5, 3)
print(shape1)
