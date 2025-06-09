# BOJ 15829: Hashing
import sys
input = sys.stdin.readline

M = 1234567891

hsh = 0

L = int(input().strip())

s = list(input().strip())

for i in range(L):
    hsh = hsh*31 + ord(s[L-1-i])-ord('a')+1
    hsh %= 1234567891
    
print(hsh)