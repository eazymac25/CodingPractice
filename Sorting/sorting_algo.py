

def heapify(a, n, i):
  """
  :param a: an array - imgaine it is a heap :)
        1
      /   \
     2     4
    / \   / \
   5   6 9   8

   :param n: the size of the heap (lenght of array)
   :param i: the starting index to heapfiy from
   :return: void method there is no return
   it eidts this array inline
  """
  largest = i
  left = 2*i + 1
  right = 2*i + 2
  
  if left < n and a[left] < a[i]:
    largest = left
  
  if right < n and a[right] < a[largest]:
    largest = right
    
  if largest != i:
    a[i], a[largest] = a[largest], a[i]
    heapify(a, n, largest)
    
def heap_sort(a):
  """
  sort the array a using the heap sort method
  :param a (list): an array of numerical types float, int, long, etc
  :return (list): sorted array
  """
  n = len(a)
  # initialize the heap
  # keep in mind the heapify method
  # must be a min heap if sorting from low to high
  for i in range(n, -1, -1):
    heapify(a, n, i)
  
  # for 
  for i in range(n-1, 0, -1):
    a[i], a[0] = a[0], a[i]
    heapify(a, i, 0)
  return arr

arr = [ 12, 11, 13, 5, 6, 7]
print(arr)
heap_sort(arr)
print(arr)

def partition(arr, begin, end):
  pivot = begin
  for i in xrange(begin+1, end+1):
    if arr[i] <= arr[begin]:
      pivot += 1
      arr[i], arr[begin] = arr[begin], arr[i]
  arr[i], arr[pivot] = arr[pivot], arr[i]
  return pivot


def quicksort(arr, begin=0, end=None):
  if not end:
    end = len(arr)

  def _quicksort(arr, begin, end):
    if begin >= end:
      return
    pivot = parition(arr, begin, end)
    _quicksort(arr, begin, pivot-1)
    _quicksort(arr, pivot+1, end)
  return _quicksort(arr, begin, end)

