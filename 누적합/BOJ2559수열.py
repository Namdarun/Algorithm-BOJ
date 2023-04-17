import sys
input = sys.stdin.readline

n, k = map(int, input().split())
suyeol = list(map(int, input().split()))

hap=check_hap=sum(suyeol[:k])

for i in range(k,n):
    hap = hap+suyeol[i]-suyeol[i-k]
    check_hap=max(hap, check_hap)

print(check_hap)