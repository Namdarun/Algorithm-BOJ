#BOJ28074_모비스_B4
#https://www.acmicpc.net/problem/28074

# def check(arr):
#     word = 'MOBIS'
#     for i in arr:
#         if i not in word:
#             return False
#         arr = arr.replace(i, '', 1)
#     return True

# check_string = input()
# checking = check(check_string)
# print('YES' if checking else 'NO')

word = input()
arr = list(set(word))
# print(arr)
if arr.count('M')+arr.count('O')+arr.count('B')+arr.count('I')+arr.count('S') == 5:
    print('YES')
else:
    print('NO')