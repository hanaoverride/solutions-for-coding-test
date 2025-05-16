# BOJ 2750: 수 정렬하기
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        

# N 입력
N = int(input())

# 배열 생성
numbers = [0]*N

# 수 입력
for i in range(N):
    numbers[i] = int(input())
    
# 정렬
numbers.sort()

# 출력
for num in numbers:
    print(num)