def counting_sort(arr, max_val):
    n = len(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    output = [0] * n
    for i in range(n - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output


scores = [78, 45, 92, 45, 60, 78, 100]
print(counting_sort(scores, 100))