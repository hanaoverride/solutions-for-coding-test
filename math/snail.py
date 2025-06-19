import sys
input = sys.stdin.readline
from math import ceil

A, B, V = map(int, input().split())

print(1 if A >= V else ceil((V - A) / (A - B)) + 1)