'''
0b11011110 & 0b11011

0x4A3|25(10)

'''

KEY = 1004

def encode_decode(num):
    return num ^ KEY

print(encode_decode(1000))
print(encode_decode(4))




