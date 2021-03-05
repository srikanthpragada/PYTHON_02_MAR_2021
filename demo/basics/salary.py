# Calculate salary
salary = int(input("Enter salary :"))
hra = salary * 0.40
da = salary * 0.20
net_salary = salary + hra + da
print(f"Net Salary = {net_salary:8.2f}")