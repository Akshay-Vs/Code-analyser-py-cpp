### You are given an array of integers nums and an integer target. The function two_sum is supposed to find and return a pair of indices (i, j) where nums[i] + nums[j] equals the target. However, the code has logical errors. Identify and correct the errors in the code to make it work as intended. The function signature is as follows:

```py
def two_sum(nums, target):
    # Your code here
```

```py
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)
```
Expected Output: [0, 1]

Note:

- The returned list should contain the indices of the two numbers in the array nums that add up to the target.
- The input array nums is not guaranteed to be sorted.
- There is exactly one solution, and you may not use the same element twice.