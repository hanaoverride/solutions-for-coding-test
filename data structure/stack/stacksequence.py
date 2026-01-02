# BOJ 1874: 스택 수열
import sys
from collections import deque
input = sys.stdin.readline

# n 입력
n = int(input().strip())

# 수열 입력
seq = [int(input().strip()) for x in range(n)]

# 초기 변수 선언
stack = deque()
result = ""
next_num = 1
flag = True

# 순회 및 판정
for target in seq:
    # 스택에 쌓는 과정을 가상화
    while next_num <= target:
        stack.append(next_num)
        result += "+"
        next_num += 1
    # 현재 수열의 출력값을 찾으면 동일하게 pop 해가며 가상화를 진행
    if stack[-1] == target:
        stack.pop()
        result += "-"
    # 못 찾았다면 해당 수열이 만들어질 수 없음
    else:
        flag = False
        break
# 결과
if flag:
    print("\n".join(result))
else:
    print("NO")