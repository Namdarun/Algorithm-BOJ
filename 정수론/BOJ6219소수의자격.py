#BOJ6219_소수의자격_S3
#https://www.acmicpc.net/problem/6219

a, b, c = map(int, input().split())

count = 0
for i in range(a, b+1):
    for j in range(2, i+1):
        if i % j == 0: 
            if i == j:
                if c in list(str(j)):
                    count += 1
                # if j in 
            break
                # if c in str(i):
                #     count += 1
print(count)