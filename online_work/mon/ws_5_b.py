data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'

for alpa in data_1:
    if alpa.isupper():
        print(alpa, end='')
    elif alpa in data_1:
        if alpa.isspace():
            print(alpa, end='')
      
print()

data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'

pra = ['내', '힘', '들', '다']
arr = []

for element in pra:
    start_index = data_2.find(element)
    if start_index != -1:
        arr.append(start_index)

print(arr)

arr.sort()
print(arr)

for index in arr:
    print(data_2[index], end='')
