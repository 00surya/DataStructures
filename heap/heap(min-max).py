arr = [23,1,2,56,4]

############### max heap ################

def max_heap(arr):
    heap_size = len(arr)-1
    for i in range(heap_size,-1,-1):
        max_heapify(arr,i)    




def max_heapify(arr,i):
    L = 2*i
    R = 2*i + 1
    heap_size = len(arr) - 1
    if L <= heap_size and arr[L] > arr[i]:
            largest = L
    else:
        largest = i
    if R <= heap_size and arr[R] > arr[largest]:
        largest = R
    
    if largest != i:
        exchange(arr,i,largest)
        max_heapify(arr,largest)

################################################################


############# min heap ###################

def min_heap(arr):
    heap_size = len(arr)-1
    for i in range(heap_size,-1,-1):
        min_heapify(arr,i)    


def min_heapify(arr,i):
    L = 2*i
    R = 2*i + 1
    heap_size = len(arr) - 1
    if L <= heap_size and arr[L] < arr[i]:
            smallest = L
    else:
        smallest = i
    if R <= heap_size and arr[R] < arr[smallest]:
        smallest = R
    
    if smallest != i:
        exchange(arr,i,smallest)
        min_heapify(arr,smallest)
    
################################################################


##### utility exchange funtion #####

def exchange(arr,i,j):
    elem_j = arr[j]
    arr[j] = arr[i]
    arr[i] = elem_j
    return

###################################



# max_heap(arr)
# print(arr)
# min_heap(arr)
# print(arr)
