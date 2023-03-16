#BOJ1021_회전하는큐_S3

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
where = list(map(int, input().split()))
q = deque([i for i in range(1, n+1)])

count = 0
for idx in where:
    while True:
        if q[0] == idx:
            q.popleft()
            break
        else:
            if q.index(idx) < len(q)/2:
                while q[0] != idx:
                    q.append(q.popleft())
                    count += 1
            else:
                while q[0] != idx:
                    q.appendleft(q.pop())
                    count += 1
print(count)