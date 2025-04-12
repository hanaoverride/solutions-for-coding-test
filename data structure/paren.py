# 프로그래머스 레벨 2: 올바른 괄호
from collections import deque
def solution(s):
    # 스택을 통해 괄호 맞추기
    stack = deque()
    
    # 각 문자에 대해 순서대로
    for char in s:
        # 여는 괄호는 스택에
        if char == '(':
            stack.append(char)
        # 닫는 괄호는 top값과 매치
        elif char == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    # 여는 괄호가 너무 많으면 틀린 괄호다.
    if len(stack) > 0:
        return False
    # 모든 조건을 통과했다면, 맞는 괄호다.
    return True