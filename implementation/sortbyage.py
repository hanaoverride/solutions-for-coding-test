# BOJ 10814: 나이순 정렬
import sys
input = sys.stdin.readline

# N 입력
N = int(input().strip())

# 개인정보 리스트 선언
personal = []

# N개의 튜플 입력
for _ in range(N):
    attr1, attr2 = map(str, input().split())
    new_tuple = (attr1, attr2)
    personal.append(new_tuple)

personal.sort(key=lambda x: int(x[0]))

# 튜플 출력
for person in personal:
    print(*person)