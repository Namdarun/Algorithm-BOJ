#BOJ14468_소건너간이유2_S4
#https://www.acmicpc.net/problem/14468

#겹치는 부분을 찾아준다.

import sys
input = sys.stdin.readline

arr = input()
cnt = 0

for i in range(52):
    for j in range(i+1, 52):
        if arr[i] == arr[j]:
            li = arr[i:j+1]
            for k in li:
                if li.count(k) == 1:
                    cnt += 1
            break

print(cnt // 2)