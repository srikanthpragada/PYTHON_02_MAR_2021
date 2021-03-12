# Print frequency of each char in a string
st = "This is to test frequency of characters"

for c in sorted(set(st)):
    print(f"{c} - {st.count(c)}")