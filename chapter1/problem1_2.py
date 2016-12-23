# given an array and a key
# find the index of the first occurrence of k in array

from problem0 import binary_search

def test_index1 ():
    assert (find_first_index([0,1,2,2,3,4,5,6,7,8,9],2) == 2)

def find_first_index (_arr, _k):
    index_1 = binary_search (_arr,_k)
    return binary_search(_arr[0:(index_1+1)],_k)

if __name__ == "__main__":
    print()