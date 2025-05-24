# BOJ 11050: 이항계수 1
import sys
input = sys.stdin.readline

# N, K 입력
N, K = map(int, input().split())

# B(N, K) = N!/(K!*(N-K)!) or, Base/K!, where Base = Permutaion(N,K)

# Base, Factorial 정의
def Base(N, K):
    result = 1
    
    for i in range(K):
        result *= N-i
    
    return result
    
def factorial(n):
    result = 1
    
    for i in range(n, 0, -1):
        result *= i
    
    return result
    
# 값 출력
print(Base(N, K)//factorial(K))
    