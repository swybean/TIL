num_data = {'0' : '0000', '1' : '0001', '2' : '0010', '3':'0011', 
            '4': '0100', '5': '0101', '6': '0110', '7': '0111', 
            '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 
            'C': '1100', 'D':'1101', 'E':'1110', 'F':'1111'}

T = int(input())
for test_case in range(1, T+1):
    N, arr = input().split()
    print(f'#{test_case} ', end='')
    for i in arr:
        if i in num_data:
            print(num_data[i], end = '')
    print()

