def max_window_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum


daily_sales = [120, 90, 150, 200, 80, 60, 175, 300]
k = 3

best = max_window_sum(daily_sales, k)
print(f"Best {k}-day total: {best}")