def problem(arr, args):  # do not edit this line
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


"""
In the provided Python code, the function problem is intended to implement the Bubble Sort algorithm. However, it's not sorting the array correctly

Hint: The problem is in the for loop,  The issue lies in the line where elements are being swapped
"""
