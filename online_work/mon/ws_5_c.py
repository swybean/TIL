# def restructure_word(word, arr):

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'

arr = list(original_word)
print(arr)

# word 문자열에서 리스트로 바꾸기
word_list = list(word)

def restructure_word(word, arr):
    result = []
    for words in word:
        if words.isdecimal():
            arr.pop()
        else:
            for i in word_list:
                arr.remove(i)
    return result


        
result = restructure_word(word, arr)
print(result)


# for문이 중첩반복중
# 중첩되지 않게 for문 하나를 미리 맨 위에 꺼내고
# 이프 엘스 하기.
