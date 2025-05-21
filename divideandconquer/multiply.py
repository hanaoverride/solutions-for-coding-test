# BOJ 1629: 곱셈
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# A, B, C 입력
A, B, C = map(int, input().split())

# A^B mod C = (A^B/2 mod C)*(A^B/2 mod C) mod C ~ log B
def f(A, B, C):
    if B == 1:
        return A % C
    temp = f(A, B//2, C) % C
    result = temp * temp % C
    if B % 2 == 1:
        result = (result * A) % C
    return result
    
print(f(A,B,C))