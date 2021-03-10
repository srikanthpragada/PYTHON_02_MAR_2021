# Print even numbers first and then odd numbers 
evens = []
odds = []

while True:
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break

    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

for n in evens + odds:
    print(n)
