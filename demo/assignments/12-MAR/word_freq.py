# Print frequency of each char in a string
st = "This is to test frequency of words. This is different from char frequency."
words = st.split(" ")

for word in sorted(set(words)):
    print(f"{word} - {words.count(word)}")