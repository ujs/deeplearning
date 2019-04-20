def max_heapify(A,i):
    '''to hangle single violation only'''
    l = 2*(i+1)-1
    r = 2*(i+1)-1
    if l <= len(A) and A[l]>A[i]:
        largest = l
    else largest = A[i]
    if r <= len(A) and A[r]>A[i]:
        largest = r
    if largest != i:
        A[i] = A[largest]
        retrun max_heapify(A,largest)



def build_maxheap(A):
    '''to product max heap from unordered array'''
    for i in range (len(A//2-1,0,-1)):
        ans = max_heapify(A,i)
        return ans


def heap_sort(A):
    '''to sort a max heap'''
    ans = []
    build_maxheap(A)
    k = len(A)
    for i in range (k-1,0,-1):  #to swap the first and last element of the max heap
        swap = A[i]
        A[i] = A[0]
        A[0] = swap
        ans.append(A[i])

        max_heapify(A,0)
        return ans




#def maxheap_insert(A,k):
