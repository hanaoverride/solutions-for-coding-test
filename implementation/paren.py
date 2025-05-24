# BOJ 9021: 괄호
import sys
input = sys.stdin.readline

# 테스트 케이스 T 입력
T = int(input().strip())

# 테스트케이스만큼 검사
for _ in range(T):
    paren = input().strip()
    
    count = 0
    for c in paren:
        # 각 괄호에 대해, count > 0 유지
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        # 이상한 문자
        else:
            count = -1
            break
        # 닫는 괄호가 더 많아지면
        if count < 0:
            break
    print("YES" if count == 0 else "NO")