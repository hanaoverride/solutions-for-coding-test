# BOJ 1316: 그룹 단어 체커
import sys
input = sys.stdin.readline

N = int(input().strip())
res = 0

for i in range(N):
    hmap = [False] * 26
    flag = False
    prev = '-'
    gets = input().strip()
    for c in gets:
        if prev != c:
            if hmap[ord(c) - 97]:
                flag = True
                break
            prev = c
            hmap[ord(c) - 97] = True
    res += int(not flag)

print(res)