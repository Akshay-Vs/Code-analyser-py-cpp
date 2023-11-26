def problem(arr, args):
    n = len(arr)

    for i in range(n):  # Incorrect range in outer loop
        for j in range(0, n - i - 1):  # Incorrect range in inner loop
             if arr[j] > arr[j + 1]:  # Incorrect condition for swapping
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
