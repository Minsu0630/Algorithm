import sys

def find_fraction(X):
    
    n = 1
    sum_of_terms = 0
    
    while sum_of_terms < X:
        sum_of_terms += n
        n += 1
    
    group_number = n - 1
    
    prev_sum = sum_of_terms - group_number
    
    P = X - prev_sum
    
    if group_number % 2 == 1:
        numerator = group_number - P + 1
        denominator = P
    else:
        numerator = P
        denominator = group_number - P + 1

    print(f"{numerator}/{denominator}")


try:
    X = int(sys.stdin.readline())
    find_fraction(X)
except:
    pass
