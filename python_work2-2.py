N = int(input())

original_N = N
count = 0

while True:
    sum_digits = (N // 10) + (N % 10)
    new_N = (N % 10) * 10 + (sum_digits % 10)
  
    count += 1
    
    if new_N == original_N:
        break
        
    N = new_N

print(count)
