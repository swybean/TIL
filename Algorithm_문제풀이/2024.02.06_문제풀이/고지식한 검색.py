## 고지식한 알고리즘 문제 강의 실습
def f(pat, txt, M, N):
    # txt에서 비교 시작 위치 i
    for i in range(N-M+1):
        for j in range(M):
            # 불일치하면 다음 시작위치로 가
            if txt[i+j] != pat[j]:
                break
        # 패턴 매칭에 성공해서
        # for문이 잘 끝난 경우에는 1을 반환해
        else:
            return 1
    # 모든 위치에서 비교가 끝난 경우
    return 0

T = int(input())
for tc in range(1, T+1):
    pat = input()
    txt = input()
    M = len(pat)
    N = len(txt)

    # txt의 시작위치를 i라고 하면
    # 마지막 비교위치는 N-3까지만 보면 된다.

    ans = f(pat, txt, M, N)
    print(f'#{tc} {ans}')

'''
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW

'''


