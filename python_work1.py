A = input().split()
N = int(A[0])
M = int(A[1])

basket = []
for i in range(N):
    basket.append(i+1)

for i in range(M):
    Mlist = input().split()
    num1 = int(Mlist[0])
    num2 = int(Mlist[1])

    basket[num1-1], basket[num2-1] = basket[num2-1], basket[num1-1]

for i in range(N):
    print(basket[i], end=" ")
