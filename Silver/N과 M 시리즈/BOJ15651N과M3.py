#BOJ15649_N과M1
def nPm():
	if len(s) == M:
		print(*s)
		return
	for i in arr:
		s.append(i)
		nPm()
		s.pop()

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
s = []
nPm()