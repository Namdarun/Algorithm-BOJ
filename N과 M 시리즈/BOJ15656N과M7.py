#BOJ15656_N과M7.py
#https://www.acmicpc.net/problem/15656

def nPm():
	if len(s) == M:
		print(*s)
		return
	# 중복가능
	for i in arr:
		s.append(i)
		nPm()
		s.pop()

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
s = []
nPm()