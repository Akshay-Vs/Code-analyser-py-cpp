def problem(arr, args):
    if not arr:
        return None
    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element
    return max_element

print(problem([1,2,5,4,6,7], 0))