#BOJ4153_직각삼각형_B3
#https://www.acmicpc.net/problem/4153

while True:
    arr = list(map(int, input().split()))
    max_num = max(arr)
    if sum(arr) == 0:
        break
    arr.remove(max_num)
    if arr[0]**2 + arr[1]**2 == max_num**2:
        print('right')
    else:
        print('wrong')