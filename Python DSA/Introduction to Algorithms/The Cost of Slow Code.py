import time
def has_duplicate_slow(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
def has_duplicate_fast(arr):
    seen = set()
    for val in arr:
        if val in seen:
            return True
        seen.add(val)
    return False
arr = list(range(20000))
start1 = time.time()
has_duplicate_slow(arr)
end1 = time.time()
start2 = time.time()
has_duplicate_fast(arr)
end2 = time.time()
print(f"Slow approach: {(end1 - start1) * 1000:.2f} ms")
print(f"Fast approach: {(end2 - start2) * 1000:.2f} ms")