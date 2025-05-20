# BOJ 7219: 비밀번호

# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# 비밀번호 해시맵 선언
password = dict()

# N, M 입력
N, M = map(int, input().split())

# 사이트와 비밀번호쌍 입력
for _ in range(N):
    site, pw = map(str, input().split())
    password[site] = pw

debug(password)
# 각 사이트에 대해 비밀번호 출력
for _ in range(M):
    site = input()
    print(password[site])