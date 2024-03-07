# 아래 클래스를 수정하시오.
class StringRepeater:
    
    def repeat_string(self, num, repeater1):
        # for i in range(num):
        #     print(repeater1)      # 더 짧게 하는 법
                                    # self. 안써도됨
        self.num = num
        self.repeater1 = repeater1
        for i in range(self.num):
            print(self.repeater1)

       

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")

