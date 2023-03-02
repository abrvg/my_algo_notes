"""
Binary search

The array were the searching will be executed should be ordered
Start looking at the midle of the array
If the middle element is the target, the searching is done
If the middle element is greater than the target, look into the begining of the array until element position -1 (repeating previous steps)
If the middle element is less than the target, look into the array from element position +1 to the end (repeating previous steps)
"""

def binary_search_iterative(array, element):
    # Time complexity : O(log(n))
    
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        print("Subarray in step {}: {}".format(step, str(array[start:end+1])))
        step = step + 1
        mid = (start + end) // 2

        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


if __name__ == "__main__":
    
    array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]       

    element = 18

    print("Searching for {} in {}".format(element, array))
    print("Index of {}: {}".format(element, binary_search_iterative(array, element)))
