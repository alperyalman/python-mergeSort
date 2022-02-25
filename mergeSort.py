# Merge sort algotihm

def mergeSort(input_list):
    
    if len(input_list) > 1: # Check the list length
        idx_mid = len(input_list) // 2 # Cut the list 
        left = input_list[:idx_mid] # Left half of the list
        right = input_list[idx_mid:] # Right half of the list

        # Call sort algorithm for each half recursively 
        mergeSort(left) # Continue cutting left half
        mergeSort(right) # Continue cutting right half

        # ıteration indices for the left and right elements
        idx_left = 0 # Index for the left half
        idx_rigth = 0 # Index for the right half
        
        # Iterator for the main list
        idx_list = 0
        
        while idx_left < len(left) and idx_rigth < len(right):
            # Check if the left value is smaller than the right one
            if left[idx_left] <= right[idx_rigth]:
                input_list[idx_list] = left[idx_left]
                idx_left += 1
            else:
                input_list[idx_list] = right[idx_rigth]
                idx_rigth += 1
            
            idx_list += 1

        # Assign remaining values after comparison
        while idx_left < len(left):
            input_list[idx_list] = left[idx_left]
            idx_left += 1
            idx_list += 1

        while idx_rigth < len(right):
            input_list[idx_list]=right[idx_rigth]
            idx_rigth += 1
            idx_list += 1