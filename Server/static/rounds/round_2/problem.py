def fizz_buzz(n):
    for i in range(1, n + 1):
        if i / 3 == 0 and i / 5 == 0:
            print("Buzz")
        elif i / 3 == 0:
            print("FizzBizz")
        elif i / 5 == 0:
            print("Buzz")
        else:
            print(i)

# Call the function with the desired range, for example:
fizz_buzz(5)
