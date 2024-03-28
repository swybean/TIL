
w, h = map(int, input().split())  # w는 가로 j, h는 세로 i
p, q = map(int, input().split())  # p는 j좌표, q는 i좌표 (시작위치 좌표)
t = int(input())    # t초 후 개미의 좌표 (j, i)를 출력해야 함



time = 0

while time < t:
    if p < w:
        p += 1
        time += 1
        
    elif p == w:
        for _ in range(w):
            if p >  0:
                p -= 1
                time += 1
            if p <= 0:
                p += 1
                time += 1

timey = 0

while timey < t:
    if q < h:
        q += 1
        timey += 1
        
    elif q == h:
        for _ in range(h):
            if q > 0:
                 q -= 1
                timey += 1
            if q <= 0:
                q += 1
                timey += 1


print(p, q)