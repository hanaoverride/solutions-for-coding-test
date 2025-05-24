# BOJ 10828: 스택
import sys
from collections import deque
input = sys.stdin.readline

# 명령의 수 N 입력
N = int(input().strip())

# 스택 선언
stack = deque()

for _ in range(N):
    # 입력 갯수에 따른 분기
    command = input().split()
    # pop, size, empty, top
    if len(command) == 1:
        if command[0] == 'pop':
            print(stack.pop() if stack else -1)
        elif command[0] == 'size':
            print(len(stack))
        elif command[0] == 'empty':
            print(int(len(stack) == 0))
        elif command[0] == 'top':
            print(stack[-1] if stack else -1)
    # push X
    elif len(command) == 2:
        element = int(command[1])
        stack.append(element)