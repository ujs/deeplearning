def max_heapify(A,i):
    l = 2*(i+1)-1
    r = 2*(i+1)-1
    if l <= len(A) and A[l]>A[i]:
        largest = l
    else largest = A[i]
    if r <= len(A) and A[r]>A[i]:
        largest = r
    if largest != i:
        A[i] = A[largest]
        max_heapify(A,largest)





def build_maxheap(A):
    for i in range (len(A//2-1,0,-1)):
        max_heapify(A,i)




def heap_sort(A):




def maxheap_insert(A,k):
