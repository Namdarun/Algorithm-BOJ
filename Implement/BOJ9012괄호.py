#BOJ9012_괄호
T = int(input())

#체크할 변수
for i in range(T):
    gwal = input()
    check = 0

#인풋의 하나씩 보면서
    for j in gwal:
        if j == "(":
            check += 1
        elif j == ")":
            check -= 1
            
        if check < 0:
            break
    
#입력할때마다 체크하기
    if check == 0:
        print("YES")
    else:
        print("NO")