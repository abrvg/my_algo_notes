# Given two arrays already sorted
# Merge and sort them.
# Exaple input: a = [4,8], b = [6,99] 
# Output --> [4,6,8,99]

def sort_arrays(arr_1, arr_2):
    arr_3 = []
    
    n = len(arr_1) 
    m = len(arr_2)
    
    i = 0 
    j = 0 
    
    while i < n and j < m:
        
        if arr_1[i] < arr_2[j]:
            arr_3.append(arr_1[i])
            
            i += 1
        
        elif arr_2[j] <= arr_1[i]:
            arr_3.append(arr_2[j])

            j += 1

    
    return arr_3

if __name__ == "__main__":
    A = [1,3,5,7]
    B = [2,4,7,8]
    print(sort_arrays(A,B))