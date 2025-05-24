# BOJ 1259: 팰린드롬수
import sys
input = sys.stdin.readline

# EOF까지 입력
while True:
    num = input().strip()
    # 종료조건
    if num == '0':
        break
    # 파이썬 슬라이싱: num[시작:끝:단계]
    print("yes" if num == num[::-1] else "no")