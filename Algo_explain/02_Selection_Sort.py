"""
Selection sort:
Start in the first element of the array, i = 0
Find the minimum element by traversing the remaining array (starting at i+1)
Swap this minimum element with the element in i
Move to the next element and repeat the iteration

Time complexity:
    - The first iteration, in the worst case all the n-1 elements are traversed
    - The second iteration, in the worst case all the n-2 elements are traversed
    - Therefore: (n-1) + (n-2) + ... + 1 = n(n-1)/2 
    - Time complexity:  O( n^{2} )$
    - Auxiliar memory:  O( 1 )
"""

def sel_sort(arr):
    for i in range(len(arr)):
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    
    return arr

if __name__ == "__main__":
    
    arr = [3, 7, 18, 1, 8, 95, 4]
    print("Input: ", arr)
 
    result = sel_sort(arr)
    print("Sorted: ", result)
