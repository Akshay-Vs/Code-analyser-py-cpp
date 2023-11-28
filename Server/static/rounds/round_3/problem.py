def problem(arr, n):
    for i in range(n):
        for j in range(0, n - i - 1):
             if arr[j] < arr[j + 1]:
                arr[i], arr[i + 1] = arr[j + 1], arr[j]
    return arr
