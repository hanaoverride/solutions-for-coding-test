# BOJ 4673: 셀프 넘버
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# 에라토스테네스의 체를 응용하자(O(n) ~ nloglogn)
mesh = [True] * 10001

# 함수 d(n) 정의
def d(n):
    result = n
    while n > 0:
        result += n % 10
        n = n // 10
    return result

# 에라토스테네스의 체 알고리즘 시작
for i in range(1, 10001):
    # 체크되어있지 않다면
    if mesh[i]:
        checker = d(i)
        # 체크 시작
        while checker <= 10000:
            mesh[checker] = False
            checker = d(checker)

# 에라토스테네스의 체 출력
for i in range(1, 10001):
    if mesh[i]:
        print(i)