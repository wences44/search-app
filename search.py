import random
# Complexity is high - heavy on CPU and Memory
def linear_search(arr, target):
    """
    Perform a linear search on the given array to find the target element.

    Parameters:
    arr (list): The array to be searched.
    target: The element to be searched for.

    Returns:
    int: The index of the target element if found, -1 otherwise.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        #elif arr[i] > target:
        #    return -1
    return -1


#Low Complexity using Binary search
def binary_search(arr, target):
    """
    Perform a binary search on the given sorted array to find the target element.

    Parameters:
    arr (list): The sorted array to be searched.
    target: The element to be searched for.

    Returns:
    int: The index of the target element if found, -1 otherwise.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def generate_large_array(size):
    """
    Generate a large array of random integers.

    Args:
        size (int): The size of the array.

    Returns:
        list: A list of random integers.
    """
    return [random.randint(1, 100) for _ in range(size)]

arr = generate_large_array(1000000)
target = 42
index = linear_search(arr, target)
print("The target ",[target], " is found at index: ",[index])