# BOJ 10845: 큐
import sys
from collections import deque
input = sys.stdin.readline

# 명령의 수 N 입력
N = int(input().strip())

# 큐 선언
queue = deque()

for _ in range(N):
    # 입력 갯수에 따른 분기
    command = input().split()
    # pop, size, empty, front, back
    if len(command) == 1:
        if command[0] == 'pop':
            print(queue.popleft() if queue else -1)
        elif command[0] == 'size':
            print(len(queue))
        elif command[0] == 'empty':
            print(int(len(queue) == 0))
        elif command[0] == 'front':
            print(queue[0] if queue else -1)
        elif command[0] == 'back':
            print(queue[-1] if queue else -1)
    # push X
    elif len(command) == 2:
        element = int(command[1])
        queue.append(element)