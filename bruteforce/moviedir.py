# BOJ 1436: 영화감독 숌
import sys
from math import log10, ceil
input = sys.stdin.readline

N = int(input().strip())

its = 666
counter = 1
while True:
    if counter == N:
        print(its)
        break
    
    its += 1
    if "666" in str(its):
        counter += 1