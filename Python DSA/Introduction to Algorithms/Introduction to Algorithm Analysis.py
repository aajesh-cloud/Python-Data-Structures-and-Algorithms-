def linear_search_with_count(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            print("Found at index", i)
            print("Comparisons made:", comparisons)
            return i
    print("Not found")
    print("Comparisons made:", comparisons)
    return -1
marks = [56, 78, 90, 43, 67, 82, 71]
linear_search_with_count(marks, 67)
linear_search_with_count(marks, 100)