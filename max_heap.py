def max_heapify(A,i):
    '''to hangle single violation only'''
    l = (i*2)+1
    r = (i+1)*2
    largest = i
    if l < len(A) and A[l]>A[i]:
        largest = l
    if r < len(A) and A[r]>A[l]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A,largest)




def build_maxheap(A):
    '''to product max heap from unordered array'''
    for i in range ((len(A)-2)//2,-1,-1):
        max_heapify(A,i)
    return A


def heap_sort(A):
    '''to sort a max heap'''
    build_maxheap(A)
    end = len(A)
    ans = []
    for i in range (end-1,-1,-1):  #to swap the first and last element of the max heap
        A[0],A[i] = A[i], A[0]
        ans.append(A[i])
        A = A[:-1]

        max_heapify(A,0)
    return ans




#build_maxheap([4,1,3,2,16,9,10,14,8,7])


#def maxheap_insert(A,k):
