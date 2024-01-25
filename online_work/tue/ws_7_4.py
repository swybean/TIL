# 아래 클래스를 수정하시오.
class Shape:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def print_info(self):
        Width = self.num1
        Height = self.num2
        Area = self.num1 * self.num2
        Perimeter = self.num1 * 2 + self.num2 * 2
        print(f'Width: {Width}')
        print(f'Height: {Height}')
        print(f'Area: {Area}')
        print(f'Perimeter: {Perimeter}')


shape1 = Shape(5, 3)
shape1.print_info()


