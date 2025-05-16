# BOJ 1065: 한수
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# 등차수열이 성립하는 수열 preprocess
judge = [False] * 1001
for number in range(1, 1001):
    # case 1: 한자리~두자리수. 무조건 등차수열이 된다
    if 1 <= number <= 99:
        judge[number] = True
    # case 2: 두자리수. 3a + 3d라서 3의 배수이면서 증가 혹은 감소하면 성립(연산 횟수를 줄일수 있음)
    elif number >= 100 and number % 3 == 0:
        temp = list(map(int, str(number)))
        first, second, third = temp
        # 증가 or 감소
        if (third - second) == (second - first):
            judge[number] = True

# 자연수 N 입력
N = int(input())

# 결과값 출력
print(sum(judge[:(N+1)]))