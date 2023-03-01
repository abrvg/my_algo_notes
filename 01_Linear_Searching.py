"""
In linear searching, each element is traversed until find the selected one
"""

def LinSearch(arr, key):
    
    #Time complexity O(n)
    
    for i in range(len(arr)):
        if (arr[i] == key):
            return i
    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    key = 10
 
    result = LinSearch(arr, key)
    if(result == -1):
        print("Element not found")
    else:
        print(f"Element {key} found at index {result}")
