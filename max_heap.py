def max_heapify(A,i):
    '''to hangle single violation only'''
    l = (i*2)+1
    r = (i+1)*2
    if l <= len(A) and A[l]>A[i]:
        largest = l
    else: largest = i
    if r <= len(A) and A[r]>A[i]:
        largest = r
    if largest != i:
        A[i] = A[largest]
    max_heapify(A,largest)
    return None



def build_maxheap(A):
    '''to product max heap from unordered array'''
    for i in range ((len(A)-2)//2,0,-1):
        return max_heapify(A,i)
        

def heap_sort(A):
    '''to sort a max heap'''
    ans = []
    build_maxheap(A)
    k = len(A)
    for i in range (k-1,0,-1):  #to swap the first and last element of the max heap
        swap = A[i]
        A[i] = A[0]
        A[0] = swap

        max_heapify(A,0)
    return A




#def maxheap_insert(A,k):
