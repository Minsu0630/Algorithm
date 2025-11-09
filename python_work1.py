A = input().split()
N = int(A[0])
M = int(A[1])

basket = []
for i in range(N):
    basket.append(i+1)

for i in range(M):
    MList = input().split()
    num1 = int(MList[0])
    num2 = int(MList[1])

    basket[num1-1], basket[num2-1] = basket[num2-1], basket[num1-1]

for i in range(N):
    print(basket[i], end=" ")
