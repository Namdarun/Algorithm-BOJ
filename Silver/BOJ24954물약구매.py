#BOJ24954물약구매_못풂
N = int(input())
price = list(map(int, input().split()))
for _ in range(N):
    dc = int(input())
    if dc == 0:
        continue
    else:
        for i in range(dc):
            dc_arr, dc_value = map(int, input().split())
        
result = float("inf")