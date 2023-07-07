#BOJ5355_화성수학_B2
#https://www.acmicpc.net/problem/5355

n = int(input())

for i in range(n):
    arr = list(input().split())
    # arr = list(map(str, input().split()))
    #수식
    arr_num = float(arr.pop(0))
    # arr_num = arr[0]
    for i in range(len(arr)):
        if arr[i] == '@':
            arr_num *= 3
        elif arr[i] == '%':
            arr_num += 5
        elif arr[i] == '#':
            arr_num -= 7
    
    print("{:.2f}".format(arr_num))