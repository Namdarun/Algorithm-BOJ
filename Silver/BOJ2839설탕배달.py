#BOJ2839_설탕배달
#1번 답
N = int(input())
count = 0
#N이 0보다 크거나 같은 동안
while N >= 0:
    #5로 정확히 떨어지면 그 값을 도출하고 
    # 그 전까지 3씩 빼주면서 count를 세준다
    # 3씩 빼주면서 5로 정확히 떨어지면 그 값을 도출한다.
    if N % 5 == 0:
        
        count += (N // 5)
        print(count)
        break
    N -= 3
    count += 1

else:
    print(-1)

#2번 답
N = int(input())
#나머지가 0이면 몫 도출
if N % 5 == 0:
    print(N//5)

#그 외
else:
    count = 0
    #3씩 줄여나가면서 5로나눌때 나머지가 0이면 몫이랑 3씩 뺐을때 더해준값 합쳐서 도출
    #1이나 2면 불가
    #0이 되면 count만 도출
    while N > 0:
        N -= 3
        count += 1
        if N % 5 == 0: 
            count += (N//5)
            print(count)
            break

        elif N == 1 or N == 2:
            print('-1')
            break

        elif N == 0:
            print(count)
            break


