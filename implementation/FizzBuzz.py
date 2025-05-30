# BOJ 28702: FizzBuzz

import sys
input = sys.stdin.readline

DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
arr = [input().strip() for i in range(3)]

debug(arr)
def FizzBuzz(n):
    res = ""
    if n % 3 == 0:
        res += "Fizz"
    if n % 5 == 0:
        res += "Buzz"
    if n % 3 != 0 and n % 5 != 0:
        res += str(n)
    return res
for i in range(3):
    # 비둘기집 원리에 의해 셋 중 하나가 3 혹은 5의 배수가 아님이 증명됩니다.
    if arr[i].isdigit():
        print(FizzBuzz(int(arr[i]) + (3-i)))
        break