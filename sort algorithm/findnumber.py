# BOJ 1920: 수 찾기
# 디버그 함수 찾기
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# N 입력
N = int(input())

# A 입력
A = list(map(int, input().split()))
A_dict = dict()

for a in A:
    if not a in A_dict:
        A_dict[a] = 1
# M 입력
M = int(input())

# test case 입력
test = list(map(int, input().split()))

for t in test:
    if t in A_dict:
        print(1)
    else:
        print(0)
