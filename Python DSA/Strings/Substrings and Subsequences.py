def is_subsequence(smaller, larger):
    i = 0
    j = 0

    while i < len(smaller) and j < len(larger):
        if smaller[i] == larger[j]:
            i += 1
        j += 1

    return i == len(smaller)


word = "CARPET"

sub = word[1:4]
print("Substring (index 1 to 4):", sub)

print("Is 'CRT' a subsequence of 'CARPET'?", is_subsequence("CRT", word))
print("Is 'CRT' a substring of 'CARPET'?", "CRT" in word)