#BUBBL SORT Time O(n^2)

A = [-5,3,2,1,-3,-3,7,2,2]

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        # If we do any changes we move the flag back to true
        for i in range(1,n):
            if arr[i-1] > arr[i]: 
                flag = True
                arr[i-1],arr[i] = arr[i], arr[-1]

bubble_sort(A) #R: [-5, -3, -3, 2, 2, 2, 2, 2, 2]

# INSERTION SORT O(n^2)
B = [-5,3,2,1,-3,-3,7,2,2]
 
def insert_sort(arr):
    n = len(arr)
    for i in range (1,n):
        for j in range (i,0,-1):
            # O in exclusive, and we are counting down 
            if arr[j-1] > arr [j]:
                arr[j-1], arr[j] = arr[j],arr[j-1] # We make the swap 
            else:
                break
insert_sort(B) #R :  [-5, -3, -3, 1, 2, 2, 2, 3, 7]


#SELECTION SORT O:(n^2)

C = [-3,3,2,1,-5,-3,7,2,2]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range (i+1,n):
            if arr[j]<arr[min_index]: #Find minimun 
                min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(C) #R: [-5, -3, 1, 2, 2, -3, 2, 3, 7]


#Merge Sort  O(n log n)

D = [-5,3,2,1,-3,-3,7,2,2]
def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr #This is base case recursion 
    m = len(arr)//2
    L = arr[:m] # Todo lo del array hasta m, sin incluir
    R = arr[m:] # Todo el resto incluyendo m 

    L = merge_sort(L)
    R = merge_sort(R)

    l,r = 0,0 #Los indices para el merge
    L_len = len(L)
    R_len = len(R)

    sorted_arr = [0]*n
    i = 0

    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
        i +=1
    
    while l < L_len:
        sorted_arr[i] = L[l]
        l +=1
        i +=1
    while r < R_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1

    return sorted_arr
merge_sort(D) #R: [-5, 3, 2, 1, -3, -3, 7, 2, 2]

