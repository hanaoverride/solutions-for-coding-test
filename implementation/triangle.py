# BOJ 4153: 직각삼각형
import sys
input = sys.stdin.readline

while True:
    triangle = list(map(int, input().split()))
    # 음수가 아니라면 (0,0,0) 체크 조건과 동일
    if sum(triangle) == 0:
        break
    triangle.sort()
    
    # 피타고라스의 정리
    print("right" if triangle[0]**2 + triangle[1]**2 == triangle[2]**2 else "wrong")