# def max_heapify(arr, heap_size,i):
#     left = 2*i+1
#     right = 2*i+2
#     largest = i
#     if arr[i] < arr[left] and left < heap_size:
#         largest = left
#     if arr[i] <arr[right] and right < heap_size:
#         largest = right
#     if i != largest:
#         arr[i],arr[largest] = arr[largest], arr[i]
#         max_heapify(arr,heap_size,largest)
# def build_heap(arr):
#     heap_size = len(arr)
#     for i in range(heap_size//2, -1,-1):
#         max_heapify(arr,heap_size,i)
# def heap_sort(arr):
#     heap_size = len(arr)
#     build_heap(arr)
#     for i in range(heap_size-1,-1,-1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heap_size -= 1
#         max_heapify(arr,heap_size, 0)      
#     return arr
# numbers = [6,5,3,1,7,2,4]
# print(heap_sort(numbers))
def max_heapify(A, heap_size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and A[left] > A[largest]:
        largest = left
    if right < heap_size and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, heap_size, largest)

def build_heap(A):
    heap_size = len(A)
    for i in range (heap_size,-1,-1):
        max_heapify(A,heap_size, i)
    return A

def heapsort(A):
    heap_size = len(A)
    build_heap(A)
    for i in range(heap_size-1,0,-1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, heap_size, 0)

A = [2,8,1,4,14,7,16,10,9,3]
build_heap(A)
print(A)
