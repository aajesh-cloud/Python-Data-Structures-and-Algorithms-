greeting = "Hi"

print("Characters typed:", len(greeting))
print("Python strings track length directly, no stop character needed.")

# Demonstrating the underlying byte values for comparison
encoded = greeting.encode('utf-8')
print("Encoded bytes:", list(encoded))