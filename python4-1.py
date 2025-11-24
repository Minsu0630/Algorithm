N, B = map(int, input().split())

system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

while N > 0:
    remainder = N % B    
    N = N // B             
    result += system[remainder]

print(result[::-1])
