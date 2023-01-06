#BOJ10817_세 수
li = list(map(int, input().split()))
li.sort()
print(li[1])

#숏코딩
print(sorted(input().split(),key=int)[1])