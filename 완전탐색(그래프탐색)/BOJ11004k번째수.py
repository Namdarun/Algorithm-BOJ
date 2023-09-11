#BOJ11004_K번째수_S4
#https://www.acmicpc.net/problem/11004

#퀵정렬로도 풀어보기 

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(arr[k-1])