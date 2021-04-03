try:
    f = open(r"d:\classroom\mar2\text.txt", "rt")
    words = []
    for line in f.readlines():
        words.extend(line.strip().split(" "))

    wordfreq = {}
    for w in set(words):
        wordfreq[w] = words.count(w)

    for w, c in sorted(wordfreq.items()):
        print(f"{w:20} {c:3}")

    f.close()
except Exception as ex:
    print("Error :", ex)
    exit()
