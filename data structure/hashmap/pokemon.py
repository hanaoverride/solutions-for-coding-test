# BOJ 1620: 나는야 포켓몬 마스터 이다솜

# 디버그 함수 및 플래그 정의
DEBUG = True
def debug(*args):
    if DEBUG:
        print(*args)

# k, v dict와 v, k dict 동시선언
poke_dict = dict()
poke_inv = dict()

# N, M 입력
N, M = map(int, input().split())

# 포켓몬 도감 완성
for i in range(1, N+1):
    newline = input()
    # 포켓몬 도감: 정방향
    poke_dict[newline] = i
    # 포켓몬 도감: 역방향
    poke_inv[i] = newline

# 테스트케이스 M개 입력
for _ in range(M):
    newline = input()
    # 숫자인가?: 역방향 호출
    if newline.isdigit():
        print(poke_inv[int(newline)])
    # 문자인가?: 정방향 호출
    else:
        print(poke_dict[newline])