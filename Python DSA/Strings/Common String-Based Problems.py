def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    counts = {}

    for c in s1:
        counts[c] = counts.get(c, 0) + 1
    for c in s2:
        counts[c] = counts.get(c, 0) - 1

    return all(count == 0 for count in counts.values())


def first_non_repeating_char(s):
    counts = {}

    for c in s:
        counts[c] = counts.get(c, 0) + 1

    for c in s:
        if counts[c] == 1:
            return c

    return None


print("Are 'listen' and 'silent' anagrams?", are_anagrams("listen", "silent"))

word = "swiss"
result = first_non_repeating_char(word)
print(f"First non-repeating character in '{word}':", result)