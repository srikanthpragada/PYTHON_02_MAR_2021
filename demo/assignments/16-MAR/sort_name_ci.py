def trim(n):
    return n.strip().upper()


names = ['Java', '  python', '  C', 'C++', 'TypeScript', 'JavaScript  ']

for n in sorted(names, key=trim):
    print(n)

for n in sorted(names, key=lambda s: s.upper()):
    print(n)
