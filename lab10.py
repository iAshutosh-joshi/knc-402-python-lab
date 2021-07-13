print("Lab 10 by Ashutosh Joshi")
def selection_sort(L):
    for i in range(len(L)-1):
        min_index = i
        for j in range(i+1, len(L)-1):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]

L = [41, 59, 26, 53, 59,4,6,786,33,2]
print("Original list: ",L)
selection_sort(L)
print("Sorted list: ",L)