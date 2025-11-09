pay = 1000

try:
    price = int(input())
except ValueError:
    print("잘못된 입력입니다.")
    exit()

change = pay - price
moneys = [500, 100, 50, 10, 5, 1]
total_count = 0

for money in moneys:
    count = change // money
    total_count += count
    change %= money 
    if change == 0:
        break

print(total_count)
