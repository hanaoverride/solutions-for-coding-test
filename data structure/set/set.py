# BOJ 11723: 집합
import sys
input = sys.stdin.readline

# 명령의 수 M 입력
M = int(input().strip())

# 공집합 S 선언
S = set()

# 명령 입력
for _ in range(M):
    command = input().split()
    
    # add, remove, check, toggle
    if len(command) == 2:
        cmd, val = command
        val = int(val)
        if cmd == 'add':
            S.add(val)
        elif cmd == 'remove':
            S.discard(val)
        elif cmd == 'check':
            print(int(val in S))
        elif cmd == 'toggle':
            if val in S:
                S.remove(val)
            else:
                S.add(val)
    # all, empty
    elif len(command) == 1:
        if command[0] == 'all':
            S = set([i for i in range(1, 21)])
        elif command[0] == 'empty':
            S = set()