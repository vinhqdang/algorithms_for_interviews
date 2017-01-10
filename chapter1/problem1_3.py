# given a sorted array and a key 
# find the first occurrence that larger than k
# return -1 if there is no such element

from problem0 import binary_search

def test_find_first_larger_1 ():
    assert (find_first_larger([1,2,3,4,5,5,6],7) == -1)

def test_find_first_larger_2 ():
    assert (find_first_larger([1,2,3,4,5,6,7,8],4) == 3)

def test_find_first_larger_3 ():
    assert (find_first_larger([1,2,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,6,7,8],4) == 3)

def test_find_first_larger_4 ():
    assert (find_first_larger([1,2,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,6,7,8],5) == 17)

def find_first_larger (_arr, _k):
    if (len(_arr) == 0):
        return -1
    if _k < _arr[0] or _k >_arr[-1]:
        return -1
    l = 0
    u = len(_arr) - 1
    
    new_k = _k - 0.5
    while u>l:
        m = l + int ((u-l)/2)
        if _arr[m] == new_k:
            return m   #never happen
        elif _arr[m] < new_k:
            l=m+1
        elif _arr[m] > new_k:
            u=m-1
    
    m = l + int ((u-l)/2)
    # print (u)
    # print (l)
    # print (m)
    # print (_arr[m])
    # print (_k)
    if _arr[m] == _k:
        return m
    if _arr[m] < _k:
        return m+1
    if _arr[m] > _k:
        return m-1

if __name__ == '__main__':
    print (find_first_larger([1,2,3,4,5,6,7,8],4) == 3)