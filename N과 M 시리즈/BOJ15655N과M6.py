#BOJ15655_N과M6_S3
#https://www.acmicpc.net/problem/15655

def nPm(start):
	if len(s) == M:
		print(*s)
		return
	# 중복없이 
	for i in range(start, N):
		if arr[i] not in s:
			s.append(i)
			nPm(i+1)
			s.pop()

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
s = []
nPm(0)