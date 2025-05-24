# BOJ 2164: 카드2
import sys
from collections import deque
input = sys.stdin.readline

# N 입력
N = int(input().strip())

# deque 사용
card = deque([i for i in range(1, N+1)])

# 카드가 빌때까지 동작 반복
while True:
    temp = card.popleft()
    if not card:
        print(temp)
        break
    card.append(card.popleft())