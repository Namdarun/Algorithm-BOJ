#BOJ10867_중복빼고정렬_S5
#https://www.acmicpc.net/problem/10867

import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
new_li = set(li)
sorted_li = sorted(new_li)
for i in sorted_li:
    print(i, end=' ')