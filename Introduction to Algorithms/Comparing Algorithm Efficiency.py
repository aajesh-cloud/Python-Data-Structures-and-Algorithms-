import time
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
data = list(range(5000))
start1 = time.perf_counter()
has_duplicate_slow(data)
end1 = time.perf_counter()
start2 = time.perf_counter()
has_duplicate_fast(data)
end2 = time.perf_counter()
print("Slow approach time:", (end1 - start1) * 1_000_000, "microseconds")
print("Fast approach time:", (end2 - start2) * 1_000_000, "microseconds")