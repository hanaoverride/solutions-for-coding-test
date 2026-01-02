# BOJ 10773: 제로
import sys
input = sys.stdin.readline

K = int(input().strip())
stack = []
for _ in range(K):
    geti = int(input().strip())
    if geti != 0:
        stack.append(geti)
    else:
        stack.pop()
print(sum(stack))