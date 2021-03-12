names = ['Anders', 'Andy', 'Scott', 'James', 'Richards']
uchars = set()

for n in names:
    uchars.update(set(n))

print(sorted(uchars))
