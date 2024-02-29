'''
주어진 2차원 배열 지도에 위치한 기지국으로 커버되지 않는 집의 수를 찾는 프로그램을 작성하시오.

[제약사항]
2차원 배열의 크기의 n은 50이하이다. 기지국의 수는 50이하이다.

[입력]
첫 줄에는 테스트 케이스의 수가 주어지고, 그 다음 줄부터 각 테스트 케이스가 n개의 줄로 구성된다. 
테스트 케이스의 첫 줄에는 n이 주어지고, 다음 n개 줄에는 2차원 배열의 각 행이 한 줄에 차례로 주어진다. 
단, 집이 위치한 원소는 H, 기지국이 위치한 원소는 A, B, C로 표시하며, 
각각 동서남북으로 1, 2, 3개를 커버하는 기지국이다. X인 원소는 아무 것도 없다는 것을 나타낸다.

[출력]
각 줄은 #x로 시작하고 공백을 하나 둔 다음, 테스트 케이스에 주어진 기지국에 cover가 되지 않는 집의 수를 출력한다. 
단, x는 테스트 케이스 번호이다.
'''






'''
2
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX
9
XXXHXXXXX
XXXHXXXXX
XXHCHXHHX
XXHHXXHXX
XXXHXHBHH
XHAHHXXXX
XXHXXXHXX
XXAHXHAHX
XXHXHXXXX

#1 4
#2 4
'''