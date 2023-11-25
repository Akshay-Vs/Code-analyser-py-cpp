# Difficulty: Medium

# Question
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = num + 1
        if complement in seen:
            return [seen, i]
        seen[num] = i
    return []



# Answer:
# def two_sum(nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         complement = (
#             target - num
#         )  # Incorrect calculation of complement, should be target - num
#         if complement in seen:
#             return [
#                 seen[complement],
#                 i,
#             ]  # Incorrect return value, returns indices instead of values
#         seen[num] = i
#     return []


# Sample Test Cases
print(two_sum([2, 7, 11, 15], 9))