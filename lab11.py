print("Lab 11 by Ashutosh Joshi")
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


L = [41, 59, 26, 53, 59,4,6,786,33,2]
print("Original list: ",L)
insertionSort(L)
print("Sorted list: ",L)