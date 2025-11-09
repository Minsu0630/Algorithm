pay = 1000
price = int(input())

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
