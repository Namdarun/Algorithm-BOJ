#BOJ15654_N과M5.py
#https://www.acmicpc.net/problem/15654

def nPm():
	if len(s) == M:
		print(*s)
		return
	# 중복없이 
	for i in arr:
		if i in s:
			continue
		else:
			s.append(i)
			nPm()
			s.pop()

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
s = []
nPm()