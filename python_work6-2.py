words = [input(), input(), input()]

next_num = 0

for i in range(3):
    if words[i] != "Fizz" and words[i] != "Buzz" and words[i] != "FizzBuzz":
        next_num = int(words[i]) + (3 - i)
        break

if next_num % 15 == 0:
    print("FizzBuzz")
elif next_num % 3 == 0:
    print("Fizz")
elif next_num % 5 == 0:
    print("Buzz")
else:
    print(next_num)
