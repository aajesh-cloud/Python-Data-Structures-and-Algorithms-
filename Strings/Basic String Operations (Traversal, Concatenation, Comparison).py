first = "Ananya"
second = "Karan"

# Traversal
print(f"Traversing '{first}': ", end="")
for char in first:
    print(char, end=" ")
print()

# Concatenation
full_team_name = first + " & " + second
print("Concatenated:", full_team_name)

# Comparison
if first < second:
    print(f"{first} comes before {second}")
else:
    print(f"{second} comes before {first}")