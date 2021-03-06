# Calculate Net Amount
price = int(input("Enter price :"))
qty = int(input("Enter qty :"))

amount = price * qty

if qty > 3:
    amount *= 0.60
elif qty > 2:
    amount *= 0.70
else:
    amount *= 0.90

print(f"Net Amount = {amount}")