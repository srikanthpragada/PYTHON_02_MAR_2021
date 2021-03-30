try:
    num = int(input("Enter number :"))
    print(100 / num)
except ValueError as ex:
    print(ex)
finally:
    print("Over")

print("The End!")
