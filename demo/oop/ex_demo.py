
try:
    num = int(input("Enter number :"))
    print(100 / num)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Zero is not a valid number")

print("The End!")