import sys
sys.stdin = open('input3.txt', 'r')

another_planet_num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
 
T = int(input())
for tc in range(1, T+1):
    t, N = map(str, input().split())
    num_list = list(map(str, input().split()))
 
    result = []
    for another_num in another_planet_num:
        for i in range(len(num_list)):
            if num_list[i] == another_num:
               result += [another_num]
    print(t)
    print(*result)




