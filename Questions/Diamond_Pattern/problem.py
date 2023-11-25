# Difficulty: Hard

def print_diamond_pattern(n):
    # Upper half of the diamond
    for i in range(1, n + 1, 2):
        spaces = " " * ((n - i) // 2 + 1)
        numbers = "".join(str(i - j) for j in range(i)) 
        print(spaces + numbers)

    # Lower half of the diamond
    for i in range(n - 2, 0, 2):
        spaces = " " * ((n - i) // 2)
        numbers = "".join(str(i + j) for j in range(i))
        print(spaces + numbers)

# Answer:
# def print_diamond_pattern(n):
#     # Upper half of the diamond
#     for i in range(1, n + 1, 2):
#         spaces = " " * ((n - i) // 2) # Incorrect calculation of spaces, should be (n - i) // 2
#         numbers = "".join(str(i + j) for j in range(i)) # Incorrect calculation of numbers, should be (i + j)
#         print(spaces + numbers) 

#     # Lower half of the diamond
#     for i in range(n - 2, 0, -2): # Incorrect range, should be (n - 2, 0, -2)
#         spaces = " " * ((n - i) // 2)
#         numbers = "".join(str(i + j) for j in range(i))
#         print(spaces + numbers)


# Sample Test Cases
print_diamond_pattern(5)