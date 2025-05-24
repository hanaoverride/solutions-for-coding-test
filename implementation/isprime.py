# BOJ 1978: 소수 찾기
import sys
input = sys.stdin.readline

# N 입력
N = int(input().strip())

# 결과값 정의
result = 0

# 소수판정 함수 정의
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
    
# 숫자 리스트 입력
num_list = list(map(int, input().split()))

for num in num_list:
    result += is_prime(num)

# 결과값 출력
print(result)