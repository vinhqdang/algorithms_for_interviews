# Implement binary search

# test first
# test with pytest
def test_bs1():
    _a1 = [0,1,2,3,4,5,6,7,8]
    _v1 = 3
    assert (binary_search(_a1,_v1) == 3)

def test_bs2():
    assert (binary_search([0,1,2,6,7,7],4) == -1)

# binary search function
# return -1 if could not find
# otherwise return the index of the value
def binary_search (_arr, _value):
    l = 0           # lower
    u = len(_arr) - 1  # upper
    while l <= u:
        # if _arr[l] > _value or _arr[u] < _value:
        #     return -1
        m = int((l+u)/2)
        if _arr[m] == _value:
            return m
        elif _arr[m] < _value:
            l = m + 1
        elif _arr[m] > _value:
            u = m - 1
        # elif l == u and _arr[l] != value:
        #     return -1
    return -1

if __name__ == "__main__":
    print (binary_search([0,1,2],2))