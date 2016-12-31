# given an array and a key
# find the index of the first occurrence of k in array
import sys
from problem0 import binary_search

def test_index1 ():
    assert (find_first_index([0,1,2,2,3,4,5,6,7,8,9],2) == 2)

def test_index2 ():
    assert (find_first_index([2,2,2,2,2,2,2],2) == 0)

def find_first_index (_arr, _k):
    while (True):
        index_1 = binary_search (_arr,_k)

        # there is no k in the array
        # or the first element
        if (index_1 <= 0):
            return index_1
        # if the previous element is different
        # i.e. we found the first occurrence
        if _arr[index_1] != _arr[index_1 - 1]:
            return index_1
        _arr = _arr[0:index_1-1]

if __name__ == "__main__":
    if (len(sys.argv) == 3):
        _arr = sys.argv[1]
        _k = sys.argv[2]
        _arr = [int(x) for x in _arr.split(',')]
        _k = int (_k)
        print (find_first_index(_arr,_k))