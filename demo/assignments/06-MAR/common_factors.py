# Common factors of two numbers
num1 = 200
num2 = 450

small = num1 if num1 < num2 else num2 # Smallest of two numbers

for i in range(2, small // 2 + 1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
