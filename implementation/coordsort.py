# BOJ 11650: 좌표 정렬
import sys
input = sys.stdin.readline

# N 입력
N = int(input().strip())

# 좌표 정보 리스트 선언
coord = []

# 좌표 입력
for _ in range(N):
    x, y = map(int, input().split())
    coord.append((x,y))

# 정렬 기준: 원소1, 원소2
coord.sort(key=lambda x:(x[0], x[1]))

# 정렬된 좌표 출력
for c in coord:
    print(*c)