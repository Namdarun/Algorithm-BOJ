#BOJ2816_디지털티비_B1
#https://www.acmicpc.net/problem/2816

n = int(input())
arr = []
for i in range(n):
    cha = input()
    if cha == 'KBS1':
        check1 = i
    elif cha == 'KBS2':
        check2 = i
    arr.append(cha)

result = ''
result += '1'*check1
result += '4'*check1
if check1 > check2:
    check2 += 1
result += '1'*check2
result += '4'*(check2-1)
print(result)
