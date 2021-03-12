names = ['Joe', 'Jack', 'Mike', 'Tom', 'Andy']
mobiles = ['93939333', '3929929232', '484848484', '28282883', '34848383']

for name, mobile in sorted(zip(names, mobiles)):
    print(f"{name:15} {mobile}")

# customers = {}
# for name, mobile in zip(names, mobiles):
#     customers[name] = mobile
#
# for name, mobile in sorted(customers.items()):
#     print(f"{name:15} {mobile}")
