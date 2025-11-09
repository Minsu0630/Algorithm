a = input().split()
n = int(A[0])
m = int(A[1])

basket = []
for i in range(n):
    basket.append(i+1)

for i in range(m):
    m_list = input().split()
    num1 = int(m_list[0])
    num2 = int(m_list[1])

    basket[num1-1], basket[num2-1] = basket[num2-1], basket[num1-1]

for i in range(n):
    print(basket[i], end=" ")
