def has_duplicate_slow(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
def has_duplicate_fast(arr):
    seen = set()
    for value in arr:
        if value in seen:
            return True
        seen.add(value)
    return False
data = [4, 2, 7, 9, 2, 5]
print("Slow check:", "Duplicate found" if has_duplicate_slow(data) else "No duplicate")
print("Fast check:", "Duplicate found" if has_duplicate_fast(data) else "No duplicate")