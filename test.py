def duplicate_encode(word):
    new = word
    for wd in word:
        for nw in new:
            if wd == nw:
                return print(")")
            else:
                return print("(")


duplicate_encode("bun")