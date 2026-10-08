def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        
        # Scan for the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # Place the found minimum element into its correct sorted position
        arr[i], arr[min_index] = arr[min_index], arr[i]