# Test insertionSort() function
from mergeSort import *

# Test input 1
test_list = [16,21,11,8,12,22]
print("Unsorted list is: {}\n".format(test_list)) # Print unsorted list first

# Get sorted list calling mergeSort() function
mergeSort(test_list)
print ("Sorted list is: {}\n".format(test_list))