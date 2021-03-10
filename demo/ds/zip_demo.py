
versions = [15, 3.9, 10]
langs = ['Java', 'Python', 'C#','TypeScript']
#
# for idx,v in enumerate(langs):
#     print(f"{v:10} {versions[idx]:5}")

for n,v in zip(langs,versions):
    print(f"{n:10} {v:5}")

