# BOJ 4949: 균형잡힌 세상
import sys
import re
input = sys.stdin.readline

result = []
while True:
    line = input().rstrip()
    if line == '.':
        break
    
    line = re.sub(r'[^()\[\]]', '', line)
    
    stack = []
    balanced = True
    
    for char in line:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                balanced = False
                break
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                balanced = False
                break
            stack.pop()
    if balanced and not stack:
        result.append('yes')
    else:
        result.append('no')
print(*result, sep='\n')
