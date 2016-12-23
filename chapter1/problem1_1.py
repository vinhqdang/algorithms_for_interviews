# implement a fast integer square root function
# takes in a 32-bit unsigned integer
# return floor of this 32-bit unsigned integer

def test_sqroot1():
    assert (sq_root(4) == 2)

def test_sqroot2():
    assert (sq_root(0) == 0)

def test_sqroot3():
    assert (sq_root(-5) == -1)

def sq_root(n):
    if n < 0:
        return -1
    return int(n)>>1

if __name__ == "__main__":
    print ("")