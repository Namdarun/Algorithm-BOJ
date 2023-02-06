#BBOJT11721_열개씩끊어 출력
arr = input()

for i in range(0, len(arr)+1, 10):
    print(arr[i:i+10])

    