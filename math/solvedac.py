# BOJ 18110: solved.ac
import sys
input = sys.stdin.readline

n = int(input().rstrip())
if n == 0:
    print(0)
else:
    diff = [0]*31
    for _ in range(n):
        geti = int(input().rstrip())
        diff[geti] += 1
    
    p = int(0.15*n + 0.5)
    
    remove_bottom = p
    for i in range(1, 31):
        if diff[i] >= remove_bottom:
            diff[i] -= remove_bottom
            break
        else:
            remove_bottom -= diff[i]
            diff[i] = 0
    
    remove_top = p
    for i in range(30, 0, -1):
        if diff[i] >= remove_top:
            diff[i] -= remove_top
            break
        else:
            remove_top -= diff[i]
            diff[i] = 0
    
    total_sum = 0
    total_count = 0
    for i in range(1, 31):
        total_sum += i * diff[i]
        total_count += diff[i]
    
    if total_count > 0:
        avg = int(total_sum / total_count + 0.5)
    else:
        avg = 0
    
    print(avg)