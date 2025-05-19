# BOJ 2609번: 최대공약수와 최소공배수

# 디버그 함수 생성
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# gcd, lcm 함수 정의
# 1. gcd = gcd(a,b) = gcd(b, a%b) recursion~
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
#2. gcd*lcm = a*b로부터 lcm = a*b/gcd
def lcm(a,b):
    return a * b // gcd(a,b)

# 두 자연수 입력
n1, n2 = map(int, input().split())

# 각 경우 출력
print(gcd(n1, n2))
print(lcm(n1, n2))