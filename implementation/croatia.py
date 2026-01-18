# BOJ 2941: 크로아티아 알파벳

import sys

input = sys.stdin.readline

pattern_2 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
pattern_3 = ['dz=']

gets = list(input().strip())
res = 0

for l in range(3,1,-1):
    ptr = 0
    while True:
        if ptr >= len(gets):
            break
        pattern = pattern_2 if l == 2 else pattern_3
        for p in pattern:
            slc = ''.join(gets[ptr:ptr+l])
            if slc == p:
                for j in range(l):
                    del gets[ptr]
                gets.insert(ptr, '.')
                res += 1
        ptr += 1
print(len(gets))
        