#Difficulty: Easy

# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n):  # Incorrect range in outer loop
#         for j in range(0, n - i - 1):  # Incorrect range in inner loop
#             if arr[j] > arr[j + 1]:  # Incorrect condition for swapping
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Sample Test Cases
# arr = [5, 1, 4, 2, 8]
# bubble_sort(arr)
# print(arr)  # Should print [1, 2, 4, 5, 8]